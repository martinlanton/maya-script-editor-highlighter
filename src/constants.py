from pathlib import Path
import re

from maya import cmds


MAYA_VERSION = cmds.about(version=True)
IS_OLD_MAYA = MAYA_VERSION < "2025"

DEFAULT_COLOR = "white"
DEFAULT_FONT_FAMILY = "Courier New"
RULES_FILE_PATH = Path(__file__).parent / "syntax_rules.json"

_WINDOWS_PATH_PATTERN = r"(?P<drive>[A-Za-z]:)[/\\](?P<path>[^:*?\"<>|\s]+\.[\w]+)"
WINDOWS_PATH_RGX = re.compile(_WINDOWS_PATH_PATTERN)

_LINE_NUMBER_PATTERN = r"(?i)line\s(?P<line_number>\d+)"
LINE_NUMBER_RGX = re.compile(_LINE_NUMBER_PATTERN)

# VSCODE_EXE = r"C:\Users\arl\AppData\Local\Programs\Microsoft VS Code\Code.exe"
# VSCODE_CMD = f"{VSCODE_EXE} --goto {{file_path}}:{{line_number}}"
_PYCHARM_EXE = r"C:\Program Files\JetBrains\PyCharm 2023.2.1\bin\pycharm64.exe"
_PYCHARM_CMD = f"{_PYCHARM_EXE} --line {{line_number}} {{file_path}}"

IDE_CMD = _PYCHARM_CMD
