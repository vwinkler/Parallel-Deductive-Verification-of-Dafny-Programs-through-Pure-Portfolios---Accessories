import argparse

from collection_persistence import load_collection
from finding_empty_matrix_cells import find_empty_cells


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
    parser.add_argument(metavar="COLLECTION_IN", dest="matrix_in", type=str)
    args = parser.parse_args()

    df = load_collection(args.matrix_in)
    warn_about_empty_cells(df)


if __name__ == '__main__':
    main()
