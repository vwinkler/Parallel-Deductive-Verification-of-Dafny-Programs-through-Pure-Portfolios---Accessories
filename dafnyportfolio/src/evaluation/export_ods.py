import argparse

from collection_persistence import load_collection


def export_to_ods(filename, df):
    with open(filename, "wb") as f:
        try:
            df.to_excel(f, engine="odf")
        except ModuleNotFoundError as e:
            print(f"Could not save as '{f.name}': {e}")


def main():
    parser = argparse.ArgumentParser(description="Export data frame as ods")
    parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
    parser.add_argument(metavar="OUTFILE", dest="output_file", type=str)
    args = parser.parse_args()

    df = load_collection(args.results_collection_in)
    export_to_ods(args.output_file, df)


if __name__ == '__main__':
    main()
