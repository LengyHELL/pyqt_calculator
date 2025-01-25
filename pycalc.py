"""Calculator app demo"""

import sys
from functools import partial
from collections.abc import Callable

from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from PyQt6.QtCore import Qt

ERROR_MSG = "ERROR"
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40


class PyCalcWindow(QMainWindow):
    """Main window (view)"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)

        self.generalLayout = QVBoxLayout()

        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonMap: dict[str, QPushButton] = {}
        buttonLayout = QGridLayout()
        keyboard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyboard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonLayout)

    def setDisplayText(self, text):
        """Set the display's text"""
        self.display.setText(text)
        self.display.setFocus()

    def getDisplayText(self):
        """Get the display's text"""
        return self.display.text()

    def clearDisplay(self):
        """Clear the display"""
        self.setDisplayText("")


def evaluateExpression(expression):
    """Evaluate an expression (model)"""
    try:
        result = str(eval(expression))
    except Exception:
        result = ERROR_MSG

    return result


class PyCalc:
    """Controller class of the calculator"""

    def __init__(self, model: Callable[[str], str], view: PyCalcWindow):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(self._view.getDisplayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.getDisplayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.getDisplayText() + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(partial(self._buildExpression, keySymbol))

        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)
        self._view.display.returnPressed.connect(self._calculateResult)


def main():
    """Main function"""
    pycalcApp = QApplication(sys.argv)
    with open("pycalc.qss", "r", encoding="utf-8") as styles:
        pycalcApp.setStyleSheet(styles.read())

    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    PyCalc(evaluateExpression, pycalcWindow)
    sys.exit(pycalcApp.exec())


if __name__ == "__main__":
    main()
