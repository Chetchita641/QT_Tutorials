import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QLineEdit,
    QInputDialog, QApplication
)

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.button = QPushButton('Dialog', self)
        self.button.move(20, 20)
        self.button.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Input dialog')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(str(text))


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()