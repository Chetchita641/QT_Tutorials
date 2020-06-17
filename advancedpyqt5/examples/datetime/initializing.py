#!/usr/bin/python3

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

d1 = QDate(2017, 12, 9)
t1 = QTime(18, 50, 59)

dt1 = QDateTime(d1, t1, Qt.LocalTime)

#locale = QLocale(QLocale.English, QLocale.UnitedKingdom)

#curr_locale = QLocale()
#print(curr_locale.nativeCountryName(), curr_locale.name(), curr_locale.nativeLanguageName())

print("Datetime: {0}".format(dt1.toString()))
print("Date: {0}".format(d1.toString()))
print("Time: {0}".format(t1.toString()))        
