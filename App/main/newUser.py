
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.results = []
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(737, 807)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(200, 200, 200);\n"
                                "margin: 15%;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("\n"
                                "font: 20pt \"Book Antiqua\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setStyleSheet("background-color: rgb(233,233,233);\n"
                                        "min-height: 60%;\n"
                                        "border-radius: 20%;\n"
                                        "font: 20pt \"Book Antiqua\";\n"
                                        "")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("font: 20pt \"Book Antiqua\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setStyleSheet("""
                                        QComboBox {
                                                background-color: rgb(233, 233, 233);
                                                border-radius: 10px;
                                                font: 20pt "Book Antiqua";
                                                padding: 10px;
                                        }
                                        QComboBox::drop-down {
                                                subcontrol-origin: padding;
                                                subcontrol-position: top right;
                                                width: 30px;
                                                border-left-width: 1px;
                                                border-left-color: darkgray;
                                                border-left-style: solid;
                                                border-top-right-radius: 10px;
                                                border-bottom-right-radius: 10px;
                                        }
                                        QComboBox::down-arrow {
                                                image: url(icons/arrow_combobox.png);
                                                width: 15px;
                                                height: 15px;
                                        }
                                        """)
        self.comboBox.setObjectName("comboBox")


        self.comboBox.addItems(["Brain MRI Test", "Lung MRI Disease Test", "Alzeihmer Test"])


        self.verticalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(84, 84, 85);\n"
                                        "    height: 70%;\n"
                                        "    border-radius: 15%;\n"
                                        "    font: 20pt \"Book Antiqua\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    margin-top: 60%;\n"
                                        "    margin-bottom: 60%;\n"
                                        "    margin-left: 100%;\n"
                                        "    margin-right: 100%;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(0, 70, 71);\n"
                                        "    height: 70%;\n"
                                        "    border-radius: 15%;\n"
                                        "    font: 20pt \"Book Antiqua\";\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    margin-top: 60%;\n"
                                        "    margin-left: 100%;\n"
                                        "    margin-right: 100%;\n"
                                        "    margin-bottom: 60%;\n"
                                        "}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.frame)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        
        self.pushButton.clicked.connect(self.save_results)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def save_results(self):
        self.results.append(self.lineEdit.text())
        self.results.append(self.comboBox.currentText())
        self.MainWindow.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "New User Addition Portal"))
        self.label.setText(_translate("MainWindow", "Name/Id:"))
        self.label_2.setText(_translate("MainWindow", "Select the Test:"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

    def get_results(self):
        return self.results


def main(app):
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
    return ui.get_results()
