from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 470, 300, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 370, 300, 87))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 300, 350))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser2.setGeometry(QtCore.QRect(320,20, 300, 350))
        self.textBrowser2.setObjectName("textBrowser")
        self.vbox = QtWidgets.QVBoxLayout(Form)
        #self.vbox.addStretch(1)
        self.vbox.setAlignment(QtCore.Qt.AlignCenter)
        #self.hbox.setGeometry(QtCore.QRect(650, 20, 600, 250))
        self.vbox.setObjectName("hbox")
        btn = QtWidgets.QPushButton()
        btn.setMinimumSize(150, 30)



        self.retranslateUi(Form)



        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Send"))
