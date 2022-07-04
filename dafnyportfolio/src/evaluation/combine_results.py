import argparse

import pandas as pd

from collection_persistence import load_collection, store_collection


def main():
    parser = argparse.ArgumentParser(description="Combine two sets of results")
    parser.add_argument(metavar="COLLECTION_1", dest="results_collection_1", type=str)
    parser.add_argument(metavar="COLLECTION_2", dest="results_collection_2", type=str)
    parser.add_argument(metavar="COLLECTION_OUT", dest="results_collection_out", type=str)
    parser.add_argument("--param", dest="param_name", type=str)
    parser.add_argument("--value_1", "-1", dest="param_value_1", type=str)
    parser.add_argument("--value_2", "-2", dest="param_value_2", type=str)
    args = parser.parse_args()

    df1 = load_collection(args.results_collection_1)
    df2 = load_collection(args.results_collection_2)
    if args.param_name:
        df1[args.param_name] = args.param_value_1
        df2[args.param_name] = args.param_value_2
    df = pd.concat([df1, df2])
    store_collection(args.results_collection_out, df)


if __name__ == '__main__':
    main()
