#!/usr/bin/python3

from PyQt5.QtCore import QDate, Qt

d1 = QDate(2017, 4, 5)
d2 = QDate(2016, 4, 5)

if d1 < d2:
    print("{0} comes before {1}".format(d1.toString(Qt.ISODate), 
        d2.toString(Qt.ISODate)))
else:
    print("{0} comes after {1}".format(d1.toString(Qt.ISODate), 
        d2.toString(Qt.ISODate)))


