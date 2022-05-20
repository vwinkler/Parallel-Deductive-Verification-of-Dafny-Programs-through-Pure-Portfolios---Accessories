from dataclasses import dataclass


@dataclass(frozen=True)
class CellReference:
    row_index: int
    column_index: int
    row_name: str
    column_name: str


def find_empty_cells(df):
    result = []
    error_matrix = df.isnull()
    for row_index, row in enumerate(error_matrix.to_numpy()):
        for col_index, cell in enumerate(row):
            if cell:
                result.append(make_cell_reference(df, row_index, col_index))
    return result


def make_cell_reference(df, row_index, col_index):
    return CellReference(row_index=row_index, column_index=col_index, row_name=df.index[row_index],
                         column_name=df.columns[col_index])
