def find_vbs_results(df):
    df = df.loc[df["num_running_instances"] == 1].reset_index()
    top_config_df = df.loc[df.groupby(["problem", "procedure"])["runtime"].idxmin()]
    top_config_df.sort_values(["problem", "procedure"], ascending=True)
    return top_config_df
