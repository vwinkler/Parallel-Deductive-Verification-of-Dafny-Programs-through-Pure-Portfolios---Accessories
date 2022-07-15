import itertools


def find_vbs_results(df):
    df = df.loc[df["num_running_instances"] == 1].reset_index()
    top_config_df = df.loc[df.groupby(["problem", "procedure"])["runtime"].idxmin()]
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

# combine them to all combinations of n
# for each combination get the theoretical runtime from df
# return best combination
