#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

This is a simple Snake game clone.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: October 2017
'''


from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QImage, QColor, QFont, QFontMetrics
from PyQt5.QtCore import Qt, QBasicTimer, QPoint

import random
import sys

WIDTH = 300
HEIGHT = 270
DOT_SIZE = 10
ALL_DOTS = WIDTH * HEIGHT // (DOT_SIZE * DOT_SIZE)
RAND_POS = 26
DELAY = 140

x = [0] * ALL_DOTS
y = [0] * ALL_DOTS


class Board(QWidget):

    def __init__(self):
        super().__init__()
        
        self.setFocusPolicy(Qt.StrongFocus)
     
        self.initGame()


    def timerEvent(self, event):

        if self.inGame:
            self.checkApple()
            self.checkCollision()
            self.move()
        else:
            self.timer.stop()
        
        self.repaint()
    
    
    def initGame(self):

        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.inGame = True
        self.dots = 3

        for i in range(self.dots):
            
            x[i] = 50 - i * 10
            y[i] = 50
        
        try:
            self.ball = QImage("dot.png")
            self.apple = QImage("apple.png")
            self.head = QImage("head.png")
            
        except Exception as e:
            
            print(e.message)
            sys.exit(1)

        self.locateApple()
        self.timer = QBasicTimer()
        self.timer.start(DELAY, self)


    def paintEvent(self, event):
        super().paintEvent(event)
       
        painter = QPainter()
        painter.begin(self)
        
        painter.setBrush(QColor(0, 0, 0, 255))
        painter.drawRect(0, 0, self.width(), self.height())

        if self.inGame:
            self.drawObjects(painter)
        else: 
            self.gameOver(painter)
        
        painter.end()


    def drawObjects(self, painter):
    
        painter.drawImage(self.apple_x, self.apple_y, self.apple)
        
        for z in range(self.dots):
            if z == 0: 
                painter.drawImage(x[z], y[z], self.head)
            else:
                painter.drawImage(x[z], y[z], self.ball)
    
           
    def gameOver(self, painter):

        msg = "Game Over"
        small = QFont("Helvetica", 12, QFont.Bold)
        metr = QFontMetrics(small)
        
        textWidth = metr.width(msg)
        h = self.height()
        w = self.width()

        painter.setPen(QColor(255, 255, 255))
        painter.setFont(small)
        painter.translate(QPoint(w/2, h/2))
        painter.drawText(-textWidth/2, 0, msg)

    
    def checkApple(self):

        if x[0] == self.apple_x and y[0] == self.apple_y: 
        
            self.dots = self.dots + 1
            self.locateApple()
        
    
    def move(self):

        z = self.dots

        while z > 0:
            
            x[z] = x[(z - 1)]
            y[z] = y[(z - 1)]
            z = z - 1

        if self.left:
            x[0] -= DOT_SIZE

        if self.right: 
            x[0] += DOT_SIZE

        if self.up:
            y[0] -= DOT_SIZE

        if self.down:
            y[0] += DOT_SIZE
        
    
    def checkCollision(self):

        z = self.dots
       
        while z > 0:
            if z > 4 and x[0] == x[z] and y[0] == y[z]:
                self.inGame = False
            z = z - 1

        if y[0] > HEIGHT - DOT_SIZE: 
            self.inGame = False
        
        if y[0] < 0:
            self.inGame = False
        
        if x[0] > WIDTH - DOT_SIZE:
            self.inGame = False

        if x[0] < 0:
            self.inGame = False
        

    def locateApple(self):
    
        r = random.randint(0, RAND_POS)
        self.apple_x = r * DOT_SIZE
        r = random.randint(0, RAND_POS)
        self.apple_y = r * DOT_SIZE
  

    def keyPressEvent(self, event): 
    
        key = event.key()

        if key == Qt.Key_Left and not self.right:
            
            self.left = True
            self.up = False
            self.down = False
                
        if key == Qt.Key_Right and not self.left: 
        
            self.right = True
            self.up = False
            self.down = False          
        
        if key == Qt.Key_Up and not self.down: 
        
            self.up = True
            self.right = False
            self.left = False            
        
        if key == Qt.Key_Down and not self.up: 
        
            self.down = True
            self.right = False
            self.left = False      


class Snake(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setWindowTitle("Snake")
        self.resize(WIDTH, HEIGHT)
        self.setCentralWidget(Board())

        self.move(300, 300)
        self.show()


def main():
    
    app = QApplication([])
    snake = Snake()
    sys.exit(app.exec_())    

if __name__ == '__main__':
    main()





