
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.result = -1
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(435, 838)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(200, 200, 200);\n"
                                "margin:30%;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("background-color: rgb(130, 130, 130);\n"
                                "border-radius: 50%;\n"
                                "margin: 60%;\n"
                                "font: 30pt \"Kunstler Script\";\n"
                                "color: rgb(255, 255, 255);\n"
                                "margin-bottom: 160%;\n"
                                "text-align: center;\n"
                                "qproperty-alignment: \'AlignCenter\';\n"
                                "")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(84, 84, 85);\n"
                                        "    height: 70%;\n"
                                        "    border-radius: 15%;\n"
                                        "    font: 20pt \"Book Antiqua\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    margin-top: 0%;\n"
                                        "    margin-left: 50%;\n"
                                        "    margin-right: 50%;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(0, 70, 71);\n"
                                        "    height: 70%;\n"
                                        "    border-radius: 15%;\n"
                                        "    font: 20pt \"Book Antiqua\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    margin-top: 0%;\n"
                                        "    margin-left: 50%;\n"
                                        "    margin-right: 50%;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(84, 84, 85);\n"
                                        "    height: 70%;\n"
                                        "    border-radius: 15%;\n"
                                        "    font: 20pt \"Book Antiqua\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    margin-top: 0%;\n"
                                        "    margin-left: 50%;\n"
                                        "    margin-right: 50%;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(0, 70, 71);\n"
                                        "    height: 70%;\n"
                                        "    border-radius: 15%;\n"
                                        "    font: 20pt \"Book Antiqua\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    margin-top: 0%;\n"
                                        "    margin-left: 50%;\n"
                                        "    margin-right: 50%;\n"
                                        "}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.add_new_user)
        self.pushButton_2.clicked.connect(self.get_history)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_history(self):
        self.result = 0
        self.MainWindow.close()

    def add_new_user(self):
        self.result = 1
        self.MainWindow.close()

    def get_result(self):
        return self.result

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.label.setText(_translate("MainWindow", "\"Keep it simple.\" \n"
                                                        "— Albert Einstein —"))
        self.pushButton_2.setText(_translate("MainWindow", "History"))
        self.pushButton.setText(_translate("MainWindow", "New"))


def main(app):
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    return ui.get_result()
