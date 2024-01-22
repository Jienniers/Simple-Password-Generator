from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation
import pyperclip
import random

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(669, 518)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/padlock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 671, 521))
        self.stackedWidget.setStyleSheet("background-color: rgb(88, 88, 88);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(60, 0, 541, 91))
        self.label.setStyleSheet("font: 48pt \"Impact\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(10, 140, 201, 31))
        self.label_2.setStyleSheet("font: 20pt \"Impact\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.page)
        self.lineEdit.setGeometry(QtCore.QRect(220, 140, 291, 31))
        self.lineEdit.setStyleSheet("border:none;\n"
"font: 20pt \"Impact\";\n"
"background-color: rgb(131, 131, 131);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(20, 230, 201, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 36pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(92, 143, 154);\n"
"border:none;\n"
"border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 145, 142);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(97, 189, 186);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(200, 300, 261, 91))
        self.label_3.setStyleSheet("font: 48pt \"Impact\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setGeometry(QtCore.QRect(110, 400, 401, 51))
        self.label_4.setStyleSheet("border:none;\n"
"font: 20pt \"Impact\";\n"
"background-color: rgb(131, 131, 131);\n"
"border-radius:5px;\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.clear_btn = QtWidgets.QPushButton(self.page)
        self.clear_btn.setGeometry(QtCore.QRect(410, 230, 201, 51))
        self.clear_btn.setStyleSheet("QPushButton{\n"
"font: 36pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(92, 143, 154);\n"
"border:none;\n"
"border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 145, 142);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(97, 189, 186);\n"
"}")
        self.clear_btn.setObjectName("clear_btn")
        self.Copy_btn = QtWidgets.QPushButton(self.page)
        self.Copy_btn.setGeometry(QtCore.QRect(200, 460, 201, 51))
        self.Copy_btn.setStyleSheet("QPushButton{\n"
"font: 36pt \"Impact\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(92, 143, 154);\n"
"border:none;\n"
"border-radius:3px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(50, 145, 142);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(97, 189, 186);"
"transition-duration: 0.4s\n"
"}")
        self.Copy_btn.setObjectName("Copy_btn")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
###################################Connections########################################

        self.pushButton.clicked.connect(self.generter)
        self.clear_btn.clicked.connect(self.clear_label)
        self.Copy_btn.clicked.connect(self.copy)




####################################Connections End##########################################

#####################################Functions##############################################
    
    
    def generter(self):
        self.label_4.clear()
        # storing the keys in a list which will be used to generate 
# the password 
        pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
        'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
        'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
        '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
        '*', '(', ')']

# declaring the empty string
        password = "" 

        # loop to generate the random password of the length entered           
        # by the user
        for x in range(int(self.lineEdit.text())):
                password = password + random.choice(pass1)

# setting the password to the entry widget
        text2=self.label_4.text()
        self.label_4.setText(password)




    def clear_label(self):
            self.label_4.clear()

    def copy(self):
        random_password = self.label_4.text()
        pyperclip.copy(random_password)

###########################################Functions end ###########################################

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Password Generator"))
        self.label.setText(_translate("Form", "Password Generator"))
        self.label_2.setToolTip(_translate("Form", "Password lenght"))
        self.label_2.setText(_translate("Form", "Password Lenght:"))
        self.lineEdit.setToolTip(_translate("Form", "Enter password Lenght in numbers"))
        self.pushButton.setText(_translate("Form", "Generate"))
        self.pushButton.setShortcut(_translate("Form", "Return"))
        self.label_3.setText(_translate("Form", "Password"))
        self.label_4.setText(_translate("Form", "Password:"))
        self.clear_btn.setText(_translate("Form", "Clear"))
        self.clear_btn.setShortcut(_translate("Form", "Shift+Backspace"))
        self.Copy_btn.setText(_translate("Form", "Copy"))
        self.Copy_btn.setShortcut(_translate("Form", "Shift+Backspace"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
