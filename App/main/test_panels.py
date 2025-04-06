from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mainmenu
import newUser

app = QtWidgets.QApplication(sys.argv)
query_1 = mainmenu.main(app)

if query_1 == 1:
    new_user_info = newUser.main(app)
    print(new_user_info)


