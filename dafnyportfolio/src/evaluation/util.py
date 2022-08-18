import os


def save_plot(boxplot, filename):
    ensure_surrounding_directory_exists(filename)
    boxplot.get_figure().savefig(filename)


def ensure_surrounding_directory_exists(filename):
    try:
        os.makedirs(os.path.dirname(filename))
    except FileExistsError:
        pass


def make_matrix(df, agg="median"):
    df = df.copy()
    df["configuration"] = df["diversification_string"]
    df["score"] = df["runtime"]
    df = df[["configuration", "num_running_instances", "problem", "procedure", "score"]]
    df = df.groupby(["configuration", "num_running_instances", "problem", "procedure"], as_index=False).agg(agg)
    df = df.pivot(index=["problem", "procedure"], columns=["configuration", "num_running_instances"], values="score")
    df["[vbs]"] = df.min(axis=1)
    df.loc["[total]"] = df.sum()
    return df
