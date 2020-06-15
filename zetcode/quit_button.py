import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton
)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qbutton = QPushButton('Quit', self)
        qbutton.clicked.connect(QApplication.instance().quit)
        qbutton.resize(qbutton.sizeHint())
        qbutton.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

def main():
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()