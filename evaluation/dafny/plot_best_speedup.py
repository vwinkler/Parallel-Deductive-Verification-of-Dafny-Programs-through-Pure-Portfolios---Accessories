import argparse

import seaborn as sns

from collection_persistence import load_collection


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Make speedup plot with best configurations")
        parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
        parser.add_argument("--plot-file", dest="plot_file", type=str)
        parser.add_argument("--info-file", dest="info_file", type=str)
        parser.add_argument("--boxplot", dest="make_boxplot", action='store_true')
        self.args = parser.parse_args()

    def run(self):
        df = load_collection(self.args.results_collection_in)
        if not self.args.make_boxplot:
            df_mean_runtime = self.accumulate_iterations(df)
        else:
            df_mean_runtime = df
        df_total_mean_runtime = self.accumulate_benchmarks(df_mean_runtime)
        df_min_mean_total_runtime = self.pick_best_configurations_per_cpu_count(df_total_mean_runtime)

        if self.args.plot_file:
            self.plot(self.args.plot_file, df_min_mean_total_runtime)

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

    def plot(self, filename, df_min_mean_total_runtime):
        if self.args.make_boxplot:
            ax = sns.boxplot(x="num_running_instances", y="runtime", data=df_min_mean_total_runtime)
        else:
            ax = sns.lineplot(x="num_running_instances", y="runtime", data=df_min_mean_total_runtime)
        figure = ax.get_figure()
        ax.set_ylim(bottom=0)
        figure.savefig(filename)


if __name__ == '__main__':
    Main().run()
