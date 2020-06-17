from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import QPoint, QBasicTimer
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.rot = 0
        self.timer = QBasicTimer()
        self.timer.start(500, self)

        self.setGeometry(300, 300, 430, 240)
        self.setWindowTitle('Soulmate')
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawDonut(painter)
        painter.end()

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.rot += 1
            self.repaint()
        else:
            super(Example, self).timerEvent(event)

    def drawDonut(self, painter):
        brush = QBrush(QColor('#535353'))
        painter.setPen(QPen(brush, 0.5))
        painter.setRenderHint(QPainter.Antialiasing)

        h = self.height()
        w = self.width()

        painter.translate(QPoint(w/2, h/2))

        for r in range(0, self.rot, 1):
            painter.rotate(float(r))
            painter.drawEllipse(-125, -40, 250, 80)

    
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
