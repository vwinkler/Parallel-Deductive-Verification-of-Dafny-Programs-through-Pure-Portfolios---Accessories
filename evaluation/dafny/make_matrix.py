import argparse

from collection_persistence import load_collection, store_collection
from finding_empty_matrix_cells import find_empty_cells
from runtime_penalization import penalize_runtime_matrix
from util import make_matrix


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


def main():
    parser = argparse.ArgumentParser(description="Penalize results")
    parser.add_argument(metavar="COLLECTION_IN", dest="results_collection_in", type=str)
    parser.add_argument(metavar="COLLECTION_OUT", dest="results_collection_out", type=str)
    parser.add_argument("--supress-empty-cell-warnings", dest="supress_empty_cell_warnings", action='store_true')
    parser.add_argument("--penalty-runtime", dest="penalty_runtime", type=float, default=1200)
    args = parser.parse_args()

    df = load_collection(args.results_collection_in)
    df = make_matrix(df)
    if not args.supress_empty_cell_warnings:
        warn_about_empty_cells(df)
    penalize_runtime_matrix(df, penalty_runtime=args.penalty_runtime)
    store_collection(args.results_collection_out, df)


if __name__ == '__main__':
    main()
