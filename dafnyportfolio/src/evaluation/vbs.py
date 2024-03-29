import itertools


def find_vbs_results(df):
    df = df.loc[df["num_running_instances"] == 1].reset_index()
    group_columns = ["problem", "procedure", "num_running_instances", "diversification_string"]
    df_agg = df.groupby(group_columns).agg({"runtime": "median"}).reset_index()
    top_config_df = df_agg.loc[df_agg.groupby(["problem", "procedure"])["runtime"].idxmin()]
    top_config_df.sort_values(["problem", "procedure"], ascending=True)
    return top_config_df


def find_n_vbs_results(df, n):
    possible_configs = find_vbs_results(df)["diversification_string"].unique()

    df = df.loc[df["diversification_string"].isin(possible_configs)]

    total_time_by_portfolio = dict()
    for n_portfolio in itertools.combinations(possible_configs, n):
        reduced_df = df.loc[df["diversification_string"].isin(n_portfolio)]
        total_time_by_portfolio[n_portfolio] = reduced_df.groupby(["problem", "procedure"])["runtime"].min().sum()

    best_config = min(total_time_by_portfolio, key=total_time_by_portfolio.get)
    return find_vbs_results(df.loc[df["diversification_string"].isin(best_config)])
