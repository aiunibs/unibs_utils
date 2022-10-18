import matplotlib.pyplot as plt
import numpy as np
from utils_unibs.constants import C
import warnings


class _CharSize:
    """
    Class for handling the character sizes

    Attributes:
        small_size: the value of the small size characters
        medium_size: the value of the medium size characters
        big_size: the value of the bigger size characters
    """

    _SMALL_SIZE = 10
    _MEDIUM_SIZE = 15
    _BIGGER_SIZE = 20

    _instance = None

    def __new__(cls):
        """
        Implementation of the Singleton Pattern
        """
        if cls._instance is None:
            cls._instance = super(_CharSize, cls).__new__(cls)
        return cls._instance

    @property
    def small_size(self):
        """
        small_size attribute getter

        Returns: an int containing the value of the small size
        """
        return self._SMALL_SIZE

    @small_size.setter
    def small_size(self, value: int):
        """
        small_size attribute setter

        Args:
            value: an int containing the new small size value

        Raises:
            ValueError: an error on the value
        """
        if value >= self._MEDIUM_SIZE or value < 1:
            raise ValueError
        self._SMALL_SIZE = value

    @property
    def medium_size(self):
        """
        medium_size attribute getter

        Returns: an int containing the value of the medium size
        """
        return self._MEDIUM_SIZE

    @medium_size.setter
    def medium_size(self, value: int):
        """
        medium_size attribute setter

        Args:
            value: an int containing the new medium size value

        Raises:
            ValueError: an error on the value
        """
        if value >= self._BIGGER_SIZE or value <= self._SMALL_SIZE:
            raise ValueError
        self._MEDIUM_SIZE = value

    @property
    def big_size(self):
        """
        big_size attribute getter

        Returns: an int containing the value of the bigger size
        """
        return self._BIGGER_SIZE

    @big_size.setter
    def big_size(self, value: int):
        """
        big_size attribute setter

        Args:
            value: an int containing the new bigger size value

        Raises:
            ValueError: an error on the value
        """
        if value <= self._MEDIUM_SIZE:
            raise ValueError
        self._BIGGER_SIZE = value


CS = _CharSize()


def set_size(size: str, value: int):
    """
    Set a new size value
    Args:
        size: string containing the target size to change {'small', 'medium', 'big'}
        value: the new value for the target size

    Returns:
        True if the new value is set correctly, False otherwise
    """

    if type(size) == str:
        size = size.lower().strip()

    try:
        value = int(value)
    except ValueError:
        print(C.VALUE_ERROR_MSG)
        return False
    if size == C.SMALL:
        try:
            CS.small_size = value
            update_dimensions()
            return True
        except ValueError:
            print(C.SMALL_ERROR_MSG.format(CS.medium_size))
    elif size == C.MEDIUM:
        try:
            CS.medium_size = value
            update_dimensions()
            return True
        except ValueError:
            print(C.MEDIUM_ERROR_MSG.format(CS.small_size, CS.big_size))
    elif size == C.BIG:
        try:
            CS.big_size = value
            update_dimensions()
            return True
        except ValueError:
            print(C.BIG_ERROR_MSG.format(CS.medium_size))
    else:
        print(C.SIZE_ERROR_MSG)
    return False


DIMENSIONS = {
    C.FONT: C.SMALL,
    C.AXES_TITLE: C.BIG,
    C.AXES_LABEL: C.MEDIUM,
    C.XTICK: C.MEDIUM,
    C.YTICK: C.MEDIUM,
    C.LEGEND_FONT: C.MEDIUM,
    C.LEGEND_TITLE: C.MEDIUM,
    C.TITLE: C.BIG,
    C.LATEX: "false",
}


def update_dimensions():
    """
    Update all dimensions in DIMENSIONS
    """
    for k in DIMENSIONS:
        _update_dimension(k, DIMENSIONS[k])


def _update_dimension(dimension: str, size: str):
    """
    Updates the value of a single parameter to a different size

    Args:
        dimension: string containing the target parameter {'font', 'axes title', 'axes label', 'xtick', 'ytick',
                   'legend font', 'legend title', 'title', 'latex'}
        size: string containing the target size to change {'small', 'medium', 'big'}

    Returns:
        True if the size was updated correctly, False otherwise
    """

    if type(dimension) == str:
        dimension = dimension.lower().strip()

    if type(size) == str:
        size = size.lower().strip()

    try:
        if dimension == C.FONT:
            plt.rc("font", size=get_size(size))  # controls default text sizes
        elif dimension == C.AXES_TITLE:
            plt.rc("axes", titlesize=get_size(size))  # fontsize of the axes title
        elif dimension == C.AXES_LABEL:
            plt.rc("axes", labelsize=get_size(size))  # fontsize of the x and y labels
        elif dimension == C.XTICK:
            plt.rc("xtick", labelsize=get_size(size))  # fontsize of the tick labels
        elif dimension == C.YTICK:
            plt.rc("ytick", labelsize=get_size(size))  # fontsize of the tick labels
        elif dimension == C.LEGEND_FONT:
            plt.rc("legend", fontsize=get_size(size))  # legend fontsize
        elif dimension == C.LEGEND_TITLE:
            plt.rc("legend", title_fontsize=get_size(size))  # fontsize of legend title
        elif dimension == C.TITLE:
            plt.rc("figure", titlesize=get_size(size))  # fontsize of the figure title
        elif dimension == C.LATEX:
            if size == "true":
                plt.rcParams["text.usetex"] = True
            elif size == "false":
                plt.rcParams["text.usetex"] = False
            else:
                raise ValueError
        else:
            print(C.DIMENSIONS_ERROR_MSG.format(f"{[k for k in DIMENSIONS]}"))
            return False
    except ValueError:
        print(C.SIZE_LATEX_ERROR_MSG)
        return False

    return True


