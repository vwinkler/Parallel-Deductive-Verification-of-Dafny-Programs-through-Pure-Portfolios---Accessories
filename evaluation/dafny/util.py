import os


def save_plot(boxplot, filename):
    try:
        os.makedirs(os.path.dirname(filename))
    except FileExistsError:
        pass
    boxplot.get_figure().savefig(filename)