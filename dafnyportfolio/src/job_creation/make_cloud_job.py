from os.path import abspath
import argparse
from util import *


def make_command(args, call, results_filename):
    cmd = ""
    if not args.omit_sbatch:
        cmd += make_sbatch_prefix(args, call, results_filename)
    cmd += make_container_command(args, call, results_filename)
    return cmd


def make_sbatch_prefix(args, call, results_filename):
    cmd = (
        f"sbatch "
        f"-o {prepend_base_path(args.results_base_path, results_filename)}.out "
        f"--partition={args.partition} "
        "--exclusive "
    )
    cmd += turn_key_errors_and_null_to_emptystring("--time {} ", call, "estimated_runtime")
    cmd += turn_key_errors_and_null_to_emptystring("--mem {} ", call, "estimated_memory")
    return cmd


def make_container_command(args, call, results_filename):
    results_base_path = abspath(args.results_base_path)
    dfy_base_path = abspath(args.dfy_base_path)
    cmd = (
        f"{make_container_start_command(args.container_framework)} "
        f"{make_mount_argument(args.container_framework, results_base_path, '/result/', read_only=False)} "
        f"{make_mount_argument(args.container_framework, dfy_base_path, '/benchmarks/', read_only=True)} "
        f"{args.container} "
        f"{prepend_base_path('/benchmarks/', call['dfy-path'])} "
        f"{call['procedurename']} "
        f"{call['optionselector']} "
        f"{prepend_base_path('/result/', results_filename)} "
        "--dafny-cmd /opt/dafny/dafny "
    )
    cmd += turn_key_errors_and_null_to_emptystring("--num-instances {} ", call, "num_instances")
    cmd += turn_key_errors_and_null_to_emptystring("--seed {} ", call, "seed")
    cmd += turn_key_errors_and_null_to_emptystring("--only-instances {} ", call, "only_instances")
    return cmd


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
    args = parser.parse_args()

    print("#!/bin/sh")

    for_all_calls(args.filename,
                  lambda call, results_file: print(make_command(args, call, results_file)))
