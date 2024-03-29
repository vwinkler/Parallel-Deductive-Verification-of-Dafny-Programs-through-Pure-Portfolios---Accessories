import argparse
import re

from matplotlib import pyplot as plt

from cactus_plotting import prepare_for_inverted_cactus

from collection_persistence import load_collection


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Make inverted cactus plot")
        parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
        parser.add_argument("--max-runtime", dest="max_runtime", type=float, default=600)
        parser.add_argument("--plot-file", dest="plot_file", type=str)
        parser.add_argument("--vcsMaxKeepGoingSplits", dest="vcs_max_keep_going_splits", type=int)
        self.args = parser.parse_args()

    def run(self):
        df = load_collection(self.args.results_collection_in)
        df["num_cpus"] = self.make_num_cpus_column(df)
        df["vcs_maxsplits"] = self.make_vcsmaxsplitscolumn_column(df)
        df["vcs_split_to_p_ratio"] = df["vcs_maxsplits"] // df["num_cpus"]
        print(df[["num_cpus", "vcs_maxsplits", "vcs_split_to_p_ratio"]].to_string())
        df = self.filter_best_vcs_config(df)
        df = self.filter_by_parallelity(df)

        self.plot(df)

    def filter_by_parallelity(self, df):
        return df[df["num_cpus"].isin([1, 2, 4, 8])]

    def filter_best_vcs_config(self, df):
        return df[(df["source"] == "more_iterations") | (df["vcs_split_to_p_ratio"] == 8)]

    def make_num_cpus_column(self, df):
        def get_num_cpus(row):
            if row["source"] == "more_iterations":
                return row["num_running_instances"]
            elif row["source"] == "parallel_vcs":
                diversification_string = row["diversification_string"]
                match = re.search("/vcsCores:(\d+)", diversification_string)
                if not match:
                    error = f"Illegal diversification string '{diversification_string}' for source='parallel_vcs'"
                    raise RuntimeError(error)
                return int(match[1])
            else:
                raise RuntimeError("Unknown source")

        return df.apply(get_num_cpus, axis="columns")

    def make_vcsmaxsplitscolumn_column(self, df):
        def get_vcsmaxsplits(row):
            if row["source"] == "more_iterations":
                return -1
            elif row["source"] == "parallel_vcs":
                diversification_string = row["diversification_string"]
                match = re.search("/vcsMaxSplits:(\d+)", diversification_string)
                if not match:
                    error = f"Illegal diversification string '{diversification_string}' for source='parallel_vcs'"
                    raise RuntimeError(error)
                return int(match[1])
            else:
                raise RuntimeError("Unknown source")

        return df.apply(get_vcsmaxsplits, axis="columns")

    def accumulate_iterations(self, df):
        group_columns = ["problem", "procedure", "num_cpus", "source"]
        return df.groupby(group_columns).agg({"runtime": "median"}).reset_index()

    def calculate_right_x_limit(self, df):
        return self.calculate_longest_total_runtime(df) * 1.05

    def calculate_longest_total_runtime(self, df):
        def sum_up_finished_runtimes(t):
            return t[t <= self.args.max_runtime].agg("sum")

        return df.groupby(["num_cpus", "source"])["runtime"].apply(sum_up_finished_runtimes).max()

    def plot(self, df):
        fig, ax = plt.subplots()
        ax.set_xlim(left=0, right=x_max)

        linestyle_by_num_cpus = {1: (0, (1, 1)), 2: (0, (2, 2)), 4: (0, (4, 4)), 8: (0, (8, 8))}
        linewidth_by_source = {"parallel_vcs": 0.8, "more_iterations": 0.5}
        color_by_source = {"parallel_vcs": "tab:blue", "more_iterations": "tab:orange"}

        for (num_cpus, source), column in runtime_chart.iteritems():
            ax.stairs(column.index, list(column) + [x_max], linestyle=linestyle_by_num_cpus[num_cpus],
                      color=color_by_source[source], alpha=1, linewidth=linewidth_by_source[source])
        if self.args.plot_file:
            fig.savefig(self.args.plot_file)


if __name__ == '__main__':
    Main().run()
