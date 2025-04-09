
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import sqlite3
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, curr):
        self.MainWindow = MainWindow
        self.is_searched = False
        self.curr = curr

        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(900, 300)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(200, 200, 200);\n"
                                 "font: 15pt 'Book Antiqua';\n")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")


        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setStyleSheet("background-color: rgb(233,233,233);\n"
                                        "min-height: 60%;\n"
                                        "border-radius: 20%;\n"
                                        "font: 15pt \"Book Antiqua\";\n")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                        "    max-width: 400px;\n"
                                        "    min-width: 200px;\n"
                                        "    background-color: rgb(84, 84, 85);\n"
                                        "    height: 70%;\n"
                                        "    border-radius: 15%;\n"
                                        "    font: 20pt \"Book Antiqua\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    margin-top: 60%;\n"
                                        "    margin-bottom: 60%;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(0, 70, 71);\n"
                                        "}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton, alignment=Qt.AlignCenter)

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.label.setFixedHeight(0)
        self.verticalLayout_3.addWidget(self.label)

        self.verticalLayout_2.addWidget(self.frame)

        self.scroll_area = QtWidgets.QScrollArea(self.frame)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedHeight(0) 
        self.scroll_content = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        self.verticalLayout_3.addWidget(self.scroll_area)

        self.verticalLayout_2.addWidget(self.frame)

        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.search_user)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def search_user(self):
        userquery = self.lineEdit.text()
        if userquery == "":
            QMessageBox.information(None, "Empty Input!",
                                    "Please write the username before searching!!")
            return

        if not os.path.exists("database/HealthcareDB.db"):
            QMessageBox.information(None, "No Database Found!",
                                    "There is NO database available!")
            self.MainWindow.close()
            return

        user_search = f"""SELECT * FROM user_table WHERE userName = '{userquery}';"""
        results = self.curr.execute(user_search).fetchall()

        if len(results) == 0:
            QMessageBox.information(None, "No Such User",
                                    f"There is no user named {userquery}!")
            return
        self.label.setFixedHeight(70)
        self.verticalLayout_2.addWidget(self.frame)

        self.label.setText(f"Search Results for {userquery}")

        # Clear previous results from scroll area
        for i in reversed(range(self.scroll_layout.count())):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        user_id = int(results[0][0])
        brain_table = f"SELECT * FROM brain_tests_table WHERE user_id = {user_id};"
        lung_table = f"SELECT * FROM lung_tests_table WHERE user_id = {user_id};"

        content = self.curr.execute(brain_table).fetchall()
        content += self.curr.execute(lung_table).fetchall()
        if len(content) == 1:
            self.scroll_area.setFixedHeight(100)
        elif len(content) == 2:
            self.scroll_area.setFixedHeight(130)
        else:
            self.scroll_area.setFixedHeight(200)

        for row in content:
            row_layout = QtWidgets.QHBoxLayout()

            label_1 = QtWidgets.QLabel(userquery)
            label_2 = QtWidgets.QLabel(str(row[4]))  # Date or test type?
            label_3 = QtWidgets.QLabel(str(row[2]))  # Result?

            label_1.setStyleSheet("padding-right: 5px;")
            label_2.setStyleSheet("padding-right: 5px;")
            label_3.setStyleSheet("padding-right: 5px;")
            

            row_layout.addWidget(label_1)
            row_layout.addWidget(label_2)
            row_layout.addWidget(label_3)

            row_widget = QtWidgets.QWidget()
            row_widget.setLayout(row_layout)
            row_widget.setStyleSheet("QWidget {" \
            "background-color: rgb(220, 220, 220);}" \
            "QWidget:hover {" \
            "background-color: rgb(240, 240, 240);}")

            self.scroll_layout.addWidget(row_widget)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "User Search Engine"))
        self.label.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "Search by Name"))
        self.pushButton.setText(_translate("MainWindow", "Search"))


def main(app, curr):
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, curr)
    MainWindow.show()
    app.exec_()