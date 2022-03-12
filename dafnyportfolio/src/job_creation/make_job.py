import argparse
import json
import sys

from slugify import slugify
import expand


def turn_key_errors_and_null_to_emptystring(format_string, container, key):
    if key in container and container[key] is not None:
        return format_string.format(container[key])
    else:
        return ""


def turn_null_to_emptystring(format_string, value):
    if value is None:
        return ""
    else:
        format_string.format(value)


def make_result_filename(call):
    return slugify(" ".join(make_arg_strings(call))) + ".json"


def make_arg_strings(call):
    result_file_identifier = [call['dfy-path'], call['procedurename'], call['optionselector'],
                              call['optionselector'], call['num_instances'], call['only_instances'],
                              call['seed']]
    return [str(v) for v in result_file_identifier]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Turn some job.json into a shell script")
    parser.add_argument(metavar="FILE", dest="filename", type=str)
    parser.add_argument(metavar="CMD", dest="command", type=str)
    parser.add_argument("--dafny-cmd", dest="dafny_cmd", type=str, default=None)
    args = parser.parse_args()

    print("#!/bin/sh")
    with open(args.filename) as job_file:
        job = json.load(job_file)
        expanded_job = expand.process(job)

        seen_results_filenames = set()
        for call in expanded_job:
            results_filename = make_result_filename(call)
            if results_filename in seen_results_filenames:
                print("duplicate results file '{}'".format(results_filename), file=sys.stderr)
            seen_results_filenames.add(results_filename)

            cmd = (""
                   "(set -x; "
                   "python "
                   f"{args.command} "
                   f"{call['dfy-path']} "
                   f"{call['procedurename']} "
                   f"{call['optionselector']} "
                   f"{results_filename} "
                   )
            cmd += turn_key_errors_and_null_to_emptystring("--num-instances {} ", call, "num_instances")
            cmd += turn_key_errors_and_null_to_emptystring("--seed {} ", call, "seed")
            cmd += turn_key_errors_and_null_to_emptystring("--only-instances {} ", call, "only_instances")
            cmd += turn_null_to_emptystring("--dafny-cmd {} ", args.dafny_cmd)

            cmd += ")"
            print(cmd)
