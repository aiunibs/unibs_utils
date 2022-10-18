from utils_unibs.constants import C
import numpy as np
import re


def get_idxs(position: int, count_vals: int):
    """
    Computes intervals of length count_val given the current position.

    Args:
        position: an integer representing the current position along the axis
        count_vals: an integer representing the size of the interval. Value -1 represents the whole axis.

    Returns:
        A tuple that contains the beginning (included) and the end (not included) of the interval.

    """
    if count_vals <= 0:
        next_idx = np.iinfo(int).max
        prev_idx = 0
    else:

        next_idx = (position - position % count_vals) + count_vals
        prev_idx = next_idx - count_vals if next_idx - count_vals > 0 else 0

    return prev_idx, next_idx


def _tex_escape(text):
    """
    Source: https://stackoverflow.com/questions/16259923/how-can-i-escape-latex-special-characters-inside-django-templates

    Args:
        text: a plain text message

    Returns:
        the message escaped to appear correctly in LaTeX
    """
    conv = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\^{}",
        "\\": r"\textbackslash{}",
        "<": r"\textless{}",
        ">": r"\textgreater{}",
    }
    regex = re.compile(
        "|".join(
            re.escape(str(key))
            for key in sorted(conv.keys(), key=lambda item: -len(item))
        )
    )
    return regex.sub(lambda match: conv[match.group()], text)


def _get_formatted_element(el: object, precision: int = 1):
    try:
        f = float(el)
        return f"{f:.{precision}f}"
    except ValueError:
        s = str(el)
        return f"{_tex_escape(s)}"


def print_latex_table(
    dataset: list,
    labels: list = None,
    best=-1,
    axis: int = 0,
    count_vals: int = -1,
    precision: int = 1,
    hline: int = 0,
):
    """
    Creates a latex table of a given dataset

    Args:
        dataset: a list that contains the data that compose the table divided by rows
        labels: the list of labels to put at the beginning of each row. Default is None
        best: an integer representing the best value to highlight {-1: None, 0: Max, 1: Min}
        axis: An integer representing the axis along which to compute the best value {0: COLUMN, 1: ROW}
        count_vals: An integer representing the length of the interval within which to compute the best value.
                    Value -1 represents the whole axis.
        precision: an int that contains the float precision. Default is 1
        hline: an int that contains the number of rows after which to put an horizontal line. Default is 0

    Returns:
        A string that contains the latex body of the given dataset
    """
    table = np.asanyarray(dataset)

    max_idxs = []
    function = ""
    s = ""

    if best == C.MAX:
        function = np.max
    elif best == C.MIN:
        function = np.min

    for i, r in enumerate(table):

        try:
            if labels is not None:
                s += _get_formatted_element(labels[i])
            else:
                raise IndexError
        except IndexError:
            pass
        s += " & "

        for j, el in enumerate(r):
            try:
                if best == 0 or best == 1:
                    if axis == C.COLUMN:
                        prev_idx, next_idx = get_idxs(i, count_vals)
                        max_idxs = np.where(
                            table[:, j] == function(table[prev_idx:next_idx, j])
                        )[0]
                    elif axis == C.ROW:
                        prev_idx, next_idx = get_idxs(j, count_vals)
                        max_idxs = np.where(
                            table[i] == function(table[i, prev_idx:next_idx])
                        )[0]
            except Exception as e:
                max_idxs = []

            if (axis == C.COLUMN and i in max_idxs) or (
                axis == C.ROW and j in max_idxs
            ):
                s += r"\bf{"
            s += _get_formatted_element(el, precision)
            if (axis == C.COLUMN and i in max_idxs) or (
                axis == C.ROW and j in max_idxs
            ):
                s += "}"
            s += " & "
        s = s[:-2]
        s += r"\\"
        if hline > 0 and i % hline == hline - 1:
            s += "\hline"
        s += "\n"
    return s


def print_text_table(
    title: str, headers: list, rows: list, just: int = 10, precision: int = 2
) -> list:
    """
    Create a text table that contains the given rows

    Args:
        title: a string that contains the table title
        headers: a list of string that contains the table headers
        rows: a list that contains the table values
        just: an int that contains the justification value for each column. Default is 10
        precision: an int that contains the float precision. Default is 2

    Returns:
        a list of string that contains the rows of the table
    """
    to_ret = []
    divider = "-" * ((just + 5) * len(headers) - 4)
    to_ret.append(title)
    to_ret.append(divider)
    s = ""
    for h in headers:
        s += f"{str(h).rjust(just)}     "
    to_ret.append(s)
    to_ret.append(divider)

    for row in rows:
        s = ""
        for value in row:
            if type(value) == int:
                s += f"{value:{just}.{precision}f}     "
            elif type(value) == float or type(value) == np.float64:
                s += f"{value:{just}.{precision}f}     "
            elif type(value) == str:
                s += f"{value.rjust(just)}     "
            else:
                print(f"Could not parse type {type(value)}")
        to_ret.append(s)
    to_ret.append(divider)
    return to_ret


def transpose_latex_table(table_string: str):
    """
    Transpose a latex table

    Args:
        table_string (str): A latex table

    Returns:
        str: The transposed table
    """
    data = []
    to_return = ""

    lines = table_string.split("\n")
    for line in lines:
        elements = line.split("&")
        if len(elements) > 1:
            data.append([e.replace("\\", "").strip() for e in elements])
    data = np.asanyarray(data)
    data = data.T
    for i in range(data.shape[0]):
        if i == 0:
            to_return += "\\toprule\n"
        elif i == 1:
            to_return += "\\midrule\n"
        for j in range(data.shape[1]):
            if j > 0:
                to_return += " & "
            to_return += data[i, j]
        to_return += " \\\\ \n"
    to_return += r"\bottomrule"
    return to_return