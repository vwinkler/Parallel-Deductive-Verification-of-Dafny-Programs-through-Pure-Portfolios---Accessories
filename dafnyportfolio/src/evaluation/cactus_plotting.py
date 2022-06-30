import pandas as pd


def make_sorted_runtime_chart(df, configuration_columns):
    df = df.sort_values(by="runtime", ignore_index=True, ascending=True)
    runtimes_by_diversification = {div_string: runtimes.reset_index(drop=True) for div_string, runtimes in
                                   df.groupby(configuration_columns)["runtime"]}
    new_df = pd.DataFrame(runtimes_by_diversification)
    return new_df


def fill_mising_results(df, x_max):
    return df.fillna(x_max)


def calculate_prefix_sums(new_df):
    return new_df.cumsum(axis="index")


def prepare_for_inverted_cactus(df, x_max, configuration_columns):
    runtime_chart = make_sorted_runtime_chart(df, configuration_columns)
    runtime_chart = fill_mising_results(runtime_chart, x_max)
    runtime_chart = calculate_prefix_sums(runtime_chart)
    return runtime_chart
