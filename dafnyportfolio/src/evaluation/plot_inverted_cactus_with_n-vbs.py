import argparse

import pandas as pd
from matplotlib import pyplot as plt

from cactus_plotting import prepare_for_inverted_cactus
from collection_persistence import load_collection
from linestyles import get_color, get_marker, get_zorder
from util import ensure_surrounding_directory_exists
from vbs import find_n_vbs_results


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Make inverted cactus plot")
        parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
        parser.add_argument("--max-runtime", dest="max_runtime", type=float, default=600)
        parser.add_argument("--plot-file", dest="plot_file", type=str)
        self.args = parser.parse_args()

    def run(self):
        df = load_collection(self.args.results_collection_in)
        df_with_vbs = self.add_all_n_vbs_to_results(df, [1, 2, 4, 8])
        df_with_vbs = self.filter_timeouts(df_with_vbs)
        df_with_vbs = self.accumulate_iterations(df_with_vbs)
        x_max = self.calculate_right_x_limit(df_with_vbs)

        runtime_chart = prepare_for_inverted_cactus(df_with_vbs, x_max, ["approach", "num_cores"])
        runtime_chart = self.sort_configurations(runtime_chart)
        self.plot(runtime_chart, x_max)

    def add_all_n_vbs_to_results(self, df, ps):
        all_vbs_results = []
        for i in ps:
            vbs_results = find_n_vbs_results(df.loc[df["source"] == "all"], i)
            vbs_results["approach"] = "vbs"
            vbs_results["num_cores"] = i
            all_vbs_results.append(vbs_results)
        portfolio_results = df[(df["source"] == "portfolio") & (df["num_running_instances"].isin(ps))].copy()
        portfolio_results["approach"] = "portfolio"
        portfolio_results["num_cores"] = portfolio_results["num_running_instances"]
        kept_columns = ["problem", "procedure", "approach", "num_cores", "runtime"]
        df_with_vbs = pd.concat(
            [portfolio_results[kept_columns]] + [vbs_results[kept_columns] for vbs_results in all_vbs_results])
        return df_with_vbs

    def filter_timeouts(self, df):
        return df.loc[df["runtime"] <= self.args.max_runtime]

    def accumulate_iterations(self, df):
        group_columns = ["problem", "procedure", "approach", "num_cores"]
        return df.groupby(group_columns).agg({"runtime": "median"}).reset_index()

    def calculate_right_x_limit(self, df):
        return self.calculate_longest_total_runtime(df) * 1.05

    def calculate_longest_total_runtime(self, df):
        return df.groupby(["approach", "num_cores"])["runtime"].apply(lambda t: t.agg("sum")).max()

    def sort_configurations(self, runtime_chart):
        runtime_chart = runtime_chart.reindex(sorted(runtime_chart.columns, reverse=True), axis=1)
        return runtime_chart

    def plot(self, runtime_chart, x_max):
        plt.rcParams.update({"text.usetex": True})

        fig, ax = plt.subplots()
        ax.set_xlim(left=0, right=x_max)
        ax.set(xlabel='Time limit (\(s\))', ylabel='Number of solved benchmarks')

        for (approach, p), column in runtime_chart.iteritems():
            if approach == "vbs":
                linestyle = (0, (5, 5))
                ax.plot([0] + list(column), [0] + list(column.index), label=f"\\({p}\\)-VBS",
                        zorder=get_zorder(linestyle), color=get_color(p), alpha=1, linestyle=linestyle, linewidth=1.5)
            else:
                linestyle = (0, (1, 0))
                ax.plot([0] + list(column), [0] + list(column.index), label=f"Portfolio, \\(p={p}\\)",
                        zorder=get_zorder(linestyle), color=get_color(p), alpha=1, linestyle=linestyle, linewidth=1.5)

        ax.legend(loc="lower right")
        if self.args.plot_file:
            ensure_surrounding_directory_exists(self.args.plot_file)
            fig.savefig(self.args.plot_file)
        else:
            plt.show()


if __name__ == '__main__':
    Main().run()
