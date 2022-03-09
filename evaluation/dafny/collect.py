import pandas as pd
import json


# Returned columns: problem | procedure | option_selector | processes | seed | only_instances | runtime
def collect_runtimes(result_filenames) -> pd.DataFrame:
    df = pd.DataFrame()

    for filename in result_filenames:
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
        df = pd.concat([df, data])

    return df


def format_only_instances_arg(arg):
    return None if arg is None else arg[0]


def get_arg(arg_name, results):
    if arg_name in results["args"]:
        return [results["args"][arg_name]]
    else:
        return [None]
