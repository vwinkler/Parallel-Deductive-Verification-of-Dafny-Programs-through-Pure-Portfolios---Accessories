import argparse

import pandas as pd
import matplotlib.pyplot as plt

from collection_persistence import load_collection
from export_html import export_to_html


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Make inverted cactus plot")
        parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
        parser.add_argument("--max-runtime", dest="max_runtime", type=float, default=600)
        parser.add_argument("--plot-file", dest="plot_file", type=str)
        self.args = parser.parse_args()

    def run(self):
        df = load_collection(self.args.results_collection_in)
        df = self.accumulate_iterations(df)
        x_max = self.calculate_right_x_limit(df)

        runtime_chart = self.make_sorted_runtime_chart(df)
        runtime_chart = self.fill_mising_results(runtime_chart, x_max)
        runtime_chart = self.calculate_prefix_sums(runtime_chart)

        self.plot(runtime_chart, x_max)

    def accumulate_iterations(self, df):
        group_columns = ["problem", "procedure", "diversification_string"]
        return df.groupby(group_columns).agg({"runtime": "median"}).reset_index()

    def make_sorted_runtime_chart(self, df):
        df = df.sort_values(by="runtime", ignore_index=True, ascending=True)
        runtimes_by_diversification = {div_string: runtimes.reset_index(drop=True) for div_string, runtimes in
                                       df.groupby("diversification_string")["runtime"]}
        new_df = pd.DataFrame(runtimes_by_diversification)
        return new_df

    def calculate_right_x_limit(self, df):
        return self.calculate_longest_total_runtime(df) * 1.05

    def calculate_longest_total_runtime(self, df):
        def sum_up_finished_runtimes(t):
            return t[t <= self.args.max_runtime].agg("sum")

        return df.groupby("diversification_string")["runtime"].apply(sum_up_finished_runtimes).max()

    def fill_mising_results(self, df, x_max):
        return df.fillna(x_max)

    def calculate_prefix_sums(self, new_df):
        return new_df.cumsum(axis="index")

    def plot(self, new_df, x_max):
        fig, ax = plt.subplots()
        ax.set_xlim(left=0, right=x_max)
        for column_name, column in new_df.iteritems():
            ax.stairs(column.index, list(column) + [x_max])
        if self.args.plot_file:
            fig.savefig(self.args.plot_file)


if __name__ == '__main__':
    Main().run()
