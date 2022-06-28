import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn

from collect import *
from collection_persistence import load_collection
from util import *


def plot_as_heatmap(filename, relative_df, max_value, title):
    rcParams.update({'figure.autolayout': True})
    relative_heatmap = plot(relative_df, title, max_value)
    save_plot(relative_heatmap, filename)
    plt.close()


def plot(relative_df, title, vmax):
    plotted_df = relative_df.drop("[total]")
    plotted_df = plotted_df.drop("[vbs]", axis=1)
    plotted_df.index = range(len(plotted_df.index))
    plotted_df.columns = range(len(plotted_df.columns))
    colormap = seaborn.color_palette("dark:salmon_r", as_cmap=True)
    fig, ax = plt.subplots(figsize=(len(plotted_df.columns) / 10, len(plotted_df.index) / 10))
    heatmap = seaborn.heatmap(plotted_df, vmin=0, vmax=vmax, cmap=colormap, cbar_kws={"shrink": 0.8}, square=True,
                              ax=ax)
    heatmap.set_title(title)
    heatmap.set_xlabel("Configuration")
    heatmap.set_ylabel("Benchmark")
    return heatmap


def plot_heatmap_with_absolute_runtimes(df, filename, max_value):
    plot_as_heatmap(filename, df, max_value, "Runtime in Seconds")


def plot_heatmap_with_runtime_differences(filename, df, max_value):
    relative_matrix = df.apply(lambda row: row - row.min(), axis=1)
    plot_as_heatmap(filename, relative_matrix, max_value, "Runtime Difference to VBS in Seconds")


def main():
    parser = argparse.ArgumentParser(description="Plot matrix displaying runtime")
    parser.add_argument(metavar="COLLECTION", dest="results_collection", type=str)
    parser.add_argument(metavar="OUTFILE", dest="output_file", type=str)
    parser.add_argument("--plot-differences", dest="plot_differences", action='store_true')
    parser.add_argument("--max-value", dest="max_value", type=float)
    args = parser.parse_args()

    df = load_collection(args.results_collection)

    if args.plot_differences:
        plot_heatmap_with_runtime_differences(args.output_file, df, args.max_value)
    else:
        plot_heatmap_with_absolute_runtimes(df, args.output_file, args.max_value)


if __name__ == '__main__':
    main()
