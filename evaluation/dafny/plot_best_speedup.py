import argparse

import seaborn as sns

from collection_persistence import load_collection


def main():
    parser = argparse.ArgumentParser(description="Make speedup plot with best configurations")
    parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
    parser.add_argument("--plot-file", dest="plot_file", type=str)
    parser.add_argument("--info-file", dest="info_file", type=str)
    args = parser.parse_args()

    df = load_collection(args.results_collection_in)
    df_mean_runtime = accumulate_iterations(df)
    df_total_mean_runtime = accumulate_benchmarks(df_mean_runtime)
    df_min_mean_total_runtime = pick_best_configurations_per_cpu_count(df_total_mean_runtime)

    if args.plot_file:
        plot(args.plot_file, df_min_mean_total_runtime)

    if args.info_file:
        print_info(df_min_mean_total_runtime, args.info_file)


def print_info(df_min_mean_total_runtime, info_file_name):
    with open(info_file_name, "w") as file:
        file.write(df_min_mean_total_runtime.to_string())


def accumulate_iterations(df):
    return df.groupby(["problem", "procedure", "diversification_string", "num_running_instances"]).agg(
        {"runtime": "mean"}).reset_index()


def accumulate_benchmarks(df_mean_runtime):
    df_total_mean_runtime = df_mean_runtime.groupby(["diversification_string", "num_running_instances"]).agg(
        {"runtime": "sum"}).reset_index()
    return df_total_mean_runtime


def pick_best_configurations_per_cpu_count(df_total_mean_runtime):
    index_of_best_configurations = df_total_mean_runtime.groupby("num_running_instances")["runtime"].idxmin()
    return df_total_mean_runtime.loc[index_of_best_configurations]


def plot(filename, df_min_mean_total_runtime):
    ax = sns.lineplot(x="num_running_instances", y="runtime", data=df_min_mean_total_runtime)
    figure = ax.get_figure()
    ax.set_ylim(bottom=0)
    figure.savefig(filename)


if __name__ == '__main__':
    main()
