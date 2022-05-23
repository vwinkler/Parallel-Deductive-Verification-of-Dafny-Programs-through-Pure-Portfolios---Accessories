import argparse

import pandas as pd

from collection_persistence import load_collection


def main():
    parser = argparse.ArgumentParser(description="Plot matrix displaying runtime")
    parser.add_argument(metavar="COLLECTION", dest="results_collection", type=str)
    parser.add_argument("--max-runtime", dest="max_runtime", type=float, default=600)
    args = parser.parse_args()

    df = load_collection(args.results_collection)

    df = df.transpose()
    df = df.drop("[total]", axis=1)

    min_value_of_timedout_runs = args.max_runtime + 10
    result_df = pd.DataFrame(index=df.index)
    result_df["id"] = range(len(df.index))
    result_df["total_runtime"] = df.sum(axis=1)
    result_df["timeout_count"] = df[df > min_value_of_timedout_runs].count(axis=1)
    result_df.sort_values(["total_runtime", "timeout_count"], ascending=True, inplace=True)

    print(result_df.to_string())


if __name__ == '__main__':
    main()
