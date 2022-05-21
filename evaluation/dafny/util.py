import os


def save_plot(boxplot, filename):
    ensure_surrounding_directory_exists(filename)
    boxplot.get_figure().savefig(filename)


def ensure_surrounding_directory_exists(filename):
    try:
        os.makedirs(os.path.dirname(filename))
    except FileExistsError:
        pass


def make_matrix(df):
    df = df.copy()
    df = df[df["num_running_instances"] == 1]
    df["configuration"] = df[("diversification", 0)]
    df["score"] = df["runtime"]
    df = df[["configuration", "problem", "procedure", "score"]]
    df = df.groupby(["configuration", "problem", "procedure"], as_index=False).agg("mean")
    df = df.pivot(index=["problem", "procedure"], columns="configuration", values="score")
    df["[vbs]"] = df.min(axis=1)
    df.loc["[total]"] = df.sum()
    return df


