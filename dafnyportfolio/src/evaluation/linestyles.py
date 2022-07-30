from matplotlib import cm
from numpy import linspace


def get_color(p):
    colormap = cm.copper
    cm_subsection = linspace(0.0, 1.0, 10)
    colors = [colormap(x) for x in cm_subsection]
    # colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    colors = ['#006ba4', '#ff800e', '#5f9ed1', '#c85200', '#ababab', '#595959', '#898989', '#a2c8ec']
    return colors[(p - 1) % len(colors)]


def get_linestyle(p):
    linestyles = [(0, (1, 0)), (0, (1, 1)), (0, (2, 2)), (0, (4, 4))]
    return linestyles[p % len(linestyles)]


def get_marker(p):
    markers = ["o", "v", "^", "*", "x", "d", "s", "P"]
    return markers[p % len(markers)]


def get_zorder(linestyle):
    (_, (fill_size, gap_size)) = linestyle
    period = gap_size + fill_size if gap_size > 0 else 9999
    return 1 / period


vbs_color = "tab:grey"
vbs_marker = ""