def set_dimension(dimension: str, value: str):
    """
    Set the a character size for a parameter
    Args:
        dimension: string containing the target parameter {'font', 'axes title', 'axes label', 'xtick', 'ytick',
                   'legend font', 'legend title', 'title', 'latex'}
        value: string containing the target size to change {'small', 'medium', 'big'}

    Returns:
        True is the parameter is set correctly, False otherwise
    """
    if dimension in DIMENSIONS.keys():
        if _update_dimension(dimension, value):
            DIMENSIONS[dimension] = value
            return True

    return False


def get_size(size: str):
    """
    Returns the current value for a given size

    Args:
        size: string containing the target size {'small', 'medium', 'big'}

    Returns:
        An integer containing the value of the given size
    """
    if type(size) == str:
        size = size.lower().strip()

    if size == C.SMALL:
        return CS.small_size
    elif size == C.MEDIUM:
        return CS.medium_size
    elif size == C.BIG:
        return CS.big_size
    else:
        raise ValueError


def _get_label(labels: list, index: int):
    """
    Returns the label for a given index
    Args:
        labels: a list containing the labels. Can be None.
        index: an integer containing the position of the label in the list

    Returns:
        The label at a given position in the list if the list is not None, None otherwise
    """
    if labels is None:
        return None
    else:
        try:
            label = labels[index]
        except IndexError:
            label = None
    return label


def _line_plot(
    dataset: np.ndarray,
    x: np.ndarray,
    fig: plt.Figure,
    ax: plt.Axes,
    labels: list,
    styles: list,
    markers: list,
    colors: list,
):
    """
    Plots all the lines in the dataset

    Args:
        dataset: a ndarray containing the data to plot
        x: a ndarray containing the x axis labels
        fig: the Figure where to plot
        ax: the Axes where to plot
        labels: a list containing the labels for the dataset
        styles: a list containing pyplot styles
        markers: a list containing pyplot markers
        colors: a list containing pyplot colors

    Returns:
        A tuple that contains the plotted figure and axis
    """
    for l, line in enumerate(dataset):
        label = _get_label(labels, l)
        try:
            color = colors[l]
        except IndexError:
            w = C.WARNING_MSG.format(f"colors[{l}]", f"{C.DEFAULT_COLOR}")
            warnings.warn(w)
            color = C.DEFAULT_COLOR
        try:
            marker = markers[l]
        except IndexError:
            w = C.WARNING_MSG.format(f"markers[{l}]", f"{C.DEFAULT_MARKER}")
            warnings.warn(w)
            marker = C.DEFAULT_MARKER
        try:
            style = styles[l]
        except IndexError:
            w = C.WARNING_MSG.format(f"style[{l}]", f"{C.DEFAULT_STYLE}")
            warnings.warn(w)
            style = C.DEFAULT_STYLE

        ax.plot(
            x,
            line,
            color=color,
            marker=marker,
            linestyle=style,
            label=label,
        )
    return fig, ax


def _set_axis_ticks(ax: plt.Axes, ticks: list, labels: list, axis: str):
    """
    Set the ticks and labels for a given axis

    Args:
        ax (plt.Axes): the axis where to set the ticks
        ticks (list): a list containing the ticks
        labels (list): a list containing the labels
        axis (str): the axis where to set the ticks ('y' or 'x')

    Returns:
        The axis with the ticks and labels set
    """
    if axis == C.X:
        set_axis = ax.set_xticks
    elif axis == C.Y:
        set_axis = ax.set_yticks
    else:
        return None
    
    if labels is None:
        set_axis(ticks)
    elif len(labels) != len(ticks):
        warnings.warn(C.TICKS_WARNING_MSG.format(axis))
        set_axis(ticks)
    else:
        set_axis(ticks, labels)

    return ax


