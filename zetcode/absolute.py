import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        label_1 = QLabel('ZetCode', self)
        label_1.move(15, 10)

        label_2 = QLabel('tutorials', self)
        label_2.move(35, 40)

        label_3 = QLabel('for programmers', self)
        label_3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()