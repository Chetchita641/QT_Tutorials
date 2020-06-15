from PySide2.QtCore import (
    Slot,
    Qt, QAbstractTableModel, QModelIndex
)
from PySide2.QtGui import QKeySequence, QColor
from PySide2.QtWidgets import (
    QMainWindow, QAction, qApp,
    QBoxLayout, QHeaderView, QSizePolicy, QTableView, QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Earthquakes information')

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu('File')

        # Exit QAction
        exit_action = QAction('Exit', self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage('Data loaded and plotted')

        # Window dimensions
        geometry = qApp.desktop().availableGeometry(self)
        self.setFixedHeight(geometry.width() * 0.8, geometry.height() * 0.7)