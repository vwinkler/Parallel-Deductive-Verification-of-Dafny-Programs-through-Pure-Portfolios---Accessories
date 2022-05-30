import argparse
import json
import sys

from progress.bar import Bar
from enum import Enum


def shorten_string(num_characters, string):
    if len(string) < num_characters:
        return string
    else:
        return string[:(num_characters - 3)] + "..."


def check_files(filenames):
    bar = Bar("Processing", max=len(filenames), suffix='%(percent)d%%    ')
    successes = 0
    for filename in filenames:
        if check_file_by_name(filename):
            successes += 1
        bar.next()

    bar.finish()
    print(f"{successes}/{len(filenames)}")


def check_file_by_name(filename):
    try:
        with open(filename) as file:
            return check_file(file)
    except FileNotFoundError:
        print_error(filename, 'file not found')
        return False


def check_file(file):
    filename = file.name
    try:
        results = json.load(file)
    except json.decoder.JSONDecodeError as e:
        print_error(filename, f"json error: '{e}'")
        return False

    try:
        termination_reason = results["termination_reason"]
    except KeyError:
        termination_reason = None

    try:
        if termination_reason is not None and termination_reason == "portfolio timeout":
            return True
    except TypeError:
        pass

    try:
        instances = results["instances"]
    except KeyError:
        print_error(filename, 'syntax error, missing instances')
        return False

    if len(instances) == 0:
        print_error(filename, 'no instance')
        return False

    num_instances_with_at_least_once_method = 0
    try:
        for instance in instances:
            try:
                xml = instance["xml"]
            except KeyError:
                print_error(filename, 'syntax error, missing xml')
                return False
            except TypeError:
                print_error(filename, 'syntax error, ill-formed instance')
                return False

            try:
                methods = xml["methods"]
            except KeyError:
                print_error(filename, 'syntax error, missing methods')
                return False
            except TypeError:
                continue

            try:
                if len(methods) > 1:
                    print_error(filename, 'at least one instance has more than one method')
                    return False
                if len(methods) == 1:
                    num_instances_with_at_least_once_method += 1
            except TypeError:
                print_error(filename, 'syntax error, ill-formed method')
                return False
    except TypeError:
        print_error(filename, 'syntax error, ill-formed instances list')
        return False

    if num_instances_with_at_least_once_method > 0:
        return True
    else:
        print_error(filename, 'no instance has a method')
        return False


def print_error(filename, message):
    print(f"{filename}: {message}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Plot matrix displaying runtime")
    parser.add_argument(metavar="RESULTFILE", dest="result_filenames", type=str, nargs="+",
                        help="or '-' to read from stdin (one filename per line)")
    args = parser.parse_args()

    if args.result_filenames != ["-"]:
        check_files(args.result_filenames)
    else:
        check_files([filename for filename in sys.stdin.read().splitlines()])
