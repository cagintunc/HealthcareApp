

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.result = -1
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(747, 562)
        self.MainWindow.setStyleSheet("background-color: rgb(48, 48, 71);\n"
                                        "color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(90, 40, 90, 40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setStyleSheet("font: 24pt \"Symbol\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "\n"
                                        "text-align: center;\n"
                                        "qproperty-alignment: \'AlignCenter\';\n"
                                        "")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("\n"
                                "text-align: center;\n"
                                "qproperty-alignment: \'AlignCenter\';\n"
                                "")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setStyleSheet("\n"
                                "text-align: center;\n"
                                "qproperty-alignment: \'AlignCenter\';\n"
                                "")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setStyleSheet("\n"
                                "text-align: center;\n"
                                "qproperty-alignment: \'AlignCenter\';\n"
                                "")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setStyleSheet("font: 24pt \"Symbol\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "\n"
                                        "text-align: center;\n"
                                        "qproperty-alignment: \'AlignCenter\';\n"
                                        "")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    font: 18pt \"MS Shell Dlg 2\";\n"
                                        "    \n"
                                        "    background-color: rgb(70, 0, 0);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(0, 0, 80);\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                        "    font: 18pt \"MS Shell Dlg 2\";\n"
                                        "    \n"
                                        "    background-color: rgb(70, 0, 0);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(0, 0, 80);\n"
                                        "}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    font: 18pt \"MS Shell Dlg 2\";\n"
                                        "    \n"
                                        "    background-color: rgb(70, 0, 0);\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    background-color: rgb(0, 0, 80);\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setStyleSheet("font: 24pt \"Symbol\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "\n"
                                        "text-align: center;\n"
                                        "qproperty-alignment: \'AlignCenter\';\n"
                                        "")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.gridLayout.setRowStretch(0, 30)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()

        self.pushButton.clicked.connect(lambda: self.button_clicked(2))
        self.pushButton_2.clicked.connect(lambda: self.button_clicked(3))
        self.pushButton_3.clicked.connect(lambda: self.button_clicked(1))
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "BioHackers Main Panel"))
        self.label_3.setText(_translate("MainWindow", "b Test"))
        self.label.setText(_translate("MainWindow", "Y test number"))
        self.label_8.setText(_translate("MainWindow", "b test number"))
        self.label_9.setText(_translate("MainWindow", "Overall number"))
        self.label_2.setText(_translate("MainWindow", "bY Test"))
        self.pushButton_3.setText(_translate("MainWindow", "Test"))
        self.pushButton.setText(_translate("MainWindow", "Test"))
        self.pushButton_2.setText(_translate("MainWindow", "Test"))
        self.label_7.setText(_translate("MainWindow", "Y Test"))

    def button_clicked(self, x):
        self.result = x
        self.MainWindow.close()


def main(app):
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    return ui.result
