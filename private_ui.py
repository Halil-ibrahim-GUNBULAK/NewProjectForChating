from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Private(object):
    def emojiBox(self,Form):
        self.pushButtonSmail = QtWidgets.QPushButton(Form)
        self.pushButtonSmail.setGeometry(QtCore.QRect(10, 370, 30, 30))
        self.pushButtonSmail.setObjectName("😂")
        self.pushButtonHeartFace = QtWidgets.QPushButton(Form)
        self.pushButtonHeartFace.setGeometry(QtCore.QRect(10, 410, 30, 30))
        self.pushButtonHeartFace.setObjectName("😍")
        self.pushButtonTaxi = QtWidgets.QPushButton(Form)
        self.pushButtonTaxi.setGeometry(QtCore.QRect(10, 450, 30, 30))
        self.pushButtonTaxi.setObjectName("🚕")
        # 2.layout
        self.pushButtonGlassFace = QtWidgets.QPushButton(Form)
        self.pushButtonGlassFace.setGeometry(QtCore.QRect(45, 370, 30, 30))
        self.pushButtonGlassFace.setObjectName("😎")
        self.pushButtonStarFace = QtWidgets.QPushButton(Form)
        self.pushButtonStarFace.setGeometry(QtCore.QRect(45, 410, 30, 30))
        self.pushButtonStarFace.setObjectName("🤩")
        self.pushButtonRoket = QtWidgets.QPushButton(Form)
        self.pushButtonRoket.setGeometry(QtCore.QRect(45, 450, 30, 30))
        self.pushButtonRoket.setObjectName("🚀")
        # 3.layout
        self.pushButtonGozK = QtWidgets.QPushButton(Form)
        self.pushButtonGozK.setGeometry(QtCore.QRect(80, 370, 30, 30))
        self.pushButtonGozK.setObjectName("😉")
        self.pushButtonTongue = QtWidgets.QPushButton(Form)
        self.pushButtonTongue.setGeometry(QtCore.QRect(80, 410, 30, 30))
        self.pushButtonTongue.setObjectName("😋")
        self.pushButtonHandS = QtWidgets.QPushButton(Form)
        self.pushButtonHandS.setGeometry(QtCore.QRect(80, 450, 30, 30))
        self.pushButtonHandS.setObjectName("👋")
        # 4.layout
        self.pushButtonGa = QtWidgets.QPushButton(Form)
        self.pushButtonGa.setGeometry(QtCore.QRect(115, 370, 30, 30))
        self.pushButtonGa.setObjectName("🙄")
        self.pushButtonSad = QtWidgets.QPushButton(Form)
        self.pushButtonSad.setGeometry(QtCore.QRect(115, 410, 30, 30))
        self.pushButtonSad.setObjectName("😔")
        self.pushButtonHandSOK = QtWidgets.QPushButton(Form)
        self.pushButtonHandSOK.setGeometry(QtCore.QRect(115, 450, 30, 30))
        self.pushButtonHandSOK.setObjectName("👍")
        # 5.layout
        self.pushButtonHeartB = QtWidgets.QPushButton(Form)
        self.pushButtonHeartB.setGeometry(QtCore.QRect(150, 370, 30, 30))
        self.pushButtonHeartB.setObjectName("💙")
        self.pushButtonHeartBr = QtWidgets.QPushButton(Form)
        self.pushButtonHeartBr.setGeometry(QtCore.QRect(150, 410, 30, 30))
        self.pushButtonHeartBr.setObjectName("💔")
        self.pushButtonHandSW = QtWidgets.QPushButton(Form)
        self.pushButtonHandSW.setGeometry(QtCore.QRect(150, 450, 30, 30))
        self.pushButtonHandSW.setObjectName("✍")
        # 6.layout
        self.pushButtonHug = QtWidgets.QPushButton(Form)
        self.pushButtonHug.setGeometry(QtCore.QRect(185, 370, 30, 30))
        self.pushButtonHug.setObjectName("🤗")
        self.pushButtonStrong = QtWidgets.QPushButton(Form)
        self.pushButtonStrong.setGeometry(QtCore.QRect(185, 410, 30, 30))
        self.pushButtonStrong.setObjectName("💪")
        self.pushButtonComp = QtWidgets.QPushButton(Form)
        self.pushButtonComp.setGeometry(QtCore.QRect(185, 450, 30, 30))
        self.pushButtonComp.setObjectName("🎉")
        # 7.layout
        self.pushButtonAngle = QtWidgets.QPushButton(Form)
        self.pushButtonAngle.setGeometry(QtCore.QRect(220, 370, 30, 30))
        self.pushButtonAngle.setObjectName("😇")
        self.pushButtonRose = QtWidgets.QPushButton(Form)
        self.pushButtonRose.setGeometry(QtCore.QRect(220, 410, 30, 30))
        self.pushButtonRose.setObjectName("🌹")
        self.pushButtonHandSa = QtWidgets.QPushButton(Form)
        self.pushButtonHandSa.setGeometry(QtCore.QRect(220, 450, 30, 30))
        self.pushButtonHandSa.setObjectName("👏")
        # 8.layout
        self.pushButtonHmm = QtWidgets.QPushButton(Form)
        self.pushButtonHmm.setGeometry(QtCore.QRect(255, 370, 30, 30))
        self.pushButtonHmm.setObjectName("🤔")
        self.pushButtonFire = QtWidgets.QPushButton(Form)
        self.pushButtonFire.setGeometry(QtCore.QRect(255, 410, 30, 30))
        self.pushButtonFire.setObjectName("🔥")
        self.pushButtonHan = QtWidgets.QPushButton(Form)
        self.pushButtonHan.setGeometry(QtCore.QRect(255, 450, 30, 30))
        self.pushButtonHan.setObjectName("💞")


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 590, 300, 30))
        self.pushButton.setObjectName("pushButton1")
        self.pushButtonSelect = QtWidgets.QPushButton(Form)
        self.pushButtonSelect.setGeometry(QtCore.QRect(10, 630, 100, 30))
        self.pushButtonSelect.setObjectName("pushButton2")
        self.pushButtonSend = QtWidgets.QPushButton(Form)
        self.pushButtonSend.setGeometry(QtCore.QRect(220, 630, 100, 30))
        self.pushButtonSend.setObjectName("pushButton3")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 490, 300, 87))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 300, 350))
        self.vbox = QtWidgets.QVBoxLayout(Form)
        self.turnBackButton = QtWidgets.QPushButton(Form)
        self.turnBackButton.setGeometry(QtCore.QRect(320,10, 150, 50))
        self.turnBackButton.setObjectName("turnBackButton")
        #self.vbox.addStretch(1)
        self.vbox.setAlignment(QtCore.Qt.AlignCenter)
        #self.hbox.setGeometry(QtCore.QRect(650, 20, 600, 250))
        self.vbox.setObjectName("hbox")
        self.emojiBox(Form)




        self.retranslateUi(Form)



        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Send 🗯"))
        self.pushButtonSelect.setText(_translate("Form", "Select File 📁"))
        self.pushButtonSend.setText(_translate("Form", "Send File ⏫"))
        self.turnBackButton.setText(_translate("Form", "Turn Back ⍇"))
        self.pushButtonSmail.setText(_translate("Form", "😂"))
        self.pushButtonHeartFace.setText(_translate("Form", "😍"))
        self.pushButtonTaxi.setText(_translate("Form", "🚕"))

        self.pushButtonGlassFace.setText(_translate("Form", "😎"))

        self.pushButtonStarFace.setText(_translate("Form", "🤩"))

        self.pushButtonRoket.setText(_translate("Form", "🚀"))
        # 3.layout

        self.pushButtonGozK.setText(_translate("Form", "😉"))

        self.pushButtonTongue.setText(_translate("Form", "😋"))

        self.pushButtonHandS.setText(_translate("Form", "👋"))

        self.pushButtonGa.setText(_translate("Form", "🙄"))

        self.pushButtonSad.setText(_translate("Form", "😔"))

        self.pushButtonHandSOK.setText(_translate("Form", "👍"))
        # 5.layout

        self.pushButtonHeartB.setText(_translate("Form", "💙"))

        self.pushButtonHeartBr.setText(_translate("Form", "💔"))

        self.pushButtonHandSW.setText(_translate("Form", "✍"))
        # 6.layout

        self.pushButtonHug.setText(_translate("Form", "🤗"))

        self.pushButtonStrong.setText(_translate("Form", "💪"))

        self.pushButtonComp.setText(_translate("Form", "🎉"))
        # 7.layout

        self.pushButtonAngle.setText(_translate("Form", "😇"))

        self.pushButtonRose.setText(_translate("Form", "🌹"))

        self.pushButtonHandSa.setText(_translate("Form", "👏"))
        # 8.layout

        self.pushButtonHmm.setText(_translate("Form", "🤔"))

        self.pushButtonFire.setText(_translate("Form", "🔥"))

        self.pushButtonHan.setText(_translate("Form", "💞"))
