def penalize(df, max_runtime=600, penalty_runtime=1200):
    penalize_overtime(df, max_runtime, penalty_runtime)
    penalize_unfinished(df, max_runtime, penalty_runtime)
    penalize_incorrect(df, max_runtime, penalty_runtime)


def penalize_overtime(df, max_runtime=600, penalty_runtime=1200):
    df["runtime"] = df.apply(lambda row: penalty_runtime if row["runtime"] > max_runtime else row["runtime"], axis=1)


def penalize_unfinished(df, max_runtime=600, penalty_runtime=1200):
    df["runtime"] = df.apply(lambda row: penalty_runtime if not row["finished"] else row["runtime"], axis=1)


def penalize_incorrect(df, max_runtime, penalty_runtime):
    df["runtime"] = df.apply(lambda row: penalty_runtime if not row["correct"] else row["runtime"], axis=1)
