import argparse

from collection_persistence import load_collection, store_collection
from runtime_penalization import penalize_results_table


def main():
    parser = argparse.ArgumentParser(description="Penalize results")
    parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
    parser.add_argument(metavar="COLLECTION_OUT", dest="results_collection_out", type=str)
    args = parser.parse_args()

    df = load_collection(args.results_collection_in)
    penalize_results_table(df)
    store_collection(args.results_collection_out, df)


if __name__ == '__main__':
    main()
