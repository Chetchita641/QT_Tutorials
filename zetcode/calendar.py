from PyQt5.QtWidgets import (
    QWidget, QCalendarWidget, QLabel, QApplication, QVBoxLayout
)
from PyQt5.QtCore import QDate
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)

        self.label = QLabel(self)
        date = cal.selectedDate()
        self.label.setText(date.toString())

        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.label.setText(date.toString())

    
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()