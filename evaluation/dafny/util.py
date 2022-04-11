import os


def save_plot(boxplot, filename):
    ensure_surrounding_directory_exists(filename)
    boxplot.get_figure().savefig(filename)


def ensure_surrounding_directory_exists(filename):
    try:
        os.makedirs(os.path.dirname(filename))
    except FileExistsError:
        pass