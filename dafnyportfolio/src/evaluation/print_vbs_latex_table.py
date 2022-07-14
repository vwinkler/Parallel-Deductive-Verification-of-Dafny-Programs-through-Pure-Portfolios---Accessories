import argparse
import pandas as pd

from collection_persistence import load_collection
from vbs import find_vbs_results


def main():
    parser = argparse.ArgumentParser(description="Plot matrix displaying runtime")
    parser.add_argument(metavar="COLLECTION", dest="results_collection", type=str)
    parser.add_argument("--prefix", dest="prefix", type=str, default="")
    parser.add_argument("--suffix", dest="suffix", type=str, default="")
    args = parser.parse_args()

    df = load_collection(args.results_collection)

    top_config_df = find_vbs_results(df)
    top_config_df["Benchmark"] = range(1, len(top_config_df) + 1)
    top_config_df["Configuration"] = top_config_df[("diversification", 0)].str.replace("_", "\\_")
    top_config_df["Configuration"] = args.prefix + top_config_df["Configuration"] + args.suffix
    top_config_df["Runtime"] = top_config_df["runtime"]
    top_config_df.loc[top_config_df["Runtime"] > 600, "Configuration"] = "not solved by any configuration"
    top_config_df.loc[top_config_df["Runtime"] > 600, "Runtime"] = 1200
    top_config_df.sort_values(["problem", "procedure"], ascending=True, inplace=True)

    with pd.option_context("max_colwidth", 1000):
        columns = ["Benchmark", "Configuration", "Runtime"]
        print(top_config_df[columns].to_latex(escape=False, index=False, float_format="\\({:0.2f}\, s\\)".format))


if __name__ == '__main__':
    main()
