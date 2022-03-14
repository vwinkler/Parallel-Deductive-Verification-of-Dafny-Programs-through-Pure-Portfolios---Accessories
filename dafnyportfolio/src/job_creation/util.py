import os
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
    result_file_identifier = [call['dfy-path'], call['procedurename'], call['optionselector'], call['num_instances'],
                              call['only_instances'], call['seed']]
    return [str(v) for v in result_file_identifier]


def print_error_if_duplicate(seen_filenames, filename):
    if filename in seen_filenames:
        print("duplicate results file '{}'".format(filename), file=sys.stderr)


def for_all_calls(filename, f):
    with open(filename) as job_file:
        job = json.load(job_file)
        expanded_job = expand.process(job)

        seen_results_filenames = set()
        for call in expanded_job:
            results_filename = make_result_filename(call)
            print_error_if_duplicate(seen_results_filenames, results_filename)
            seen_results_filenames.add(results_filename)
            f(call, results_filename)


def prepend_base_path(base, rest):
    if base is None:
        return rest
    else:
        return os.path.join(base, rest)
