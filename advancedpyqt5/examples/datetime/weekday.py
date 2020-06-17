#!/usr/bin/python3

from PyQt5.QtCore import QDate, QLocale

now = QDate.currentDate()

dayOfWeek = now.dayOfWeek()

print(QDate.shortDayName(dayOfWeek))
print(QDate.longDayName(dayOfWeek))

locale = QLocale(QLocale.Slovak, QLocale.Slovakia)
print(locale.toString(now, 'dddd'))
#~ print(now.toString('dddd'))


