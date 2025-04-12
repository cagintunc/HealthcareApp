
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, username):
        self.MainWindow = MainWindow
        self.username = username
        self.result = None

        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(561, 904)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("\n"
                                        "#frame {\n"
                                        "background-color: rgb(200, 200, 200);\n"
                                        "margin: 15%;\n"
                                        "}\n"
                                        "#frame QLabel {\n"
                                        "font: 15pt \"Book Antiqua\";\n"
                                        "qproperty-alignment: \"AlignCenter\";\n"
                                        "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setStyleSheet("max-height: 80px;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("#frame_2 {\n"
                                "    max-height: 140px;\n"
                                "    background-color: rgb(170, 170, 170);\n"
                                "    border-radius: 20%;\n"
                                "}\n"
                                "#frame_2 QLabel {\n"
                                "    background-color: rgb(170, 170, 170);\n"
                                "}\n"
                                "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox.setStyleSheet("min-height: 70px;\n"
                                   "background-color: rgb(233, 233, 233);\n" \
                                   "font: 15pt \"Book Antiqua\";\n" \
                                   "qproperty-alignment: \'AlignCenter\';")
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("max-height: 50%;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
                                        "background-color: rgb(233, 233, 233);\n"
                                        "border-radius: 10px;\n"
                                        "font: 15pt \"Book Antiqua\";\n"
                                        "padding: 10px;\n"
                                        "}\n"
                                        "QComboBox::drop-down {\n"
                                        "subcontrol-origin: padding;\n"
                                        "subcontrol-position: top right;\n"
                                        "width: 50px;\n"
                                        "border-left-width: 2px;\n"
                                        "border-left-color: darkgray;\n"
                                        "border-left-style: solid;\n"
                                        "border-top-right-radius: 10px;\n"
                                        "border-bottom-right-radius: 10px;\n"
                                        "}\n"
                                        "QComboBox::down-arrow {\n"
                                        "image: url(\'icons/arrow_combobox.png\');\n"
                                        "width: 40px;\n"
                                        "height: 40px;\n"
                                        "}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["Male", "Female", "Other"])
        self.verticalLayout_3.addWidget(self.comboBox_2)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("max-height: 50%;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setStyleSheet("QComboBox {\n"
                                        "background-color: rgb(233, 233, 233);\n"
                                        "border-radius: 10px;\n"
                                        "font: 15pt \"Book Antiqua\";\n"
                                        "padding: 10px;\n"
                                        "}\n"
                                        "QComboBox::drop-down {\n"
                                        "subcontrol-origin: padding;\n"
                                        "subcontrol-position: top right;\n"
                                        "width: 50px;\n"
                                        "border-left-width: 2px;\n"
                                        "border-left-color: darkgray;\n"
                                        "border-left-style: solid;\n"
                                        "border-top-right-radius: 10px;\n"
                                        "border-bottom-right-radius: 10px;\n"
                                        "}\n"
                                        "QComboBox::down-arrow {\n"
                                        "image: url(\'icons/arrow_combobox.png\');\n"
                                        "width: 40px;\n"
                                        "height: 40px;\n"
                                        "}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Employed", "Retired", "Unemployed"])
        self.verticalLayout_3.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                        "max-width: 400px !important;\n"
                                        "min-width: 300px !important;\n"
                                        "background-color: rgb(84, 84, 85);\n"
                                        "height: 70%;\n"
                                        "border-radius: 15%;\n"
                                        "font: 20pt \"Book Antiqua\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "margin-top: 40px;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "max-width: 400px !important;\n"
                                        "min-width: 300px !important;\n"
                                        "background-color: rgb(0, 70, 71);\n"
                                        "height: 70%;\n"
                                        "border-radius: 15%;\n"
                                        "font: 20pt \"Book Antiqua\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "margin-top: 40px;\n"
                                        "}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton, alignment=Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.frame)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.get_new_user_info)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)


    def get_new_user_info(self):
        self.result = [self.username, 
                       self.spinBox.value(), 
                       self.comboBox.currentText(),
                       self.comboBox_2.currentText()]
        self.MainWindow.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Record New User"))
        self.label_4.setText(_translate("MainWindow", "New Patient Information"))
        self.label.setText(_translate("MainWindow", "Age"))
        self.label_2.setText(_translate("MainWindow", "Gender"))
        self.label_3.setText(_translate("MainWindow", "Employment Status"))
        self.pushButton.setText(_translate("MainWindow", "Next"))

    def get_result(self):
        return self.result


def main(app, username):
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, username)
    MainWindow.show()
    app.exec_()
    return ui.get_result()
