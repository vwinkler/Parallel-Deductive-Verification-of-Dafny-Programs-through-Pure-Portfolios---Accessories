import matplotlib.pyplot as plt
from matplotlib import rcParams
from collect import *
from collection_persistence import load_collection
from finding_empty_matrix_cells import find_empty_cells
from runtime_penalization import *
from util import *
import seaborn


def warn_about_empty_cells(df):
    for cell in sorted(find_empty_cells(df), key=lambda cell: cell.row_index):
        warn_about_empty_cell(cell)


def warn_about_empty_cell(cell):
    index = cell.column_index
    configuration = cell.column_name
    (benchmark_file, benchmark_method) = cell.row_name
    print((f"Runtime for {benchmark_file} {benchmark_method} (row {cell.row_index}) "
           f"with {configuration} (column {index}) "
           f"is empty"))


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


def export_to_html(filename, df):
    with open(filename, "w") as f:
        df.to_html(f)


def export_to_ods(filename, df):
    with open(filename, "wb") as f:
        try:
            df.to_excel(f, engine="odf")
        except ModuleNotFoundError as e:
            print(f"Could not save as '{f.name}': {e}")


def export_axis_labels(filename, df):
    ensure_surrounding_directory_exists(filename)
    with open(filename, "w") as f:
        f.write("\n".join([f"{k}\t{r}" for k, r in enumerate(df.index)]))
        f.write("\n\n")
        f.write("\n".join([f"{k}\t{c}" for k, c in enumerate(df.columns)]))


def plot_as_heatmap(filename, relative_df, max_value, title):
    rcParams.update({'figure.autolayout': True})
    relative_heatmap = plot(relative_df, title, max_value)
    save_plot(relative_heatmap, filename)
    plt.close()


def main():
    parser = argparse.ArgumentParser(description="Plot matrix displaying runtime")
    parser.add_argument(metavar="COLLECTION", dest="results_collection", type=str)
    parser.add_argument("--target-dir", dest="target_dir", type=str, default=".")
    args = parser.parse_args()

    df = load_collection(args.results_collection)
    penalize_results_table(df)
    df = make_matrix(df)
    warn_about_empty_cells(df)
    penalize_runtime_matrix(df)

    relative_matrix = df.apply(lambda row: row - row.min(), axis=1)

    basename = f"{args.target_dir}/01"

    print(f"{basename}.svg")

    export_axis_labels(f"{basename}.txt", df)
    plot_as_heatmap(f"{basename}.svg", df, 1200, "Runtime in Seconds")
    plot_as_heatmap(f"{basename}_relative.svg", relative_matrix, 10, "Runtime Difference to VBS in Seconds")

    export_to_html(f"{basename}.html", df)
    export_to_ods(f"{basename}.ods", df)


if __name__ == '__main__':
    main()
