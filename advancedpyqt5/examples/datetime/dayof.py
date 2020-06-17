#!/usr/bin/python3

from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

print("Day of month: {0}".format(now.day()))
print("Day of week: {0}".format(now.dayOfWeek()))
print("Day of year: {0}".format(now.dayOfYear()))

