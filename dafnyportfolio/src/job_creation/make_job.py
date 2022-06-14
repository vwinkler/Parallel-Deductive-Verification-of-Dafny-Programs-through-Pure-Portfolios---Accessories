import argparse
from util import *


def make_self_announcing_normal_command(args, call, results_filename):
    return "(set -x; {})".format(make_normal_command(args, call, results_filename))


def make_normal_command(args, call, results_filename):
    cmd = ("python "
           f"{args.command} "
           f"{prepend_base_path(args.dfy_base_path, call['dfy-path'])} "
           f"{escape_procedurename(call)} "
           f"{call['optionselector']} "
           f"{results_filename} "
           )
    cmd += turn_key_errors_and_null_to_emptystring("--num-instances {} ", call, "num_instances")
    cmd += turn_key_errors_and_null_to_emptystring("--seed {} ", call, "seed")
    cmd += turn_key_errors_and_null_to_emptystring("--only-instances {} ", call, "only_instances")
    cmd += turn_key_errors_and_null_to_emptystring("--cpu-queue {} ", call, "cpu_queue")
    cmd += turn_null_to_emptystring("--dafny-cmd {} ", args.dafny_cmd)
    cmd += make_stdin_heredoc(call)
    cmd += "\n"

    return cmd


def admit_call_if_result_new(call, results_filename):
    if not os.path.isfile(results_filename):
        print(make_self_announcing_normal_command(args, call, results_filename))


def admit_call(call, results_filename):
    print(make_self_announcing_normal_command(args, call, results_filename))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Turn some job.json into a shell script")
    parser.add_argument(metavar="FILE", dest="filename", type=str)
    parser.add_argument(metavar="CMD", dest="command", type=str)
    parser.add_argument("--dafny-cmd", dest="dafny_cmd", type=str, default=None)
    parser.add_argument("--dfy-base-path", dest="dfy_base_path", type=str, default=None)
    parser.add_argument("--omit-existing", dest="omit_existing", action='store_true')
    args = parser.parse_args()

    print("#!/bin/sh")

    if args.omit_existing:
        admit_call_appropriately = admit_call_if_result_new
    else:
        admit_call_appropriately = admit_call

    for_all_calls(args.filename,
                  lambda call, results_file: admit_call_appropriately(call, results_file))
