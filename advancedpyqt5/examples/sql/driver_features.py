#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt5 tutorial

This example shows available SQLite driver
features.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
'''

from PyQt5 import QtSql
import sys


def main():
      
  db = QtSql.QSqlDatabase.addDatabase("QSQLITE")

  driver = db.driver()
  print(driver.hasFeature(QtSql.QSqlDriver.Transactions))
  print(driver.hasFeature(QtSql.QSqlDriver.BLOB))
  print(driver.hasFeature(QtSql.QSqlDriver.Unicode))
  print("**********")
  print(driver.hasFeature(QtSql.QSqlDriver.PreparedQueries))
  print(driver.hasFeature(QtSql.QSqlDriver.NamedPlaceholders))
  print(driver.hasFeature(QtSql.QSqlDriver.MultipleResultSets))
  print("**********")
  print(driver.hasFeature(QtSql.QSqlDriver.QuerySize))
  print(driver.hasFeature(QtSql.QSqlDriver.BatchOperations))
  print(driver.hasFeature(QtSql.QSqlDriver.EventNotifications))

  db.close()
    

if __name__ == '__main__':
    
  main()

