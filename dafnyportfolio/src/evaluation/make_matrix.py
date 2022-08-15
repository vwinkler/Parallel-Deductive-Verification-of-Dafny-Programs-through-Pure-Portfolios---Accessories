import argparse

from collection_persistence import load_collection, store_collection
from util import make_matrix


def main():
    parser = argparse.ArgumentParser(description="Penalize results")
    parser.add_argument(metavar="COLLECTION_IN", dest="matrix_in", type=str)
    parser.add_argument(metavar="COLLECTION_OUT", dest="matrix_out", type=str)
    parser.add_argument("--agg", dest="agg", default="median", type=str)
    args = parser.parse_args()

    df = load_collection(args.matrix_in)
    df = make_matrix(df, args.agg)
    store_collection(args.matrix_out, df)


if __name__ == '__main__':
    main()
