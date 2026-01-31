import os
import sys
import inspect

from highlighter import setup_highlighter


def msg():
    return "Loading script editor highlighter"


print(msg())

file_path = os.path.abspath(inspect.getfile(msg))
source_path = os.path.dirname(os.path.dirname(file_path))
sys.path.append(source_path)
setup_highlighter()
