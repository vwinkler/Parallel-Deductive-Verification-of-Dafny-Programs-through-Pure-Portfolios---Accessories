import argparse

from collection_persistence import load_collection


def export_to_html(filename, df):
    with open(filename, "w") as f:
        df.to_html(f)


def main():
    parser = argparse.ArgumentParser(description="Export data frame as html")
    parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
    parser.add_argument(metavar="OUTFILE", dest="output_file", type=str)
    args = parser.parse_args()

    df = load_collection(args.results_collection_in)
    export_to_html(args.output_file, df)


if __name__ == '__main__':
    main()
