import pandas as pd
import json


def collect_runtimes(result_filenames) -> pd.DataFrame:
    df = collect_runtime_files(result_filenames)
    df = add_is_portfolio_column(df)
    return df


def add_is_portfolio_column(df):
    df["is_portfolio"] = df.apply(lambda row: row.only_instances == None, axis=1)
    return df


def collect_runtime_files(result_filenames):
    max_num_instances = count_max_num_instances(result_filenames)
    df = pd.DataFrame()
    for filename in result_filenames:
        data = collect_runtime_from_file(filename, max_num_instances)
        df = pd.concat([df, data])
    return df


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
                         "runtime": [results["total_runtime"]["duration"]]})

    div_cells = make_diversification_cells(results, max_num_instances)
    for k, v in div_cells.items():
        data[("diversification", k)] = v
    data["num_running_instances"] = len([div for div in div_cells.values() if div is not None])

    data = data.astype({"runtime": "float64"})
    return data


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
