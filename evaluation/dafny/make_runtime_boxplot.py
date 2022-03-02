from os.path import basename
import argparse
import matplotlib.pyplot as plt
from slugify import slugify
from collect import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Plot boxplots displaying runtime")
    parser.add_argument(metavar="RESULTFILE", dest="result_filenames", type=str, nargs="+")
    parser.add_argument("--suffix", "-s", dest="out_file_suffix", type=str, nargs="?", default="")
    args = parser.parse_args()

    df = collect_runtimes(args.result_filenames)

    for (problem, procedure), group in df.groupby(["problem", "procedure"]):
        y_max = group["runtime"].max()
        group = group.pivot(columns=["option_selector", "num_threads"], index="seed", values="runtime").reset_index()
        boxplot = group.plot(kind="box", ylim=(0, y_max * 1.1))
        boxplot.get_figure().savefig("{}_{}{}.svg".format(slugify(problem), slugify(procedure), args.out_file_suffix))
