import os
from os.path import basename
import argparse
import matplotlib.pyplot as plt
from matplotlib import rcParams
from slugify import slugify
from collect import *


def save_plot(boxplot, filename):
    try:
        os.makedirs(os.path.dirname(filename))
    except FileExistsError:
        pass
    boxplot.get_figure().savefig(filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Plot boxplots displaying runtime")
    parser.add_argument(metavar="RESULTFILE", dest="result_filenames", type=str, nargs="+")
    parser.add_argument("--suffix", "-s", dest="out_file_suffix", type=str, nargs="?", default="")
    args = parser.parse_args()

    df = collect_runtimes(args.result_filenames)

    rcParams.update({'figure.autolayout': True})

    for (problem, procedure, is_portfolio), group in df.groupby(["problem", "procedure", "is_portfolio"]):
        y_max = group["runtime"].max()
        group = group.pivot(columns=["option_selector", "num_instances", "only_instances"], index="seed",
                            values="runtime").reset_index()
        boxplot = group.plot(kind="box", ylim=(0, y_max * 1.1))

        plt.setp(boxplot.xaxis.get_majorticklabels(), rotation=90)

        cmp_string = "compare_portfolios" if is_portfolio else "compare_instances"
        filename = "{}/{}_{}{}.svg".format(cmp_string, slugify(problem), slugify(procedure), args.out_file_suffix)
        save_plot(boxplot, filename)
