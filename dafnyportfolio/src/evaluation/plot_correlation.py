from matplotlib import pyplot as plt

from collect import *
from collection_persistence import load_collection

quantities = ["start_time"]


def main():
    parser = argparse.ArgumentParser(description="Plot matrix displaying runtime")
    parser.add_argument(metavar="COLLECTION", dest="results_collection", type=str)
    parser.add_argument("--plot-file", dest="output_file", type=str)
    parser.add_argument("--with", dest="other_quantity", choices=quantities, default=quantities[0], type=str)
    args = parser.parse_args()

    df = load_collection(args.results_collection)
    group_columns = ["problem", "procedure", "diversification_string"]
    medians_by_group = df.groupby(group_columns).agg({"runtime": "median"}).reset_index()
    df_with_median = pd.merge(df, medians_by_group, how="inner", on=group_columns, suffixes=("", "_agg"))
    df_with_median["runtime_factor"] = df_with_median["runtime"] / df_with_median["runtime_agg"]

    figure, ax = plt.subplots()
    ax.scatter(x=df_with_median[args.other_quantity], y=df_with_median["runtime_factor"])

    if args.output_file:
        figure.savefig(args.output_file)
    else:
        plt.show()


if __name__ == '__main__':
    main()
