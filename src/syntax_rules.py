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
        Rules.append((QtCore.QRegularExpression(fr"\b{keyword}\b"), keyword_format))
