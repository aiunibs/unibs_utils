import json
import pickle
from os.path import join
import os
from utils_unibs.constants import C


def _load_file(
    read_file: str,
    load_ok: str = "File loaded",
    error: str = f"Error while loading file",
    type: int = C.NONE,
) -> object:
    """
    Load single file. It handles txt, pddl, json and pickle files

    Args:
        read_file: string that contains the path to the file
        load_ok: string that contains the message to print when the loading is successful
        error: string that contains the message to print when the loading is not successful

    Returns:
        the loaded file
    """
    try:
        if type == C.JSON or (type == C.NONE and read_file.lower().endswith(".json")):
            with open(read_file, "r") as rf:
                o = json.load(rf)
        elif type == C.TXT or (
            type == C.NONE
            and (
                read_file.lower().endswith(".txt")
                or read_file.lower().endswith(".pddl")
            )
        ):
            with open(read_file, "r") as rf:
                o = rf.readlines()
        else:
            with open(read_file, "rb") as rf:
                o = pickle.load(rf)
        print(load_ok)
    except FileNotFoundError:
        print(error)
        o = None

    return o


def load_from_folder(read_dir: str, files: list, type: int = 0) -> list:
    """
    Load files from a given folder. Supports txt, pddl, json and pickle files.

    Args:
        read_dir: a string that contains the path to a folder
        files: a list of file names within the folder

    Returns:
        A list of loaded files
    """

    to_return = []
    for file_name in files:
        to_return.append(
            _load_file(
                join(read_dir, file_name),
                load_ok=C.LOAD_OK_MSG.format(file_name, read_dir),
                error=C.LOAD_ERROR_MSG.format(file_name, read_dir),
                type=type,
            )
        )
    return to_return


def save_file(o: object, target_dir: str, filename: str) -> bool:
    """
    Saves a given object in a file. Supports txt, json and pickle files.
    Args:
        o: object to save
        target_dir: path to the target directory. It is created if it does not exist
        filename: target file name. If needed it must contain the extension

    Returns:
        True if the saving is successful, False otherwise
    """

    os.makedirs(target_dir, exist_ok=True)
    try:
        if filename.endswith(".json") or filename.endswith(".JSON"):
            with open(join(target_dir, filename), "w") as wf:
                json.dump(o, wf, indent=4)
        elif filename.endswith(".txt") or filename.endswith(".TXT"):
            with open(join(target_dir, filename), "w") as wf:
                wf.writelines(o)
        else:
            with open(join(target_dir, filename), "wb") as wf:
                pickle.dump(o, wf)
        wf.close()
        print(C.SAVE_OK_MSG.format(filename, target_dir))
        return True
    except pickle.PicklingError:
        print(C.SAVE_ERROR_MSG.format(filename, target_dir))
        return False
