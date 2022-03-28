import argparse
import datetime
import re
import time
from os.path import abspath

from util import *


def make_commands(args, calls):
    time_sum = sum_times(calls)
    mem_max = max_mems(calls)

    cmd = ""
    if not args.omit_sbatch:
        cmd += f"{make_sbatch_prefix(args, 'job', runtime=time_sum, mem=mem_max)}"
    for call, results_filename in calls:
        if args.skip_existing:
            path = prepend_base_path(args.results_base_path, results_filename)
            cmd += f"if [[ ! -e '{path}' ]]; then\n"
        cmd += f"{make_container_command(args, call, results_filename)}"
        cmd += "\n"
        if args.skip_existing:
            cmd += "else\n"
            cmd += f"echo skipping '{path}'\n"
            cmd += "fi\n"
    if not args.omit_sbatch:
        cmd += make_sbatch_suffix_string()
    return cmd


def max_mems(calls):
    memory_estimates = [parse_memory_value(call["estimated_memory"]) for call, _ in calls if "estimated_memory" in call]

    if len(memory_estimates) > 0:
        return max([0] + memory_estimates)
    else:
        return None


def parse_memory_value(memory_value):
    match = re.search("^([0-9]+)M$", memory_value)
    if match is None:
        raise RuntimeError("Value at 'memory' is invalid. Has to be i.e. '123M'.")
    mem = int(match.group(1))
    return mem


def sum_times(calls):
    runtimes = [parse_runtime_value_to_seconds(call["estimated_runtime"]) for call, _ in calls if
                "estimated_runtime" in call]
    if len(runtimes) > 0:
        return str(datetime.timedelta(seconds=(sum(runtimes))))
    else:
        return None


def parse_runtime_value_to_seconds(runtime_value):
    t = time.strptime(runtime_value, "%H:%M:%S")
    return datetime.timedelta(hours=t.tm_hour, minutes=t.tm_min, seconds=t.tm_sec).total_seconds()


def make_sbatch_prefix(args, output_filename, runtime=None, mem=None):
    return make_sbatch_prefix_string(make_sbatch_prefix_args(args, output_filename, runtime, mem))


def make_sbatch_prefix_args(args, output_filename, runtime=None, mem=None):
    result = [f"-o {prepend_base_path(args.results_base_path, output_filename)}.out",
              f"--partition={args.partition}",
              "--exclusive",
              turn_null_to_emptystring("--time {}", runtime),
              turn_null_to_emptystring("--mem {}", mem)]
    result = [arg for arg in result if arg != ""]
    return result


def make_sbatch_prefix_string(cmd_args):
    cmd = "sbatch << EOF\n#!/bin/sh\n"
    for arg in cmd_args:
        cmd += f"#SBATCH {arg}\n"
    return cmd


def make_sbatch_suffix_string():
    return "EOF"


def make_container_command(args, call, results_filename):
    return make_container_command_string(make_container_command_args(args, call, results_filename))


def make_container_command_args(args, call, results_filename):
    results_base_path = abspath(args.results_base_path)
    dfy_base_path = abspath(args.dfy_base_path)
    cmd_args = [f"{make_container_start_command(args.container_framework)}",
                f"{make_mount_argument(args.container_framework, results_base_path, '/result/', read_only=False)}",
                f"{make_mount_argument(args.container_framework, dfy_base_path, '/benchmarks/', read_only=True)}",
                f"{args.container}", f"{prepend_base_path('/benchmarks/', call['dfy-path'])}",
                f"{escape_procedurename(call)}", f"{call['optionselector']}",
                f"{prepend_base_path('/result/', results_filename)}", "--dafny-cmd /opt/dafny/dafny",
                turn_key_errors_and_null_to_emptystring("--num-instances {} ", call, "num_instances"),
                turn_key_errors_and_null_to_emptystring("--seed {} ", call, "seed"),
                turn_key_errors_and_null_to_emptystring("--only-instances {} ", call, "only_instances")]
    cmd_args = [arg for arg in cmd_args if arg != ""]
    return cmd_args


def make_container_command_string(cmd_args):
    return " ".join(cmd_args)


def make_container_start_command(framework):
    if framework == "enroot":
        return "enroot start"
    if framework == "docker":
        return "docker run"


def make_mount_argument(framework, host_dir, container_dir, read_only):
    if framework == "enroot":
        return f"--mount={host_dir}:{container_dir}"
    if framework == "docker":
        modifier = 'ro' if read_only else 'z'
        return f"--volume={host_dir}:{container_dir}:{modifier}"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Turn some job.json into a shell script")
    parser.add_argument(metavar="FILE", dest="filename", type=str)
    parser.add_argument(metavar="PARTITION", dest="partition", type=str)
    parser.add_argument(metavar="CONTAINER", dest="container", type=str)
    parser.add_argument("--container-framework", dest="container_framework", type=str, default="enroot")
    parser.add_argument("--dfy-base-path", dest="dfy_base_path", type=str, default=None)
    parser.add_argument("--results-base-path", dest="results_base_path", type=str, default=".")
    parser.add_argument("--omit-sbatch", dest="omit_sbatch", action='store_true')
    parser.add_argument("--skip-existing", dest="skip_existing", action='store_true')
    args = parser.parse_args()

    print("#!/bin/sh")

    calls = []
    for_all_calls(args.filename, lambda call, results_file: calls.append((call, results_file)))
    print(make_commands(args, calls))
