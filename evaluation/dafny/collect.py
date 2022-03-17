import pandas as pd
import json


# Returned columns: problem | procedure | option_selector | processes | seed | only_instances | runtime | is_portfolio
def collect_runtimes(result_filenames) -> pd.DataFrame:
    df = collect_runtime_files(result_filenames)
    df = add_is_portfolio_column(df)
    return df


def add_is_portfolio_column(df):
    df["is_portfolio"] = df.apply(lambda row: row.only_instances == None, axis=1)
    return df


def collect_runtime_files(result_filenames):
    df = pd.DataFrame()
    for filename in result_filenames:
        data = collect_runtime_from_file(filename)
        df = pd.concat([df, data])
    return df


def collect_runtime_from_file(filename):
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
    data = data.astype({"runtime": "float64"})
    return data


def format_only_instances_arg(arg):
    return None if arg is None else arg[0]


def get_arg(arg_name, results):
    if arg_name in results["args"]:
        return [results["args"][arg_name]]
    else:
        return [None]
