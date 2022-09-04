import argparse

from collection_persistence import load_collection


def main():
    parser = argparse.ArgumentParser(description="Plot matrix displaying runtime")
    parser.add_argument(metavar="COLLECTION", dest="results_collection", type=str)
    args = parser.parse_args()

    df = load_collection(args.results_collection)
    df.sort_values("start_time", inplace=True)

    print(df[["start_time", "filename"]].to_string())


if __name__ == '__main__':
    main()
