from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QApplication
)
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 100)
        self.label.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()