from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QLabel


class Ui_Form(object):
    def emojiBox(self,Form):
        self.pushButtonSmail = QtWidgets.QPushButton(Form)
        self.pushButtonSmail.setGeometry(QtCore.QRect(10,370, 30, 30))
        self.pushButtonSmail.setObjectName("😂")
        self.pushButtonHeartFace = QtWidgets.QPushButton(Form)
        self.pushButtonHeartFace .setGeometry(QtCore.QRect(10,410, 30, 30))
        self.pushButtonHeartFace .setObjectName("😍")
        self.pushButtonTaxi = QtWidgets.QPushButton(Form)
        self.pushButtonTaxi.setGeometry(QtCore.QRect(10, 450, 30, 30))
        self.pushButtonTaxi.setObjectName("🚕")
        #2.layout
        self.pushButtonGlassFace = QtWidgets.QPushButton(Form)
        self.pushButtonGlassFace.setGeometry(QtCore.QRect(45,370, 30, 30))
        self.pushButtonGlassFace.setObjectName("😎")
        self.pushButtonStarFace = QtWidgets.QPushButton(Form)
        self.pushButtonStarFace.setGeometry(QtCore.QRect(45, 410, 30, 30))
        self.pushButtonStarFace.setObjectName("🤩")
        self.pushButtonRoket = QtWidgets.QPushButton(Form)
        self.pushButtonRoket.setGeometry(QtCore.QRect(45,450, 30, 30))
        self.pushButtonRoket.setObjectName("🚀")
        # 3.layout
        self.pushButtonGozK = QtWidgets.QPushButton(Form)
        self.pushButtonGozK.setGeometry(QtCore.QRect(80, 370, 30, 30))
        self.pushButtonGozK.setObjectName("😉")
        self.pushButtonTongue = QtWidgets.QPushButton(Form)
        self.pushButtonTongue.setGeometry(QtCore.QRect(80, 410, 30, 30))
        self.pushButtonTongue.setObjectName("😋")
        self.pushButtonHandS = QtWidgets.QPushButton(Form)
        self.pushButtonHandS .setGeometry(QtCore.QRect(80, 450, 30, 30))
        self.pushButtonHandS .setObjectName("👋")
        #4.layout
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
        self.pushButton.setGeometry(QtCore.QRect(10, 590, 300, 28))
        self.pushButton.setObjectName("pushButton")
        self.label1 = QtWidgets.QLabel("Client:",Form)

        self.label2 =QtWidgets.QLabel("Chat Rooms",Form)





        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 490, 300, 87))
        self.textEdit.setObjectName("textEdit")

        #Chat Room

        self.textEditChatName = QtWidgets.QTextEdit(Form)
        self.textEditChatName.setGeometry(QtCore.QRect(320, 20, 300, 50))
        self.textEditChatName.setPlaceholderText("Please input room name:")
        self.textEditChatName.setObjectName("textEdit")
        self.textEditChatPass = QtWidgets.QTextEdit(Form)
        self.textEditChatPass.setGeometry(QtCore.QRect(320, 80, 300, 50))
        self.textEditChatPass.setObjectName("textEdit")
        self.textEditChatPass.setPlaceholderText("Please input the chatroom password:")
        self.pushButtonSetRoom = QtWidgets.QPushButton(Form)
        self.pushButtonSetRoom.setGeometry(QtCore.QRect(320,150, 300, 100))
        self.pushButtonSetRoom.setObjectName("pushButton")
        #Other
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 300, 350))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser2.setGeometry(QtCore.QRect(10,680, 300, 300))
        self.textBrowser2.setObjectName("textBrowser")

        self.vbox3 = QtWidgets.QVBoxLayout(Form)
        self.vbox3.setAlignment(QtCore.Qt.AlignCenter)
        self.vbox3.setObjectName("vbox3")

        self.label1.setText("CLİENTS:")
        self.label1.setWindowTitle( "CLİENTS:")
        self.label1.setFont(QtGui.QFont("Sanserif", 12))
        self.label1.setStyleSheet("color:red;padding:5px")
        self.label2.setText("ChatRooms:")
        self.label2.setWindowTitle( "ChatRooms:")
        self.label2.setFont(QtGui.QFont("Sanserif", 12))
        self.label2.setStyleSheet("color:red;padding:5px")

        self.vbox = QtWidgets.QVBoxLayout(Form)
        self.vbox.setAlignment(QtCore.Qt.AlignTop)
        self.vbox.setObjectName("vbox1")

        self.vbox2 = QtWidgets.QVBoxLayout(Form)
        self.vbox2.setAlignment(QtCore.Qt.AlignBottom)
        self.vbox2.setObjectName("vbox2")


        self.vbox3.addWidget(self.label1)
        self.vbox3.addLayout(self.vbox)

        self.vbox3.addWidget(self.label2)
        self.vbox3.addLayout(self.vbox2)

        #self.vbox2.setGeometry(QtCore.QRect(20, 600,200,40))
        self.emojiBox(Form)

       # self.btn = QtWidgets.QPushButton()
       # self.btn.setVisible(True)
       # self.btn.setMinimumSize(150, 30)
       # self.vbox2.addWidget(self.btn)


        self.retranslateUi(Form)



        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label1.setText(_translate("Form", "CLİENTS :"))
        self.label1.setWindowTitle(_translate("Form", "CLİENTS :"))

        self.label2.setText(_translate("Form", "CHATROOMS :"))
        self.label2.setWindowTitle(_translate("Form", "CHATROOMS :"))

        self.pushButton.setText(_translate("Form", "Send 🗯"))
        self.pushButtonSetRoom.setText(_translate("Form", "Create ChatRoom"))

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
