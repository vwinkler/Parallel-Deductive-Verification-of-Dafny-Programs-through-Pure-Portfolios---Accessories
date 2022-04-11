import argparse
import matplotlib.pyplot as plt
from matplotlib import rcParams
from collect import *
from util import save_plot, ensure_surrounding_directory_exists

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Plot matrix displaying runtime")
    parser.add_argument(metavar="RESULTFILE", dest="result_filenames", type=str, nargs="+")
    args = parser.parse_args()

    df = collect_runtimes(args.result_filenames)
    df = df[df["num_running_instances"] == 1]
    df["configuration"] = df[("diversification", 0)]
    df["score"] = df["runtime"]
    df = df[["configuration", "problem", "procedure", "score"]]
    df = df.groupby(["configuration", "problem", "procedure"], as_index=False).agg("mean")
    df = df.pivot(index=["problem", "procedure"], columns="configuration", values="score")
    df.loc["[total]"] = df.sum()

    rcParams.update({'figure.autolayout': True})
    basename = "matrix/01"
    print(f"{basename}.svg")
    ensure_surrounding_directory_exists(basename)
    with open(f"{basename}.txt", "w") as f:
        f.write("\n".join([f"{k}\t{r}" for k, r in enumerate(df.index)]))
        f.write("\n\n")
        f.write("\n".join([f"{k}\t{c}" for k, c in enumerate(df.columns)]))
    save_plot(plt.matshow(df.drop("[total]")), "matrix/01.svg")
    plt.close()

    with open(f"{basename}.html", "w") as f:
        df.to_html(f)

    with open(f"{basename}.ods", "wb") as f:
        try:
            df.to_excel(f, engine="odf")
        except ModuleNotFoundError as e:
            print(f"Could not save as '{f.name}': {e}")
