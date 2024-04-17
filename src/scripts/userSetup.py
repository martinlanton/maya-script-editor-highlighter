import os
import sys
import inspect


def msg():
    return "Loading script editor highlighter"


print(msg())

file_path = os.path.abspath(inspect.getfile(msg))
source_path = os.path.dirname(os.path.dirname(file_path))
sys.path.append(source_path)
from highlighter import setup_highlighter
setup_highlighter()
