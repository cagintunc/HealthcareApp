
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, test_type, test_name):
        self.MainWindow = MainWindow
        self.result = None
        self.test_type = test_type
        self.test_name = test_name

        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(690, 640)
        self.MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame {\n"
                                "    background-color: rgb(200, 200, 200);\n"
                                "    margin: 20%;\n"
                                "    padding: 0%;\n"
                                "}\n"
                                "QLabel {\n"
                                "text-align: center;\n"
                                "qproperty-alignment: \'AlignCenter\';\n"
                                "font: 20pt \"Book Antiqua\";\n"
                                "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("QLabel {\n"
                                        "text-align: center;\n"
                                        "qproperty-alignment: \'AlignCenter\';\n"
                                        "margin-bottom: 60%;\n"
                                        "}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setStyleSheet("background-color: rgb(233,233,233);\n"
                                        "min-height: 60%;\n"
                                        "border-radius: 20%;\n"
                                        "font: 20pt \"Book Antiqua\";")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(84, 84, 85);\n"
                                        "height: 70%;\n"
                                        "border-radius: 15%;\n"
                                        "font: 20pt \"Book Antiqua\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "margin-top: 60%;\n"
                                        "margin-left: 50%;\n"
                                        "margin-right: 10%;\n"
                                        "margin-bottom: 60%;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(0, 70, 71);\n"
                                        "height: 70%;\n"
                                        "border-radius: 15%;\n"
                                        "font: 20pt \"Book Antiqua\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "margin-top: 60%;\n"
                                        "margin-left: 50%;\n"
                                        "margin-right: 10%;\n"
                                        "margin-bottom: 60%;\n"
                                        "}")
        self.pushButton.setObjectName("pushButton_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "background-color: rgb(84, 84, 85);\n"
                                        "height: 70%;\n"
                                        "border-radius: 15%;\n"
                                        "font: 20pt \"Book Antiqua\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "margin-top: 60%;\n"
                                        "margin-left: 10%;\n"
                                        "margin-right: 50%;\n"
                                        "margin-bottom: 60%;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "background-color: rgb(0, 70, 71);\n"
                                        "height: 70%;\n"
                                        "border-radius: 15%;\n"
                                        "font: 20pt \"Book Antiqua\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "margin-top: 60%;\n"
                                        "margin-left: 10%;\n"
                                        "margin-right: 50%;\n"
                                        "margin-bottom: 60%;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("#label_3 {\n"
                                "    font: 30pt \"Kunstler Script\";\n"
                                "   color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(84, 84, 85, 90);\n"
                                "    margin: 0% !important;\n"
                                "\n"
                                "}\n"
                                "")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.verticalLayout_2.addWidget(self.frame)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        
        self.pushButton.clicked.connect(self.browse_file)
        self.pushButton_2.clicked.connect(self.next)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "MRI Image"))
        self.label_2.setText(_translate("MainWindow", f"{self.test_type.title()} Data Entry\n"
                                        f"{self.test_name.title()}"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.label_3.setText(_translate("MainWindow", "\"Precision in practice.\"\n"
                                        "— Atul Gawande —"))
        
    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(None, 
                                                   "Select an MRI image", 
                                                   "", 
                                                   "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")
        
        if file_name: 
            self.lineEdit.setText(file_name)
        else:
            QMessageBox.information(None, 
                                   "No File Selected",
                                   "Please select an image file.")
    
    def next(self):
        currentFilePath = self.lineEdit.text()

        if currentFilePath == "":
            QMessageBox.information(None, 
                                    "Path of The Image Is NOT Given. CLICK BROWSE!",
                                    "File path should be given (Path of the image which your MRI result resides).")
        
        elif not os.path.exists(currentFilePath):
            self.lineEdit.setText("")
            QMessageBox.information(None,
                                    "There Is NO Path Like That!",
                                    "File path written is NOT a valid path! Give a valid path!")
            
        else:
            self.result = currentFilePath
            self.MainWindow.close()

    def get_result(self):
        return self.result
            


def main(app, test_type, test_name):
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, test_type, test_name)
    MainWindow.show()
    app.exec_()
    return ui.get_result()
