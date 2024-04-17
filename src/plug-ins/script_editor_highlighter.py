import os
import sys
import inspect


def maya_useNewAPI():  # noqa
    pass  # dummy method to tell Maya this plugin uses Maya Python API 2.0


def initializePlugin(plugin):
    file_path = os.path.abspath(inspect.getfile(maya_useNewAPI))
    source_path = os.path.dirname(os.path.dirname(file_path))
    sys.path.append(source_path)
    from highlighter import setup_highlighter
    setup_highlighter()


def uninitializePlugin(plugin):
    # TODO
    pass