def get_line_plot(
    dataset: list,
    xticks: list = [],
    xticks_labels: list = None,
    yticks: list = [],
    yticks_labels: list = None,
    labels: list = None,
    xlabel: str = None,
    ylabel: str = None,
    legend_title: str = None,
    title: str = None,
    save_fig: str = None,
    styles: list = C.STYLES,
    colors: list = C.COLORS,
    markers: list = C.MARKERS,
):
    """
    Returns a line plot of the dataset

    Args:
        dataset: a ndarray containing the data to plot divided by rows
        xticks:  a ndarray of integers containing the X axis ticks positions; default is None
        xticks_labels: a list of X axis labels, default is None
        yticks: a ndarray of integers containing the Y axis ticks positions; default is None
        yticks_labels: a list of Y axis labels, default is None
        labels: a list containing the labels for the dataset
        xlabel: a string containing the label of the X axis; default is None
        ylabel: a string containing the label of the Y axis; default is None
        legend_title: a string containing the legend title; default is None
        title: a string containing the figure title; default is None
        save_fig: a string containing the path where to save the figure; default is None. If None the figure will
                  not be saved
        styles: a list containing pyplot styles
        markers: a list containing pyplot markers
        colors: a list containing pyplot colors

    Returns:
        A tuple that contains the plotted figure and axis

    """

    dataset = np.asanyarray(dataset)
    if xticks is None:
        xticks = []
    if yticks is None:
        yticks = []
    fig, ax = plt.subplots(facecolor='w')
    if len(dataset.shape) == 2:
        x_axis = range(dataset.shape[1])
        fig, ax = _line_plot(dataset, x_axis, fig, ax, labels, styles, markers, colors)

        ax = _set_axis_ticks(ax, xticks, xticks_labels, C.X)
        ax = _set_axis_ticks(ax, yticks, yticks_labels, C.Y)

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        if labels is not None:
            fig.legend(
                bbox_to_anchor=(0.95, 0.5), loc="center left", title=legend_title
            )
        if save_fig is not None:
            if not save_fig.endswith(".png"):
                save_fig += ".png"
            plt.savefig(save_fig, bbox_inches="tight")
        plt.show()
        plt.close(fig)

    else:
        print(C.DATASET_ERROR_MSG)
    return fig, ax


def get_hist_plot(
        dataset: list,
        xticks: list = None,
        xticks_labels: list = None,
        yticks: list = None,
        yticks_labels: list = None,
        labels: list = None,
        xlabel: str = None,
        ylabel: str = None,
        legend_title: str = None,
        title: str = None,
        save_fig: str = None,
        eps1: float = 0.1,
        eps2: float = 0.1,
        colors: list = C.COLORS,
):
    """
    Returns a bar plot of the dataset

    Args:
        dataset: a ndarray containing the data to plot
        xticks:  a ndarray of integers containing the X axis ticks positions; default is None
        xticks_labels: a list of X axis labels, default is None
        labels: a list containing the labels for the dataset
        xlabel: a string containing the label of the X axis; default is None
        ylabel: a string containing the label of the Y axis; default is None
        legend_title: a string containing the legend title; default is None
        title: a string containing the figure title; default is None
        save_fig: a string containing the path where to save the figure; default is None. If None the figure will
                  not be saved
        eps1: a float that represents the space between the columns in different ticks. Must be between 0 and 0.1
        eps2: a float that represents the space between the columns in the same tick. Must be between 0 and 0.1
        colors: a list containing pyplot colors

    Returns:
        A tuple that contains the plotted figure and axis
    """

    dataset = np.asanyarray(dataset)
    if xticks is None:
        xticks = []
    if yticks is None:
        yticks = []

    if eps1 < 0:
        eps1 = 0
    elif eps1 > 0.1:
        eps1 = 0.1
    if eps2 < 0:
        eps2 = 0
    elif eps2 > 0.1:
        eps2 = 0.1

    fig, ax = plt.subplots(facecolor='w')
    if len(dataset.shape) == 2:
        w = (1 - (2 * eps1)) / dataset.shape[0]
        for i in range(dataset.shape[0]):
            for j in range(dataset.shape[1]):
                try:
                    if j == 0 and labels is not None:
                        mylabel = labels[i]
                    else:
                        raise IndexError
                except IndexError:
                    mylabel = None
                try:
                    color = colors[i]
                except IndexError:
                    w_msg = C.WARNING_MSG.format(f"colors[{i}]", C.DEFAULT_COLOR)
                    warnings.warn(w_msg)
                    color = C.DEFAULT_COLOR
                ax.bar(
                    j - 0.5 + eps1 + w / 2 + i * w,
                    dataset[i][j],
                    color=color,
                    width=w - eps2,
                    label=mylabel,
                )
        
        ax = _set_axis_ticks(ax, xticks, xticks_labels, C.X)
        ax = _set_axis_ticks(ax, yticks, yticks_labels, C.Y)

        if labels is not None:
            fig.legend(bbox_to_anchor=(0.95, 0.5), loc="center left", title=legend_title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        if save_fig is not None:
            if not save_fig.endswith(".png"):
                save_fig += ".png"
            plt.savefig(save_fig, bbox_inches="tight")
        plt.show()
        plt.close(fig)
    else:
        print(C.DATASET_ERROR_MSG)
    return fig, ax


update_dimensions()
