from dataclasses import dataclass, field
from typing import Optional

try:
    from PySide2 import QtGui
    from PySide2.QtCore import QRegExp
except:
    from PySide6 import QtGui
    from PySide6.QtCore import QRegularExpression as QRegExp

from . import constants, utils


@dataclass
class SyntaxRule:

    pattern: str
    color: Optional[str] = None
    background_color: Optional[str] = None
    font_family: Optional[str] = None
    italic: bool = False
    underline: bool = False
    multiline: bool = False
    
    format: QtGui.QTextCharFormat = field(init=False, repr=False)
    font: QtGui.QFont = field(init=False, repr=False)
    
    def __post_init__(self):
        self.pattern = QRegExp(self.pattern)
        self.font_family = self.font_family or constants.DEFAULT_FONT_FAMILY
        self.format = QtGui.QTextCharFormat()
        self.font = QtGui.QFont()
        self.setup()

    def setup(self):
        self.format.setForeground(QtGui.QColor(self.color or constants.DEFAULT_COLOR))
        self.font.setFamily(self.font_family)
        if self.background_color:
            self.format.setBackground(QtGui.QColor(self.background_color))
        if self.underline:
            self.format.setUnderlineStyle(QtGui.QTextCharFormat.SingleUnderline)

    @staticmethod
    def get_rules() -> list:
        data = utils.read_json(constants.RULES_FILE_PATH)
        return [SyntaxRule(**d) for _, d in data.items()]

"""
# TODO : finish implementing python keyword highlighting in stack traces
class PythonSyntaxRules(object):
    keywords = [
        "False",
        "await",
        "else",
        "import",
        "pass",
        "None",
        "break",
        "except",
        "in",
        "raise",
        "True",
        "class",
        "finally",
        "is",
        "return",
        "and",
        "continue",
        "for",
        "lambda",
        "try",
        "as",
        "def",
        "from",
        "nonlocal",
        "while",
        "assert",
        "del",
        "global",
        "not",
        "with",
        "async",
        "elif",
        "if",
        "or",
        "yield",
    ]

    kOrange = QtGui.QColor(255, 80, 0)

    keyword_format = QtGui.QTextCharFormat()
    keyword_format.setForeground(kOrange)

    Rules = []
    # For some reason this doesn't work as a list comprehension and yields an "undefined" for
    # keyword format in the following list comprehension :
    # Rules = [(QtCore.QRegExp(r"((\s){}(\s))".format(keyword)), keyword_format) for keyword in keywords]
    for keyword in keywords:
        Rules.append((QtCore.QRegExp(r"((\s){}(\s))".format(keyword)), keyword_format))
"""