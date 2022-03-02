import pandas as pd
import json


# Returned columns: problem | procedure | option_selector | processes | seed | runtime
def collect_runtimes(result_filenames) -> pd.DataFrame:
    df = pd.DataFrame()

    for filename in result_filenames:
        with open(filename) as file:
            results = json.load(file)
        data = pd.DataFrame({"problem": [results["args"]["dafny_file"]],
                             "procedure": [results["args"]["procedure_name"]],
                             "option_selector": [(results["args"]["option_selector_name"])],
                             "processes": [len(results["instances"])],
                             "seed": [results["args"]["seed"]],
                             "num_threads" : [results["args"]["num_threads"]],
                             "runtime": [results["total_runtime"]["duration"]]})
        data = data.astype({"runtime": "float64"})
        df = pd.concat([df, data])

    return df
