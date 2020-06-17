#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial 

This is a simple Sokoban game clone.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: September 2017
'''

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QImage, QColor
from PyQt5.QtCore import Qt
import os, sys

SPACE = 20
OFFSET = 30

LEFT_COLLISION = 1
RIGHT_COLLISION = 2
TOP_COLLISION = 3
BOTTOM_COLLISION = 4


level = """
    ######
    ##   #
    ##$  #
  ####  $##
  ##  $ $ #
#### # ## #   ######
##   # ## #####  ..#
## $  $          ..#
###### ### #@##  ..#
    ##     #########
    ########
"""


       
class Actor:

    def __init__(self, x, y):
        
        self._x = x
        self._y = y

    def getImage(self):
        return self.image
        
    def x(self):
        return self._x
    
    def y(self):
        return self._y
        
    def setX(self, x):
        self._x = x

    def setY(self, y):
        self._y = y
        
    def isLeftCollision(self, actor):
        
        if ((self.x() - SPACE) == actor.x()) and \
            (self.y() == actor.y()):
            return True
        else:
            return False
            
    def isRightCollision(self, actor):
        
        if ((self.x() + SPACE) == actor.x()) and \
            (self.y() == actor.y()):
            return True
        else:
            return False
            
    def isTopCollision(self, actor):
        
        if ((self.y() - SPACE) == actor.y()) and \
            (self.x() == actor.x()):
            return True
        else:
            return False
    
    def isBottomCollision(self, actor):
        
        if ((self.y() + SPACE) == actor.y()) and \
            (self.x() == actor.x()):
            return True
        else:
            return False
    

class Baggage(Actor):

    def __init__(self, x, y):
        super().__init__(x, y)
        
        try:
            self.image = QImage("baggage.png")
            
        except Exception as e:
            
            print(e.message)
            sys.exit(1)
        
    def move(self, x, y):
        
        self._x += x
        self._y += y
        
        
class Player(Actor):

    def __init__(self, x, y):
        super().__init__(x, y)
        
        try:
            self.image = QImage("sokoban.png")
            
        except Exception as e:
            
            print(e.message)
            sys.exit(1)
                
    def move(self, x, y):
        
        self._x += x
        self._y += y
        
        
class Wall(Actor):

    def __init__(self, x, y):
        super().__init__(x, y)
        
        try:
            self.image = QImage("wall.png")
            
        except Exception as e:
            
            print(e.message)
            sys.exit(1)
                
                
class Area(Actor):

    def __init__(self, x, y):
        super().__init__(x, y)
        
        try:
            self.image = QImage("area.png")
            
        except Exception as e:
            
            print(e.message)
            sys.exit(1)
        

class Board(QWidget):

    def __init__(self):
        super().__init__()
        
        self.setFocusPolicy(Qt.StrongFocus)
        
        self.initBoard()
        
        
    def initBoard(self):    
  
        self.world = []
        self.walls = []
        self.baggs = []
        self.areas = []
       
        self.w = 0
        self.h = 0
        
        self.completed = False
        self.soko = None

        self.initWorld()
        self.resize(self.w, self.h)
        

    def getWidth(self):
        return self.w
        
        
    def getHeight(self):
        return self.h
        
    
    def initWorld(self):
       
        x = OFFSET
        y = OFFSET
                
        for i in range(len(level)):
            
            item = level[i]
            
            if item == '\n':
                
                y += SPACE
                
                if self.w < x:
                    self.w = x
                    
                x = OFFSET
                
            elif item == '#':
                
                w = Wall(x, y)
                self.walls.append(w)
                x += SPACE
                
            elif item == '$':
                
                b = Baggage(x, y)
                self.baggs.append(b)
                x += SPACE
                
            elif item == '.':
                
                a = Area(x, y)
                self.areas.append(a)
                x += SPACE
                
            elif item == '@':
                
                self.soko = Player(x, y)
                x += SPACE
                
            elif item == " ":
                x += SPACE    
    
        self.h = y

        
    def buildWorld(self, painter):
    
        painter.setBrush(QColor(250, 240, 170))
        painter.setPen(QColor(250, 240, 170))
        painter.drawRect(0, 0, self.width(), self.height())
        painter.setPen(QColor(0, 0, 0))
       
        world = self.walls + self.areas + \
            self.baggs + [self.soko]
        
        for i in range(len(world)):
            
            item = world[i]
            
            if isinstance(item, Player) or \
                isinstance(item, Baggage):
                painter.drawImage(item.x()+2, item.y()+2, 
                                   item.getImage())
            else: 
                painter.drawImage(item.x(), item.y(), 
                                   item.getImage())
            
        
        if self.completed:
            painter.drawText(25, 20, "Completed")
        
    
        
    def paintEvent(self, event):    
        super().paintEvent(event)
        
        painter = QPainter()        
        painter.begin(self)            
        self.buildWorld(painter)       
        painter.end()

        
    def keyReleaseEvent(self, event):
    
        if self.completed:
            return
        
        key = event.key()
                   
        if key == Qt.Key_Left:
            
            if self.checkWallCollision(self.soko,
                LEFT_COLLISION):
                return         
           
            if self.checkBagCollision(LEFT_COLLISION):
                return
                
            self.soko.move(-SPACE, 0)
            
        elif key == Qt.Key_Right:

            if self.checkWallCollision(self.soko, 
                RIGHT_COLLISION):
                return
            
            if self.checkBagCollision(RIGHT_COLLISION):
                return
            
            self.soko.move(SPACE, 0)
            
        elif key == Qt.Key_Up:
            
            if self.checkWallCollision(self.soko, 
                TOP_COLLISION):
                return
                      
            if self.checkBagCollision(TOP_COLLISION):
                return   
                
            self.soko.move(0, -SPACE)
            
        elif key == Qt.Key_Down:
        
            if self.checkWallCollision(self.soko, 
                BOTTOM_COLLISION):
                return
            
            if self.checkBagCollision(BOTTOM_COLLISION):
                return   
            
            self.soko.move(0, SPACE)
            
        elif key == Qt.Key_R:
            self.restartLevel()
            
        self.repaint()    
        
           
    def checkWallCollision(self, actor, _type):
    
        if _type == LEFT_COLLISION:
            
            for i in range(len(self.walls)):
                wall = self.walls[i]
                if actor.isLeftCollision(wall):
                    return True 
            return False
                    
        elif _type == RIGHT_COLLISION:
        
            for i in range(len(self.walls)):
                wall = self.walls[i]
                if actor.isRightCollision(wall):
                    return True        
            return False
                    
        elif _type == TOP_COLLISION:
        
            for i in range(len(self.walls)):
                wall = self.walls[i]
                if actor.isTopCollision(wall):
                    return True
            return False
                    
        elif _type == BOTTOM_COLLISION:
        
            for i in range(len(self.walls)):
                wall = self.walls[i]
                if actor.isBottomCollision(wall):
                    return True         
            return False
    
                              
    def checkBagCollision(self, _type):
    
        if _type == LEFT_COLLISION:
            
            for i in range(len(self.baggs)):
                bag = self.baggs[i]
                if self.soko.isLeftCollision(bag):
                    for i in range(len(self.baggs)):
                        item = self.baggs[i]
                        if not bag is item:
                            if bag.isLeftCollision(item):
                                return True
                        if self.checkWallCollision(bag, 
                            LEFT_COLLISION):
                                return True
                    bag.move(-SPACE, 0)            
                    self.isCompleted()
                    
            return False
                    
        elif _type == RIGHT_COLLISION:
        
            for i in range(len(self.baggs)):
                bag = self.baggs[i]
                if self.soko.isRightCollision(bag):
                    for i in range(len(self.baggs)):
                        item = self.baggs[i]
                        if not bag is item:
                            if bag.isRightCollision(item):
                                return True
                        if self.checkWallCollision(bag, 
                            RIGHT_COLLISION):
                            return True
                    bag.move(SPACE, 0)
                    self.isCompleted()

            return False
                    
        elif _type == TOP_COLLISION:
        
            for i in range(len(self.baggs)):
                bag = self.baggs[i]
                if self.soko.isTopCollision(bag):
                    for i in range(len(self.baggs)):
                        item = self.baggs[i]
                        if not bag is item:
                            if bag.isTopCollision(item):
                                return True
                        if self.checkWallCollision(bag, 
                            TOP_COLLISION):
                            return True
                    bag.move(0, -SPACE)         
                    self.isCompleted()

            return False
                    
        elif _type == BOTTOM_COLLISION:
        
            for i in range(len(self.baggs)):
                bag = self.baggs[i]
                if self.soko.isBottomCollision(bag):
                    for i in range(len(self.baggs)):
                        item = self.baggs[i]
                        if not bag is item:
                            if bag.isBottomCollision(item):
                                return True
                        if self.checkWallCollision(bag, 
                            BOTTOM_COLLISION):
                            return True
                    bag.move(0, SPACE) 
                    self.isCompleted()

            return False
    
    def isCompleted(self):
    
        num = len(self.baggs)
        completed = 0
        
        for i in range(num):
            bag = self.baggs[i]
            for j in range(num):
                area = self.areas[j]
                if bag.x() == area.x() and \
                   bag.y() == area.y():
                    completed += 1
                    
        if completed == num:
            self.completed = True
            self.repaint()

    def restartLevel(self):
    
        del self.areas[:]
        del self.baggs[:]
        del self.walls[:]
        self.initWorld()
        
        if self.completed:
            self.completed = False


class Sokoban(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
    
        self.setWindowTitle("Sokoban")        
        board = Board()
        self.setCentralWidget(board)
        self.resize(board.getWidth() + OFFSET, 
                     board.getHeight() + OFFSET)
        self.move(300, 300)
        self.show()


def main():
    
    app = QApplication([])
    sokoban = Sokoban()
    sys.exit(app.exec_())    

if __name__ == '__main__':
    main()        
        
