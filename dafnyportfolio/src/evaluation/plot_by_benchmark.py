import argparse
import random

import numpy as np
from matplotlib import pyplot as plt

import pandas as pd

from collection_persistence import load_collection


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Make inverted cactus plot")
        parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
        parser.add_argument("--max-runtime", dest="max_runtime", type=float)
        parser.add_argument("--plot-file", dest="plot_file", type=str)
        parser.add_argument("--y-scale", dest="y_scale", type=str, choices=["linear", "log"], default="linear")
        self.args = parser.parse_args()

        self.x_column = "benchmark"
        self.y_column = "speedup"
        self.z_column = "diversification_string"

    def run(self):
        df = load_collection(self.args.results_collection_in)
        df = self.accumulate_iterations(df)
        df["benchmark"] = self.make_benchmark_column(df)
        df["default_runtime"] = self.make_default_runtime_column(df)
        df[self.y_column] = df["default_runtime"] / df["runtime"]
        df = self.filter_results(df)
        self.plot(df)

    def filter_results(self, df):
        result = df
        if self.args.max_runtime:
            result = result[df["runtime"] < self.args.max_runtime]
        return result

    def plot(self, df):
        plt.rcParams.update({"text.usetex": True})
        figure, ax = plt.subplots()
        x_values = np.array(df[self.x_column])
        y_values = np.array(df[self.y_column])
        z_values = np.array(df[self.z_column])
        scatter_plot = ax.scatter(x=x_values, y=y_values)
        plt.yscale(self.args.y_scale)
        plt.tight_layout()
        if self.args.plot_file:
            figure.savefig(self.args.plot_file)
        else:
            annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                                bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))

            def update_annot(ind):
                pos = scatter_plot.get_offsets()[ind["ind"][0]]
                annot.xy = pos
                text = "\n".join([z_values[n] for n in ind["ind"]])
                text = text.replace("_", "\\_")
                annot.set_text(text)
                annot.get_bbox_patch().set_alpha(0.4)

            def hover(event):
                vis = annot.get_visible()
                if event.inaxes == ax:
                    cont, ind = scatter_plot.contains(event)
                    if cont and len(ind) < 10:
                        update_annot(ind)
                        annot.set_visible(True)
                        figure.canvas.draw_idle()
                        ax.set(title=f"{random.choice([1, 2, 3])}")
                    else:
                        if vis:
                            annot.set_visible(False)
                            figure.canvas.draw_idle()

            figure.canvas.mpl_connect("motion_notify_event", hover)
            plt.show()

    def make_default_runtime_column(self, df):
        default_runtimes = df[df["diversification_string"] == ""]
        columns = ["problem", "procedure"]
        return pd.merge(df, default_runtimes, how="left", on=columns, suffixes=("", "_default"))["runtime_default"]

    def make_benchmark_column(self, df):
        columns_sorted = ["problem", "procedure"]
        df_benchmarks = df[columns_sorted].groupby(columns_sorted).size().reset_index(name="Freq")
        df_benchmarks.sort_values(columns_sorted, inplace=True)
        benchmarks = list(df_benchmarks[columns_sorted].itertuples(index=False, name=None))
        renaming = {benchmark: num for benchmark, num in zip(benchmarks, range(len(benchmarks)))}
        return df.apply(lambda row: renaming[(row["problem"], row["procedure"])], axis=1)

    def accumulate_iterations(self, df):
        group_columns = ["problem", "procedure", "diversification_string"]
        return df.groupby(group_columns).agg({"runtime": "median"}).reset_index()


if __name__ == '__main__':
    Main().run()
