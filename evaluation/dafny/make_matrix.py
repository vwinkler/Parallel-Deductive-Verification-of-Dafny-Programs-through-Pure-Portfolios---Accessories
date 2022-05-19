import sys
import argparse
import matplotlib.pyplot as plt
from matplotlib import rcParams
from collect import *
from penalize_runtimes import *
from util import save_plot, ensure_surrounding_directory_exists
import seaborn


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Plot matrix displaying runtime")
    parser.add_argument(metavar="COLLECTION", dest="results_collection", type=str)
    parser.add_argument("--target-dir", dest="target_dir", type=str, default=".")
    args = parser.parse_args()

    store = pd.HDFStore(args.results_collection)
    df = store['df']
    store.close()

    penalize(df)

    df = df[df["num_running_instances"] == 1]
    df["configuration"] = df[("diversification", 0)]
    df["score"] = df["runtime"]
    df = df[["configuration", "problem", "procedure", "score"]]
    df = df.groupby(["configuration", "problem", "procedure"], as_index=False).agg("mean")
    df = df.pivot(index=["problem", "procedure"], columns="configuration", values="score")
    df["[vbs]"] = df.min(axis=1)
    df.loc["[total]"] = df.sum()
    relative_df = df.apply(lambda row: row - row.min(), axis=1)

    rcParams.update({'figure.autolayout': True})
    basename = f"{args.target_dir}/01"
    print(f"{basename}.svg")
    ensure_surrounding_directory_exists(basename)
    with open(f"{basename}.txt", "w") as f:
        f.write("\n".join([f"{k}\t{r}" for k, r in enumerate(df.index)]))
        f.write("\n\n")
        f.write("\n".join([f"{k}\t{c}" for k, c in enumerate(df.columns)]))
    heatmap = plot(df, "Runtime in Seconds", 1200)
    save_plot(heatmap, f"{basename}.svg")
    plt.close()
    relative_heatmap = plot(relative_df, "Runtime Difference to VBS in Seconds", 10)
    save_plot(relative_heatmap, f"{basename}_relative.svg")
    plt.close()

    with open(f"{basename}.html", "w") as f:
        df.to_html(f)

    with open(f"{basename}.ods", "wb") as f:
        try:
            df.to_excel(f, engine="odf")
        except ModuleNotFoundError as e:
            print(f"Could not save as '{f.name}': {e}")
