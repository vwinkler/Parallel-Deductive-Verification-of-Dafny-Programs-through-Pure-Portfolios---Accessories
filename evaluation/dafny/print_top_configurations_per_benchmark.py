import argparse

import pandas as pd

from collection_persistence import load_collection


def main():
    parser = argparse.ArgumentParser(description="Plot matrix displaying runtime")
    parser.add_argument(metavar="COLLECTION", dest="results_collection", type=str)
    args = parser.parse_args()

    df = load_collection(args.results_collection)

    df = df.drop("[vbs]", axis=1)

    result_df = pd.DataFrame(index=df.index)
    result_df["1st"] = df.idxmin(axis=1)
    result_df["t of 1st"] = df.min(axis=1)

    print(result_df.to_string())


if __name__ == '__main__':
    main()
