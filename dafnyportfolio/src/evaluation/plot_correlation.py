from matplotlib import pyplot as plt
from numpy.polynomial.polynomial import polyfit

from collect import *
from collection_persistence import load_collection

quantities = ["start_time", "call_number", "job_number", "call_in_job_number", "median_runtime"]


def get_other_quantity_column_name(other_quantity_arg_name):
    if "median_runtime" == other_quantity_arg_name:
        return "runtime_agg"
    else:
        return other_quantity_arg_name


def main():
    parser = argparse.ArgumentParser(description="Plot matrix displaying runtime")
    parser.add_argument(metavar="COLLECTION", dest="results_collection", type=str)
    parser.add_argument("--plot-file", dest="output_file", type=str)
    parser.add_argument("--boxplot", dest="make_boxplot", action='store_true')
    parser.add_argument("--regression", dest="make_regression", action='store_true')
    parser.add_argument("--with", dest="other_quantity", choices=quantities, default=quantities[0], type=str)
    args = parser.parse_args()

    df = load_collection(args.results_collection)
    other_quantity = get_other_quantity_column_name(args.other_quantity)
    if "runtime_agg" != other_quantity and df[args.other_quantity].isnull().any():
        print(f"Got empty values for some entries at '{args.other_quantity}'.")
        num_empty = df[args.other_quantity].isnull().sum()
        num_not_empty = df[args.other_quantity].count()
        print(f"Ignoring those ({num_empty} ignored; {num_not_empty} left).")
        df = df[~df[args.other_quantity].isnull()]

    group_columns = ["problem", "procedure", "diversification_string"]
    medians_by_group = df.groupby(group_columns).agg({"runtime": "median"}).reset_index()
    df_with_median = pd.merge(df, medians_by_group, how="inner", on=group_columns, suffixes=("", "_agg"))
    df_with_median["runtime_factor"] = df_with_median["runtime"] / df_with_median["runtime_agg"]
    df_with_median["runtime_factor_rank_in_group"] = df_with_median.groupby(group_columns)["runtime_factor"].rank()
    df_with_median.sort_values(other_quantity, inplace=True)

    plt.rcParams.update({"text.usetex": True})
    figure, ax = plt.subplots()
    ax.set(title="", xlabel=args.other_quantity.replace("_", "\\_"), ylabel='runtime / median runtime')
    if not df.empty:
        x = df_with_median[other_quantity]
        y = df_with_median["runtime_factor"]
        if not args.make_boxplot:
            ax.scatter(x=x, y=y, c=df_with_median["runtime_factor_rank_in_group"], s=5)
        else:
            for other_quantity_value, group in df_with_median.groupby([other_quantity]):
                ax.boxplot(group["runtime_factor"], positions=[other_quantity_value], widths=[0.8],
                           flierprops={'marker': 'd', 'markersize': 5, 'markerfacecolor': 'black'})

        if args.make_regression:
            regression_b, regression_m = polyfit(x=x, y=y, deg=1)
            ax.plot(x, regression_b + regression_m * x)

    if args.output_file:
        figure.savefig(args.output_file)
    else:
        plt.show()


if __name__ == '__main__':
    main()
