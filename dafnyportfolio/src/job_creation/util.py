import os
import json
import sys
from slugify import slugify
import expand
import zlib


def turn_key_errors_and_null_to_emptystring(format_string, container, key):
    if key in container and container[key] is not None:
        return format_string.format(container[key])
    else:
        return ""


def turn_null_to_emptystring(format_string, value):
    if value is None:
        return ""
    else:
        return format_string.format(value)


def make_result_filename(call):
    return slugify(" ".join(list_filename_parts(call))) + ".json"


def list_filename_parts(call):
    result_file_identifier = [call['dfy-path'], call['procedurename'], call['optionselector'], call['num_instances'],
                              call['only_instances'], call['seed']]
    if "stdin" in call:
        result_file_identifier.append(make_checksum(make_stdin_checksum_input_string(call)))
    return [str(v) for v in result_file_identifier]


def make_stdin_checksum_input_string(call):
    # This is done for compatibility with misguided legacy checksum calculation of old non-list stdin values
    stdin = call['stdin']
    if len(stdin) != 1 or not isinstance(stdin, list):
        return "\n".join(stdin)
    else:
        return "\n".join(stdin[0])


def make_checksum(string):
    return zlib.crc32(string.encode("UTF-8"))


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


def escape_procedurename(call):
    return f"'{call['procedurename']}'"


def make_stdin_heredoc(call):
    if "stdin" in call:
        return f"<< EOFCALL\n{make_stdin_string(call)}\nEOFCALL"
    else:
        return ""


def make_stdin_string(call):
    if isinstance(call["stdin"], list):
        stdin_string = "\n".join(call["stdin"])
    else:
        stdin_string = call["stdin"]
    return stdin_string
