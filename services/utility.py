
import os
import sys
from typing import Union
documentdir = "Documents"


def createdirdoc(path=os.path.expanduser(f"~/{documentdir}"), dirname: str = "solardocs") -> str:
    newpath = os.path.join(path, dirname)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        return newpath
    return newpath


def resource_path(relative_path: str) -> str:
    try:
        base_dir = sys._MEIPASS2  # type: ignore
    except Exception:
        base_dir = os.path.abspath(".")
    return os.path.normpath(os.path.join(base_dir, relative_path))
