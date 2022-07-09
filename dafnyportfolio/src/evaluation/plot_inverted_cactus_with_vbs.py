import argparse

import pandas as pd
from matplotlib import pyplot as plt

from cactus_plotting import prepare_for_inverted_cactus
from collection_persistence import load_collection
from util import ensure_surrounding_directory_exists
from vbs import find_vbs_results


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Make inverted cactus plot")
        parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
        parser.add_argument("--max-runtime", dest="max_runtime", type=float, default=600)
        parser.add_argument("--plot-file", dest="plot_file", type=str)
        parser.add_argument("--approach", dest="approach", type=str, choices=["s=p", "s=8p", "s=const>>p"])
        self.args = parser.parse_args()

    def run(self):
        df = load_collection(self.args.results_collection_in)
        df = self.filter_timeouts(df)
        df_with_vbs = self.add_vbs_to_results(df)
        df_with_vbs = self.accumulate_iterations(df_with_vbs)
        x_max = self.calculate_right_x_limit(df_with_vbs)

        runtime_chart = prepare_for_inverted_cactus(df_with_vbs, x_max, "configuration")
        runtime_chart = self.sort_configurations(runtime_chart)
        self.plot(runtime_chart, x_max)

    def add_vbs_to_results(self, df):
        vbs_results = find_vbs_results(df.loc[df["source"] == "all"])
        vbs_results["configuration"] = "vbs"
        portfolio_results = df.loc[df["source"] == "portfolio"]
        portfolio_results["configuration"] = portfolio_results["diversification_string"]
        kept_columns = ["problem", "procedure", "configuration", "runtime"]
        df_with_vbs = pd.concat([portfolio_results[kept_columns], vbs_results[kept_columns]])
        return df_with_vbs

    def filter_timeouts(self, df):
        return df.loc[df["runtime"] <= self.args.max_runtime]

    def accumulate_iterations(self, df):
        group_columns = ["problem", "procedure", "configuration"]
        return df.groupby(group_columns).agg({"runtime": "median"}).reset_index()

    def calculate_right_x_limit(self, df):
        return self.calculate_longest_total_runtime(df) * 1.05

    def calculate_longest_total_runtime(self, df):
        return df.groupby("configuration")["runtime"].apply(lambda t: t.agg("sum")).max()

    def sort_configurations(self, runtime_chart):
        runtime_chart = runtime_chart.reindex(sorted(runtime_chart.columns, reverse=True), axis=1)
        return runtime_chart

    def plot(self, runtime_chart, x_max):
        plt.rcParams.update({"text.usetex": True})

        fig, ax = plt.subplots()
        ax.set_xlim(left=0, right=x_max)

        for configuration, column in runtime_chart.iteritems():
            if configuration == "vbs":
                linestyle = "dashed"
                label = "VBS"
            else:
                linestyle = "solid"
                label = f"\\(p={len(configuration.split(';')) - configuration.count('None')}\\)"
            ax.stairs(column.index, list(column) + [x_max], linestyle=linestyle, label=label)

        ax.legend(loc="lower right")
        if self.args.plot_file:
            ensure_surrounding_directory_exists(self.args.plot_file)
            fig.savefig(self.args.plot_file)
        plt.show()


if __name__ == '__main__':
    Main().run()
