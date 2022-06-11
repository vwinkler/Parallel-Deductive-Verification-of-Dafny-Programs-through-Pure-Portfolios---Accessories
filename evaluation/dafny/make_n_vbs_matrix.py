import argparse

import pandas as pd

from collection_persistence import load_collection, store_collection


def select_single_configuration_runs(runtime_matrix):
    df = runtime_matrix.iloc[:, runtime_matrix.columns.get_level_values(1) == 1]
    return df.droplevel(1, axis="columns")


def append_additional_info(n_vbs_cascading_runtime_matrix):
    append_total_cascading_runtime(n_vbs_cascading_runtime_matrix)
    append_portfolio_size(n_vbs_cascading_runtime_matrix)
    add_index_to_column_names(n_vbs_cascading_runtime_matrix)


def calculate_n_vbs_cascading_runtime_matrix(args, runtime_matrix):
    n_vbs_config_runtime_matrix = gather_n_vbs_configuration_runtime_matrix(runtime_matrix, args.max_n)
    n_vbs_cascading_runtime_matrix = cascade_runtimes(n_vbs_config_runtime_matrix)
    return n_vbs_cascading_runtime_matrix


def make_pure_runtime_matrix(df):
    df = df.drop("[vbs]", axis=1)
    df = df.drop("[total]")
    return df


def gather_n_vbs_configuration_runtime_matrix(df, max_num_configurations):
    vbs_matrix = make_0_vbs(df)
    for n in range(1, max_num_configurations + 1):
        vbs_matrix = append_best_configuration(df, vbs_matrix)
    return vbs_matrix


def make_0_vbs(df):
    return pd.DataFrame(index=df.index)


def append_best_configuration(runtime_matrix, vbs_matrix):
    best_additional_configuration_index = find_best_additional_configuration_index(runtime_matrix, vbs_matrix)
    best_additional_configuration_column = runtime_matrix.loc[:, best_additional_configuration_index]
    vbs_matrix = pd.concat([vbs_matrix, best_additional_configuration_column], axis=1)
    return vbs_matrix


def find_best_additional_configuration_index(df, current_vbs):
    new_vbs_options = {col_index: pd.concat([current_vbs, column], axis=1) for col_index, column in df.items()}
    return min(new_vbs_options, key=lambda col_index: calc_vbs_runtime(new_vbs_options[col_index]))


def calc_vbs_runtime(df):
    return df.min(axis=1).sum()


def cascade_runtimes(n_vbs_config_runtime_matrix):
    return n_vbs_config_runtime_matrix.cummin(axis=1)


def append_total_cascading_runtime(cascading_runtime_matrix):
    cascading_runtime_matrix.loc["[total]", :] = cascading_runtime_matrix.sum(axis=0)


def append_portfolio_size(cascading_runtime_matrix):
    cascading_runtime_matrix.loc["[portfolio_size]", :] = range(1, len(cascading_runtime_matrix.columns) + 1)


def add_index_to_column_names(cascading_runtime_matrix):
    column_names = [cascading_runtime_matrix.columns, range(1, len(cascading_runtime_matrix.columns) + 1)]
    cascading_runtime_matrix.columns = pd.MultiIndex.from_arrays(column_names)


def main():
    parser = argparse.ArgumentParser(description="Find n-VBS from p=1 runtime data using greedy heuristic")
    parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
    parser.add_argument(metavar="COLLECTION_OUT", dest="results_collection_out", type=str)
    parser.add_argument(metavar="MAX-N", dest="max_n", type=int)
    args = parser.parse_args()

    runtime_matrix = load_collection(args.results_collection_in)
    runtime_matrix = make_pure_runtime_matrix(runtime_matrix)
    runtime_matrix = select_single_configuration_runs(runtime_matrix)
    n_vbs_cascading_runtime_matrix = calculate_n_vbs_cascading_runtime_matrix(args, runtime_matrix)
    append_additional_info(n_vbs_cascading_runtime_matrix)

    store_collection(args.results_collection_out, n_vbs_cascading_runtime_matrix)


if __name__ == '__main__':
    main()
