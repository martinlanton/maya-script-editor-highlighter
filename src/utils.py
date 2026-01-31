from __future__ import annotations

import json
import logging
import os
import traceback
from pathlib import Path
import subprocess

try:
    from PySide2 import QtWidgets
    from shiboken2 import wrapInstance
except:
    from PySide6 import QtWidgets
    from shiboken6 import wrapInstance

from maya import OpenMayaUI as omui

import constants


logger = logging.getLogger("SCRIPT EDITOR HIGHLIGHTER")
logger.setLevel(logging.INFO)


def is_valid_path(path: str | Path) -> bool:
    if isinstance(path, str):
        path = Path(path)
    # Check if path is not empty
    if not str(path).strip():
        return False
    # Check if path have invalid character
    invalid_chars = '<>:"|?*'
    parts = path.parts
    for part in parts:
        if ':' not in part and any(char in part for char in invalid_chars):
            return False
    
    return True


def is_valid_file(file_path: str | Path) -> bool:
    return is_valid_path(file_path) and Path(file_path).is_file()


def read_json(path: str):
    if not Path(path).is_file():
        raise RuntimeError(f"Path {path} is not a file !")

    try:
        with open(path, "r") as handle:
            return json.load(handle)
    except Exception:
        logger.debug(traceback.format_exc())
        raise RuntimeError(f"Error on read file {path}")


def open_in_ide(path: None | str | Path, line_number: str):
    if not path:
        return
    if isinstance(path, str):
        path = Path(path)

    if not is_valid_file(path):
        logger.error(f"Invalid file path: {path}")
        return
        
    if not path.exists():
        logger.error(f"File not found: {path}")
        return

    try:
        cmd_string = constants.ide_cmd.format(line_number=line_number, file_path=path)
        subprocess.Popen(cmd_string)
    except Exception as e:
        logger.error(f"Error on open file: {e}")


def open_in_explorer(path: None | str | Path):
    if not path:
        return
    if isinstance(path, str):
        path = Path(path)

    if not is_valid_file(path):
        logger.error(f"Invalid file path: {path}")
        return
        
    if not path.exists():
        logger.error(f"File not found: {path}")
        return

    try:
        path_str = path.as_posix().replace("/", "\\")
        if os.name == 'nt':
            subprocess.Popen(f'explorer /select, {path_str}')
        else:
            os.startfile(path_str)
    except Exception as e:
            logger.error(f"Error on open file: {e}")


def script_editor_output_widget() -> QtWidgets.QPlainTextEdit:
    i = 0
    while i < 1000:
        ptr = omui.MQtUtil.findControl(f"cmdScrollFieldReporter{i}")   
        if ptr: 
            return wrapInstance(int(ptr), QtWidgets.QPlainTextEdit)
        i += 1
