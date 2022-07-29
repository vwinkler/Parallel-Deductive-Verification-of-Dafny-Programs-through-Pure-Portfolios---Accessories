import argparse

from matplotlib import pyplot as plt

from collection_persistence import load_collection
from cactus_plotting import prepare_for_inverted_cactus
from linestyles import get_color, get_linestyle, get_marker, get_zorder


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
        df = self.filter_timeouts(df)
        x_max = self.calculate_right_x_limit(df)

        runtime_chart = prepare_for_inverted_cactus(df, x_max, "diversification_string")
        self.plot(runtime_chart, x_max)

    def filter_timeouts(self, df):
        return df[df["runtime"] <= self.args.max_runtime]

    def accumulate_iterations(self, df):
        group_columns = ["problem", "procedure", "diversification_string"]
        return df.groupby(group_columns).agg({"runtime": "median"}).reset_index()

    def calculate_right_x_limit(self, df):
        return self.calculate_longest_total_runtime(df) * 1.05

    def calculate_longest_total_runtime(self, df):
        return df.groupby("diversification_string")["runtime"].apply(lambda t: t.agg("sum")).max()

    def plot(self, runtime_chart, x_max):
        plt.rcParams.update({"text.usetex": True})
        fig, ax = plt.subplots()
        ax.set_xlim(left=0, right=x_max)
        ax.set(xlabel='Time limit (\(s\))', ylabel='Number of solved benchmarks')

        for column_name, column in runtime_chart.iteritems():
            p = column_name.count(";") + 1 - column_name.count("None")

            linestyle = get_linestyle(p)
            ax.plot([0] + list(column), [0] + list(column.index), label=f"\(p={p}\)", color=get_color(p), alpha=1,
                    linestyle=linestyle, linewidth=1.5, marker=get_marker(p), markevery=[-1], markersize=5,
                    zorder=get_zorder(linestyle))

        ax.legend(loc="lower right")
        if self.args.plot_file:
            fig.savefig(self.args.plot_file)
        else:
            plt.show()


if __name__ == '__main__':
    Main().run()
