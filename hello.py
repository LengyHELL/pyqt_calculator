"""Hello world with PyQt6"""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QRadioButton,
)

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 300, 300)

helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)

button = QPushButton("Hello", parent=window)
button.move(60, 50)

lineEdit = QLineEdit("szia", parent=window)
lineEdit.move(60, 100)

comboBox = QComboBox(parent=window)
comboBox.move(60, 150)

radioButton = QRadioButton("helo", parent=window)
radioButton.move(60, 200)

window.show()

sys.exit(app.exec())
