import argparse

import seaborn as sns
from matplotlib import pyplot as plt

from collection_persistence import load_collection


class Main:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Make speedup plot with best configurations")
        parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
        parser.add_argument("--errorbars", dest="plot_errorbars", action='store_true')
        parser.add_argument("--plot-file", dest="plot_file", type=str)
        self.args = parser.parse_args()

    def run(self):
        df = load_collection(self.args.results_collection_in)
        df_mean_runtime = self.accumulate_iterations(df)
        df_min_mean_total_runtime = self.pick_best_configurations_per_cpu_count_and_problem(df_mean_runtime)

        self.plot(self.args.plot_file, df_min_mean_total_runtime)

    def accumulate_iterations(self, df):
        return df.groupby(["problem", "procedure", "diversification_string", "num_running_instances"]).agg(
            runtime=("runtime", "median"), runtime_std=("runtime", "std")).reset_index()

    def pick_best_configurations_per_cpu_count_and_problem(self, df_total_mean_runtime):
        columns = ["problem", "procedure", "num_running_instances"]
        return df_total_mean_runtime.loc[df_total_mean_runtime.groupby(columns)["runtime"].idxmin()]

    def plot(self, filename, df):
        plt.rcParams.update({"text.usetex": True})

        fig, ax = plt.subplots()

        for (problem, procedure), group in df.groupby(["problem", "procedure"]):
            underscore_replacement = '\\_'
            dollar_replacement = '\\$'
            label = f"{problem}, {procedure.replace('_', underscore_replacement).replace('$', dollar_replacement)}"
            if self.args.plot_errorbars:
                ax.errorbar(group["num_running_instances"], group["runtime"], yerr=group["runtime_std"], label=label)
            else:
                ax.plot(group["num_running_instances"], group["runtime"], label=label)

        figure = ax.get_figure()
        ax.set_ylim(bottom=0)
        ax.legend(loc="lower right")
        if self.args.plot_file:
            figure.savefig(filename)
        else:
            plt.show()


if __name__ == '__main__':
    Main().run()
