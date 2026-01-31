try:
    from PySide2 import QtCore, QtGui
except:
    from PySide6 import QtCore, QtGui

import constants
import utils


class LinkFilter(QtCore.QObject):

    instance = None

    def __init__(self, parent=None):
        super().__init__(parent)

    @staticmethod
    def get_file_path_and_line_number(text):
        match = constants.WINDOWS_PATH_RGX.search(text)
        if not match:
            return None, None
        
        file_path = match.group(0)
        line_match = constants.LINE_NUMBER_RGX.search(text)
        line_number = line_match.group("line_number") if line_match else None
        
        return file_path, line_number

    def eventFilter(self, obj, event):
        is_mouse_button = event.type() in [QtCore.QEvent.Type.MouseButtonPress]
        if is_mouse_button:
            is_ctrl_modifier = event.modifiers() == QtCore.Qt.ControlModifier
            if is_ctrl_modifier:
                cursor = obj.cursorForPosition(obj.mapFromGlobal(QtGui.QCursor().pos()))
                text = cursor.block().text()
                path, line_number = self.get_file_path_and_line_number(text)
                if line_number:
                    utils.open_in_ide(path, line_number)
                else:
                    utils.open_in_explorer(path)

                return True

        return super().eventFilter(obj, event)
