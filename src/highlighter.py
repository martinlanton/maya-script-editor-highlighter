import logging

try:
    from PySide2 import QtGui, QtWidgets
except ImportError:
    from PySide6 import QtGui, QtWidgets

from syntax_rules import SyntaxRule
from link_filter import LinkFilter
import constants
import utils


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class StdOut_Syntax(QtGui.QSyntaxHighlighter):

    def __init__(self, rules: list, document: QtGui.QTextDocument):
        super().__init__(document)
        self.rules = rules
        self._highlight_func = self.__old if constants.IS_OLD_MAYA else self.__new
        self.normal, self.traceback = range(2)

        self.traceback_rule = None
        for rule in self.rules:
            if rule.multiline:
                self.traceback_rule = rule
                break

    def highlightBlock(self, text: str):
        previous_state = self.previousBlockState()
    
        # Handle multiline traceback
        if self.traceback_rule:
            if self._matches_pattern(self.traceback_rule.pattern, text):
                self.setCurrentBlockState(self.traceback)
                self.setFormat(0, len(text), self.traceback_rule.format)
                return

            if previous_state == self.traceback:
                stripped = text.strip()
                if stripped == '' or stripped == '#':
                    self.setCurrentBlockState(self.traceback)
                    return
                elif text.startswith(('#  ', '# \t', '# File')) or self._is_exception_line(text):
                    self.setCurrentBlockState(self.traceback)
                    self.setFormat(0, len(text), self.traceback_rule.format)
                    return
                else:
                    self.setCurrentBlockState(self.normal)

        # Apply other rules
        for rule in self.rules:
            if not rule.multiline:
                self._highlight_func(rule, text)
        
        if self.currentBlockState() == -1:
            self.setCurrentBlockState(self.normal)
    
    def _matches_pattern(self, pattern, text: str) -> bool:
        if constants.IS_OLD_MAYA:
            return pattern.indexIn(text) == 0
        else:
            match = pattern.match(text)
            return match.hasMatch() and match.capturedStart() == 0
    
    def _is_exception_line(self, text: str) -> bool:
        stripped = text.strip()
        if not stripped:
            return False
        
        if stripped.startswith('# '):
            stripped = stripped[2:].strip()

        if ':' in stripped:
            before_colon = stripped.split(':')[0].strip()
            return (before_colon and 
                    before_colon[0].isupper() and 
                    ('Error' in before_colon or 'Exception' in before_colon or before_colon == 'Error'))

        return stripped and stripped[0].isupper() and '(' in stripped

    def __old(self, rule: SyntaxRule, text: str):
        index = rule.pattern.indexIn(text)
        while index >= 0:
            length = rule.pattern.matchedLength()
            self.setFormat(index, length, rule.format)
            index = rule.pattern.indexIn(text, index + length)

    def __new(self, rule: SyntaxRule, text: str):
        iterator = rule.pattern.globalMatch(text)
        while iterator.hasNext():
            match = iterator.next()
            index = match.capturedStart()
            length = match.capturedLength()
            self.setFormat(index, length, rule.format)


def __se_highlight():
    logger.debug("Attaching highlighter")
    script_editor_output_widget = utils.script_editor_output_widget()
    if not script_editor_output_widget:
        return
    logger.debug(script_editor_output_widget)
    StdOut_Syntax(SyntaxRule.get_rules(), script_editor_output_widget.document())
    instance = LinkFilter.instance
    if not instance:
        event_filter = LinkFilter()
        script_editor_output_widget.installEventFilter(event_filter)
        LinkFilter.instance = event_filter
    logger.debug("Done attaching highlighter to : %s" % script_editor_output_widget)


__qt_focus_change_callback = {"cmdScrollFieldReporter": __se_highlight}


def __on_focus_changed(old_widget, new_widget):
    """Enable the highlighter when changing focus to the script editor.

    :param old_widget: previously focused widget. Argument passed by the signal triggering this.
    :param new_widget: currently focused widget. Argument passed by the signal triggering this.
    """
    if new_widget:
        widget_name = new_widget.objectName()
        cbs = [name for name in __qt_focus_change_callback if widget_name.startswith(name)]
        for callback in cbs:
            __qt_focus_change_callback[callback]()


def setup_highlighter():
    try:
        app = QtWidgets.QApplication.instance()
        app.focusChanged.connect(__on_focus_changed)
        __se_highlight()
    except Exception as exp:
        pass
