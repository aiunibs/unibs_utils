class C:
    """
    Constants class
    """

    SMALL = "small"
    MEDIUM = "medium"
    BIG = "big"

    FONT = "font"
    AXES_TITLE = "axes title"
    AXES_LABEL = "axes label"
    XTICK = "xtick"
    YTICK = "ytick"
    LEGEND_FONT = "legend font"
    LEGEND_TITLE = "legend title"
    TITLE = "title"
    LATEX = "latex"

    COLUMN = 0
    ROW = 1

    MAX = 0
    MIN = 1

    STYLES = ["-", "--"]
    COLORS = [
        "tab:blue",
        "tab:orange",
        "tab:green",
        "tab:red",
        "tab:olive",
        "tab:purple",
    ]
    MARKERS = ["v", "^", "s", "o", "*", "h"]

    DEFAULT_COLOR = "tab:blue"
    DEFAULT_MARKER = None
    DEFAULT_STYLE = "-"

    SAVE_OK_MSG = "{0} saved in {1}"
    LOAD_OK_MSG = "{0} loaded from {1}"

    WARNING_MSG = "Could not find {0}. Using default {1}"
    TICKS_WARNING_MSG = 'The number of {0}ticks labels is different from the number of {0}ticks'

    LOAD_ERROR_MSG = (
        "Could not load {0} from {1}."
    )
    SAVE_ERROR_MSG = "Could not save {0} in {1}"
    DATASET_ERROR_MSG = (
        "Error while parsing the dataset. Make sure dataset is a matrix."
    )
    SIZE_ERROR_MSG = (
        f"Unknown size value. Accepted sizes are {SMALL}, {MEDIUM} and {BIG}"
    )
    SIZE_LATEX_ERROR_MSG = SIZE_ERROR_MSG + f"\nlatex accepted sizes are true and false"

    DIMENSIONS_ERROR_MSG = f"Unknown dimension value. Accepted dimensions are {0}"
    VALUE_ERROR_MSG = "New value must be an integer"
    SMALL_ERROR_MSG = "Small size must be between 0 and medium size ({0})"
    MEDIUM_ERROR_MSG = "Medium size must be between small size ({0}) and big size ({1})"
    BIG_ERROR_MSG = "Big size must be greater than medium size ({0})"

    X = 'x'
    Y = 'y'

    NONE = 0
    JSON = 1
    TXT = 2
    PICKLE = 3
