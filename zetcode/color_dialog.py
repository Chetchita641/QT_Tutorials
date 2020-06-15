import sys
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QFrame,
    QColorDialog, QApplication
)
from PyQt5.QtGui import QColor

class Example(QWidget):
    super().__init__()

    self.initUI()

def initUI(self):
    col = QColor(0, 0, 0)

    self.button = QPushButton('Dialog', self)
    self.button.move(20, 20)

    