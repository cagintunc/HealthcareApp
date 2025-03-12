from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys
import main_panel


app = QtWidgets.QApplication(sys.argv)
query_1 = main_panel.main(app)

#query_1 = 1: medical test

#query_1 = 2: gene test

#query_1 = 3: overall test
