import argparse

import seaborn as sns
from matplotlib import pyplot as plt

from collection_persistence import load_collection


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Make speedup plot with best configurations")
        parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
        parser.add_argument("--plot-file", dest="plot_file", type=str)
        parser.add_argument("--info-file", dest="info_file", type=str)
        parser.add_argument("--boxplot", dest="make_boxplot", action='store_true')
        parser.add_argument("--show-plot", dest="show", action='store_true')
        self.args = parser.parse_args()

    def run(self):
        df = load_collection(self.args.results_collection_in)
        num_benchmarks = len(df[["problem", "procedure"]].value_counts())
        if not self.args.make_boxplot:
            df_mean_runtime = self.accumulate_iterations(df)
        else:
            df_mean_runtime = df
        df_total_mean_runtime = self.accumulate_benchmarks(df_mean_runtime)
        df_min_mean_total_runtime = self.pick_best_configurations_per_cpu_count(df_total_mean_runtime)
        df_min_mean_total_runtime["runtime"] = df_min_mean_total_runtime["runtime"] / num_benchmarks

        if self.args.plot_file or self.args.show:
            self.plot(self.args.plot_file, df_min_mean_total_runtime, self.args.show)

        if self.args.info_file:
            self.print_info(df_min_mean_total_runtime, self.args.info_file)

    def print_info(self, df_min_mean_total_runtime, info_file_name):
        with open(info_file_name, "w") as file:
            file.write(df_min_mean_total_runtime.to_string())

    def accumulate_iterations(self, df):
        return df.groupby(["problem", "procedure", "diversification_string", "num_running_instances"]).agg(
            {"runtime": "mean"}).reset_index()

    def accumulate_benchmarks(self, df_mean_runtime):
        if self.args.make_boxplot:
            columns = ["diversification_string", "num_running_instances", "seed"]
        else:
            columns = ["diversification_string", "num_running_instances"]
        df_total_mean_runtime = df_mean_runtime.groupby(columns).agg({"runtime": "sum"}).reset_index()
        return df_total_mean_runtime

    def pick_best_configurations_per_cpu_count(self, df_total_mean_runtime):
        if self.args.make_boxplot:
            columns = ["num_running_instances", "seed"]
        else:
            columns = ["num_running_instances"]
        index_of_best_configurations = df_total_mean_runtime.groupby(columns)[
            "runtime"].idxmin()
        return df_total_mean_runtime.loc[index_of_best_configurations]

    def plot(self, filename, df_min_mean_total_runtime, show):
        plt.rcParams.update({"text.usetex": True})
        if self.args.make_boxplot:
            _, ax = plt.subplots()
            for num_running_instances, group in df_min_mean_total_runtime.groupby(["num_running_instances"]):
                ax.boxplot(group["runtime"], positions=[num_running_instances], widths=[0.8],
                           flierprops={'marker': 'd', 'markersize': 5, 'markerfacecolor': 'black'})
        else:
            ax = sns.lineplot(x="num_running_instances", y="runtime", data=df_min_mean_total_runtime)
        ax.set(xlabel='Number \(p\) of processes', ylabel='Cumulative PAR-2 score/\#benchmarks (\(s\))')
        figure = ax.get_figure()
        ax.set_ylim(bottom=0)
        if filename:
            figure.savefig(filename)
        if show:
            plt.show()


if __name__ == '__main__':
    Main().run()
