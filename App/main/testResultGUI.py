
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, username, results):
        self.username = username
        self.results = results
        self.MainWindow = MainWindow


        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(675, 809)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame {\n"
                                "    background-color :    rgb(200, 200, 200);\n"
                                "    margin: 20%;\n"
                                "}\n"
                                "QLabel {\n"
                                "    text-align: center;\n"
                                "    qproperty-alignment: \'AlignCenter\';\n"
                                "    font: 18pt \"Book Antiqua\";\n"
                                "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("max-height: 100px !important;\n"
                                 "margin-top: 20px;")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("#label_2 {\n"
                                        "    background-color: rgb(230, 230, 230);\n"
                                        "    margin-top: 30px;\n"
                                        "    padding-top: 20px;\n"
                                        "    padding-bottom: 20px;\n"
                                        "    margin-left: 20%;\n"
                                        "    margin-right: 20%;\n"
                                        "    font: 10pt \"Book Antiqua\";\n"
                                        "    text-align: left;\n"
                                        "    qproperty-alignment: \'AlignLeft\';\n"
                                        "    min-height: 250px;"
                                        "}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setStyleSheet("#pushButton {\n"
                                        "    width: 400px !important;"
                                        "    background-color: rgb(84, 84, 85);\n"
                                        "    border-radius: 15%;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    min-height: 70%;\n"
                                        "    font: 18pt \"Book Antiqua\";\n"
                                        "    margin-bottom: 50%;\n"
                                        "    margin-top: 50%;\n"
                                        "}\n"
                                        "\n"
                                        "#pushButton:hover {\n"
                                        "    width: 400px !important;\n"
                                        "    background-color: rgb(0, 70, 71);\n"
                                        "    border-radius: 15%;\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    min-height: 70%;\n"
                                        "    font: 20pt \"Book Antiqua\";\n"
                                        "    margin-bottom: 50%;\n"
                                        "    margin-top: 50%;\n"
                                        "}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton, alignment=Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("#label_3 {\n"
                                        "    font: 30pt \"Kunstler Script\";\n"
                                        "   color: rgb(255, 255, 255);\n"
                                        "    background-color: rgba(84, 84, 85, 0.9);\n"
                                        "    margin: 0% !important;\n"
                                        "\n"
                                        "}\n"
                                        "")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.end)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)
    
    def end(self):
        self.MainWindow.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        print(self.results)
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Test Result Page"))
        self.label.setText(_translate("MainWindow", f"Test Results for {self.username.title()}"))
        self.label_2.setText(_translate("MainWindow", f"""  Test Date: {self.results[1]}\n
        The patient who has a user name of '{self.username}' sent a {self.results[0]} tests.\n
        According to the system, there is a chance for this patient to be '{self.results[2]}'.\n
        Notice: Even though the models in these program were trained on real world data with a high accuracy,\n 
        the program can only give an estimation. Therefore, it's only purpose is to give a prediction, NOT a result!"""))
        self.pushButton.setText(_translate("MainWindow", "Finish"))
        self.label_3.setText(_translate("MainWindow", "\"Precision in practice.\"\n"
                                        "— Atul Gawande —"))


def main(app, username, results):
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, username, results)
    MainWindow.show()
    app.exec_()
    
    
