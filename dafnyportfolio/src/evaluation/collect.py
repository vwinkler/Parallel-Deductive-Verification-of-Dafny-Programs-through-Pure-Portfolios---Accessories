import argparse
import sys
from typing import Union

import pandas as pd
import json

from collection_persistence import store_collection


def collect_runtimes(result_filenames) -> pd.DataFrame:
    df = collect_runtime_files(result_filenames)
    df = add_is_portfolio_column(df)
    return df


def add_is_portfolio_column(df):
    df["is_portfolio"] = df.apply(lambda row: row.only_instances == None, axis=1)
    return df


def collect_runtime_files(result_filenames):
    max_num_instances = count_max_num_instances(result_filenames)
    data_frames_from_json_files = []
    for filename in result_filenames:
        data_frames_from_json_files.append(collect_runtime_from_file(filename, max_num_instances))
    return pd.concat(data_frames_from_json_files)


def count_max_num_instances(result_filenames):
    max_num_instances = 0
    for filename in result_filenames:
        with open(filename) as file:
            results = json.load(file)
            max_num_instances = max(max_num_instances, len(results["instances"]))
    return max_num_instances


def collect_runtime_from_file(filename, max_num_instances):
    with open(filename) as file:
        results = json.load(file)
    data = pd.DataFrame({"problem": get_arg("dafny_file", results),
                         "procedure": get_arg("procedure_name", results),
                         "option_selector": get_arg("option_selector_name", results),
                         "processes": [len(results["instances"])],
                         "seed": get_arg("seed", results),
                         "num_instances": get_arg("num_instances", results),
                         "only_instances": format_only_instances_arg(get_arg("only_instances", results)),
                         "runtime": [results["total_runtime"]["duration"]],
                         "finished": [has_finished(results)],
                         "correct": [is_correct(results)],
                         "start_time": [pd.to_datetime(results["total_runtime"]["start_readable"])],
                         "call_number": [retrieve_key_value_value(results, "call_number")],
                         "job_number": [retrieve_key_value_value(results, "job_number")],
                         "call_in_job_number": [retrieve_key_value_value(results, "call_in_job_number")],
                         "filename": [filename]})

    div_cells = make_diversification_cells(results, max_num_instances)
    for k, v in div_cells.items():
        data[("diversification", k)] = v
    data["diversification_string"] = "; ".join([str(x) for x in div_cells.values()])
    data["num_running_instances"] = len([div for div in div_cells.values() if div is not None])

    data = data.astype({"runtime": "float64", "start_time": "datetime64"})
    return data


def retrieve_key_value_value(results, key):
    try:
        return int(results["key-values"][key])
    except KeyError:
        return None


def has_finished(results):
    if has_portfolio_timed_out(results):
        return False
    instances_finished = [has_instance_finished(instance) for instance in results["instances"]]
    return any(instances_finished)


def has_instance_finished(instance):
    try:
        return instance["xml"]["methods"][0]["finished"]
    except (TypeError, IndexError):
        return False


def is_correct(results):
    if has_portfolio_timed_out(results):
        return False
    instances_correct = [is_instance_correct(instance) for instance in results["instances"]]
    return any(instances_correct)


def is_instance_correct(instance):
    try:
        return instance["xml"]["methods"][0]["outcome"] == "correct"
    except (TypeError, IndexError):
        return False


def has_portfolio_timed_out(results):
    portfolio_terminated = False
    try:
        if results["termination_reason"] == "portfolio timeout":
            portfolio_terminated = True
    except:
        pass
    return portfolio_terminated


def make_diversification_cells(results, num_cells):
    padded_argument_strings = pad_list(num_cells, None, make_diversification_argument_strings(results))
    return {k: v for k, v in enumerate(padded_argument_strings)}


def make_diversification_argument_strings(results):
    return [" ".join(instance["diversification"]) for instance in results["instances"]]


def pad_list(num_elements, filler_value, unpadded_list):
    return unpadded_list + [filler_value] * (num_elements - len(unpadded_list))


def format_only_instances_arg(arg):
    return None if arg is None else arg[0]


def get_arg(arg_name, results):
    if arg_name in results["args"]:
        return [results["args"][arg_name]]
    else:
        return [None]


def main():
    parser = argparse.ArgumentParser(description="Collect runtimes")
    parser.add_argument(metavar="OUTFILE", dest="results_collection_filename", type=str)
    parser.add_argument(metavar="RESULTFILE", dest="result_filenames", type=str, nargs="+",
                        help="or '-' to read from stdin (one filename per line)")
    args = parser.parse_args()
    if args.result_filenames == ["-"]:
        df = collect_runtimes([filename for filename in sys.stdin.read().splitlines()])
    else:
        df = collect_runtimes(args.result_filenames)
    store_collection(args.results_collection_filename, df)


if __name__ == '__main__':
    main()
