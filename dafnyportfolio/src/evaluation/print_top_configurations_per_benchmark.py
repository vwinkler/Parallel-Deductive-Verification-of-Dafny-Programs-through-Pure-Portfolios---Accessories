import argparse

from collection_persistence import load_collection


def main():
    parser = argparse.ArgumentParser(description="Plot matrix displaying runtime")
    parser.add_argument(metavar="COLLECTION", dest="results_collection", type=str)
    args = parser.parse_args()

    df = load_collection(args.results_collection)

    df = df.drop("[vbs]", axis=1)

    melted_df = df.melt(value_name="runtime", ignore_index=False).reset_index().rename(columns={"index": "benchmark"})
    melted_df["problem"] = melted_df.apply(lambda row: row["benchmark"][0], axis=1)
    melted_df["procedure"] = melted_df.apply(lambda row: row["benchmark"][1], axis=1)
    melted_df = melted_df.drop(columns=["benchmark"], axis=1)
    melted_df = melted_df.sort_values("runtime").groupby(["problem", "procedure"]).head(3)
    melted_df = melted_df.set_index(["problem", "procedure", "configuration"])
    print(melted_df.sort_values(["problem", "procedure"], kind="stable").to_string())


if __name__ == '__main__':
    main()
