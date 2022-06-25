import argparse

from collection_persistence import load_collection


def main():
    parser = argparse.ArgumentParser(description="Print axis labels (column and index titles)")
    parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
    args = parser.parse_args()

    df = load_collection(args.results_collection_in)
    print("\n".join([f"{k}\t{r}" for k, r in enumerate(df.index)]))
    print("\n\n")
    print("\n".join([f"{k}\t{c}" for k, c in enumerate(df.columns)]))


if __name__ == '__main__':
    main()
