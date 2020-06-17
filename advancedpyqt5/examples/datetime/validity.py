#!/usr/bin/python3

from PyQt5.QtCore import QDate, Qt

dates = (QDate(2017, 5, 11), QDate(2017, 8, 1), 
         QDate(2017, 2, 30))

for date in dates:
    
    if date.isValid():
        print("{0} is a valid date".format(date.toString(Qt.ISODate)))
    else:
        print("{0} is not a valid date".format(date))
        

