"""Signals and slots demo"""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QLineEdit,
    QDialog,
)


class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Signals and slots")
        self.name = ""

        layout = QVBoxLayout()

        lineEdit = QLineEdit()
        lineEdit.textChanged.connect(self._setName)

        button = QPushButton("Greet")
        button.clicked.connect(self._greet)

        layout.addWidget(lineEdit)
        layout.addWidget(button)

        self.msgLabel = QLabel("")
        layout.addWidget(self.msgLabel)

        self.setLayout(layout)

    def _setName(self, name):
        self.name = name

    def _greet(self):
        self.msgLabel.setText("" if self.msgLabel.text() else f"Hello, {self.name}!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
