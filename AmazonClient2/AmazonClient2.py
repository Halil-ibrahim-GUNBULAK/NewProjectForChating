from functools import partial

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QFileDialog, QVBoxLayout, QFormLayout, QLineEdit, QDialogButtonBox
import client_ui
import connect_ui
import private_ui
import time
import sys
import socket
import random
from chat_room_ui import Ui_Form_chatRoom
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic.properties import QtGui


class ReceiveThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super(ReceiveThread, self).__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            self.receive_message()

    def receive_message(self):
        message = self.client_socket.recv(1024)
        message = message.decode('utf-8', 'ignore')

        # print(message)
        self.signal.emit(message)

    def receive_clientOnline(self):
        message = self.client_socket.recv(1024)
        message = message.decode('utf-8', 'ignore')


class Client(object):
    buttonList = []
    buttonRoomList = []
    send_message_clientName = "client_xyz-"
    nickname = ""
    fileName = ""

    def buttonListi(self):
        btn = QtWidgets.QPushButton()
        btn.setMinimumSize(150, 30)
        btn.setVisible(False)

        btn2 = QtWidgets.QPushButton()
        btn2.setMinimumSize(150, 30)
        btn2.setVisible(False)
        btn3 = QtWidgets.QPushButton()
        btn3.setMinimumSize(150, 30)
        btn3.setVisible(False)
        btn4 = QtWidgets.QPushButton()
        btn4.setMinimumSize(150, 30)
        btn4.setVisible(False)
        btn5 = QtWidgets.QPushButton()
        btn5.setMinimumSize(150, 30)
        btn5.setVisible(False)
        self.buttonList.append(btn)
        self.buttonList.append(btn2)
        self.buttonList.append(btn3)
        self.buttonList.append(btn4)
        self.buttonList.append(btn5)

    def buttonRoomListi(self):
        btn6 = QtWidgets.QPushButton()
        btn6.setMinimumSize(150, 30)
        btn6.setVisible(False)

        btn7 = QtWidgets.QPushButton()
        btn7.setMinimumSize(150, 30)
        btn7.setVisible(False)
        btn8 = QtWidgets.QPushButton()
        btn8.setMinimumSize(150, 30)
        btn8.setVisible(False)
        btn9 = QtWidgets.QPushButton()
        btn9.setMinimumSize(150, 30)
        btn9.setVisible(False)
        btn10 = QtWidgets.QPushButton()
        btn10.setMinimumSize(150, 30)
        btn10.setVisible(False)
        self.buttonRoomList.append(btn6)
        self.buttonRoomList.append(btn7)
        self.buttonRoomList.append(btn8)
        self.buttonRoomList.append(btn9)
        self.buttonRoomList.append(btn10)

    def __init__(self):
        self.messages = []
        self.takedClints = []
        self.buttonListi()
        self.buttonRoomListi()
        self.mainWindow = QtWidgets.QMainWindow()
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor('red'))

        # add widgets to the application window
        self.connectWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)
        self.privateChatWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatRoomWidget = QtWidgets.QWidget(self.mainWindow)
        self.fileDir = QFileDialog(self.mainWindow)

        self.connect_ui = connect_ui.Ui_Form()
        self.connect_ui.setupUi(self.connectWidget)
        self.connect_ui.pushButton.clicked.connect(self.btn_connect_clicked)

        self.chatRoomWidget.setHidden(True)
        self.chat_room_ui = Ui_Form_chatRoom()
        self.chat_room_ui.setupUi(self.chatRoomWidget)
        self.chat_room_ui.pushButton.clicked.connect(self.send_message_ChatRoom)
        self.chat_room_ui.turnBackButton.clicked.connect(self.turnBackMessage)
        self.emojiler_chatRoom()

        self.chatWidget.setHidden(True)
        self.chat_ui = client_ui.Ui_Form()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.pushButton.clicked.connect(self.send_message)
        self.chat_ui.pushButtonSetRoom.clicked.connect(self.createRoom)

        self.emojilerChat()

        self.privateChatWidget.setHidden(True)
        self.chat_ui_private = private_ui.Ui_Form_Private()
        self.chat_ui_private.setupUi(self.privateChatWidget)
        self.chat_ui_private.pushButton.clicked.connect(self.send_message_private2)
        self.chat_ui_private.pushButtonSelect.clicked.connect(self.selectFile)
        self.chat_ui_private.pushButtonSend.clicked.connect(self.sendFile)
        self.chat_ui_private.turnBackButton.clicked.connect(self.turnBackButtonsAction)

        self.chat_ui.label1.setPalette(palette)
        self.chat_ui.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.emojiler_private()

        self.mainWindow.setGeometry(QtCore.QRect(1080, 20, 800, 800))
        self.mainWindow.setWindowTitle("AmazonClient1")
        self.mainWindow.show()

        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def turnBackButtonsAction(self):
        self.connectWidget.setHidden(True)
        self.chatWidget.setVisible(True)
        self.privateChatWidget.setHidden(True)
        message = "private_out_talking"
        self.tcp_client.send(message.encode('utf-8'))

    def createRoom(self):
        chatName = self.chat_ui.textEditChatName.toPlainText()
        chatPassword = self.chat_ui.textEditChatPass.toPlainText()

        if len(chatName) == 0:
            chatName = "unknown"

        if len(chatPassword) == 0:
            chatPassword = "0000"

        message = "createroom_xyz-" + chatName + "-" + chatPassword
        self.tcp_client.send(message.encode('utf-8'))
        self.chat_ui.textEditChatName.clear()
        self.chat_ui.textEditChatPass.clear()

    def emojiTextChatRoom(self, action):

        self.chat_room_ui.textEdit.append(action)

    def emojiTextChat(self, action):

        self.chat_ui.textEdit.append(action)

    def emojiText(self, action):
        self.chat_ui_private.textEdit.append(action)

    def selectFile(self):
        # self.fileDir.setVisible(True)
        self.fileName = self.fileDir.getOpenFileName(self.fileDir, 'Open file', '.')
        # self.myTextBox.setText(fileName)
        try:
            self.fileName = str(self.fileName)
            self.fileName = self.fileName.split(",")
            self.fileName = self.fileName[0][2:len(self.fileName[0]) - 1]
            print(self.fileName)

        except Exception:
            print(Exception)
        # self.fileDir.setHidden(True)

    def sendFile(self):
      if (self.fileName != ""):
        sentence = "SEND"

        self.tcp_client.send(sentence.encode('utf-8'))
        print(self.fileName)
        self.tcp_client.send(self.fileName.encode('utf-8'))
        time.sleep(1)

        print('Sending file to server...')
        message = 'BEGIN'

        self.tcp_client.send(message.encode('utf-8'))
        time.sleep(1)
        with open(self.fileName, 'rb') as f:
            while True:

                data = f.read(2048)
                print("data= ", data.decode(encoding='utf-8', errors='ignore'))
                self.tcp_client.send(data)

                if not data:
                    print('Breaking from sending data')
                    break
            time.sleep(1)
            message = 'ENDED'
            self.tcp_client.send(message.encode('utf-8'))  # I used the same size of the BEGIN token
            f.close()

    def btn_connect_clicked(self):
        host = self.connect_ui.hostTextEdit.toPlainText()
        port = self.connect_ui.portTextEdit.toPlainText()
        self.nickname = self.connect_ui.nameTextEdit.toPlainText()

        if len(host) == 0:
            host = "18.219.228.137"#use amazon web server public ip //for server must use server private Ip
             #if you dont know cmd --> ipconfig  --> IPV4 value is your private Ip

        if len(port) == 0:
            port = 5555
        else:
            try:
                port = int(port)
            except Exception as e:
                error = "Invalid port number \n'{}'".format(str(e))
                print("[INFO]", error)
                self.show_error("Port Number Error", error)

        if len(self.nickname) < 1:
            self.nickname = socket.gethostname()

        self.nickname = self.nickname + "_" + str(random.randint(1, port))

        if self.connect(host, port, self.nickname):
            self.connectWidget.setHidden(True)
            self.chatWidget.setVisible(True)

            self.mainWindow.setWindowTitle(str(self.nickname))
            self.recv_thread = ReceiveThread(self.tcp_client)
            self.recv_thread.signal.connect(self.show_message)
            self.recv_thread.start()
            print("[INFO] recv thread started")

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def show_message(self, message):
        print("gelen mesaj:", message)

        if message[0:2] == '+ ':
            i = 0
            print(message)

            print("vbox2", self.chat_ui.vbox2.isEmpty())

            self.buttonList.clear()
            self.clearLayout(self.chat_ui.vbox)

            self.buttonListi()

            self.chat_ui.textBrowser2.clear()

            message = str(message).split("*")
            for i in range(len(message) - 1):
                strmessage = str(message[i])
                messageNickAndPorts = message[i].split("-")
                nicks = messageNickAndPorts[0][2:]
                ports = messageNickAndPorts[1]
                self.buttonList[i].setVisible(True)
                self.buttonList[i].setText(nicks)
                self.buttonList[i].clicked.connect(partial(self.printName, action=strmessage))
                self.chat_ui.textBrowser2.append(message[i])
                self.chat_ui.vbox.addWidget(self.buttonList[i])

                print("vbox1", self.chat_ui.vbox.isEmpty(), "  i=", i)



        elif message[0:4] == '^+^ ':
            i = 0
            print(message)
            print("vbox2", self.chat_ui.vbox.isEmpty())

            self.buttonRoomList.clear()

            self.clearLayout(self.chat_ui.vbox2)
            self.buttonRoomListi()
            self.chat_ui.textBrowser2.clear()
            # self.chat_ui.vbox
            message = str(message).split("*")
            print("sayısı=", (len(message) - 1))
            for i in range(len(message) - 1):
                strmessage = str(message[i])
                messageNickAndPorts = message[i].split("-")
                name = messageNickAndPorts[1]
                password = messageNickAndPorts[2]
                print("gelen oda ismi=", name, "oda şifresi=", password)
                self.buttonRoomList[i].setVisible(True)
                self.buttonRoomList[i].setText(name)
                self.buttonRoomList[i].clicked.connect(partial(self.joinRoom, action=strmessage))
                self.chat_ui.textBrowser2.append(message[i])

                self.chat_ui.vbox2.addWidget(self.buttonRoomList[i])
                print("eklendi")

                print("vbox2", self.chat_ui.vbox2.isEmpty(), "  i=", i)



        elif message == "question_xyz":
            print("istek geldi")
            self.showdialog()
        elif message == "youJoinRoom":
            self.connectWidget.setHidden(True)
            self.chatWidget.setHidden(True)
            self.privateChatWidget.setHidden(True)
            name = self.chat_ui.textEditChatName.toPlainText()
            print("name is=", name)
            self.mainWindow.setWindowTitle(name)
            self.chatRoomWidget.setVisible(True)
        elif message == "turnBackSignal*":
            self.chat_room_ui.textBrowser.clear()
            self.connectWidget.setHidden(True)
            self.chatWidget.setVisible(True)
            self.mainWindow.setWindowTitle(self.nickname)
            self.privateChatWidget.setHidden(True)
            self.chatRoomWidget.setHidden(True)

        elif message == "not_accept_xyz":
            self.showdialogNotAccept()
        elif message == "private_out_talking":
            print("private_out_talkingi algıladı")
            self.showdialogTalkingOut()


        elif message == "GET":

            print('Get içine girdi dosya adı yollanması bekleniyor')
            yenigelen = self.tcp_client.recv(1024)
            file_names = yenigelen.decode('utf-8', 'ignore')
            print("serverdam gelenler =", yenigelen.decode('utf-8', 'ignore'))
            print("filename= ", file_names)
            file_names = "client_" + str(file_names)
            print("file name altı")
            f = open(file_names, "wb")
            print('Receiving file from client..')

            while True:
                try:
                    data = self.tcp_client.recv(2048)
                    print('sonraki gelen data decode=', data.decode('utf-8', 'ignore'))
                    if data.decode('utf-8', 'ignore') == 'BEGIN':
                        print("begine girdi")
                        continue
                    elif data.decode('utf-8', 'ignore') == 'ENDED':
                        print('Breaking from file write')
                        break
                    elif not data:
                        print('data yok')
                        break
                    else:

                        f.write(data)
                        print('Wrote to file', data.decode('utf-8', 'ignore'))
                    print("data bekleniyor")

                except Exception:

                    print(Exception.args)

            f.close()
            print("burada bitiyor")
            print('Done receiving file')

        elif (message[0:12] == "private_xyz*"):
            self.chat_ui_private.textBrowser.append(message[12:])
        elif (message[0:20] == "chatroomMessage_xyz*"):
            print("chatroomMEssage konumuna girdi:")
            self.chat_room_ui.textBrowser.append(message[20:])

        elif message == "match_xyz":
            self.connectWidget.setHidden(True)
            self.chatWidget.setHidden(True)
            self.privateChatWidget.setVisible(True)
        elif message == "joinRoom_xyz":
            print("buraya girdi")
        else:
            self.chat_ui.textBrowser.append(message)

    def printName(self, action):
        messageNickAndPorts = action.split("-")
        nicks = messageNickAndPorts[0][2:]
        ports = messageNickAndPorts[1]
        send_message_clientName = "client_xyz-" + str(nicks)
        print(send_message_clientName == ("client_xyz-" + str(self.nickname)), "send message name=",
              send_message_clientName
              , "client name =", "client_xyz_+ " + str(self.nickname))
        if send_message_clientName == ("client_xyz-" + str(self.nickname)):
            print("say noo")
        else:
            print(send_message_clientName)
            self.send_message_private(send_message_clientName)

    def joinRoom(self, action):
        message = "join_createdroom_xyz" + action
        self.tcp_client.send(message.encode('utf-8'))

        print("Action=", action)

    def connect(self, host, port, nickname):

        try:
            self.tcp_client.connect((host, port))
            self.tcp_client.send(nickname.encode())

            print("[INFO] Connected to server")

            return True
        except Exception as e:
            error = "Unable to connect to server \n'{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Connection Error", error)
            self.connect_ui.hostTextEdit.clear()
            self.connect_ui.portTextEdit.clear()

            return False

    def send_message(self):
        message = self.chat_ui.textEdit.toPlainText()
        self.chat_ui.textBrowser.append("Me: " + message)

        print("sent: " + message)

        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        self.chat_ui.textEdit.clear()

    def send_message_ChatRoom(self):
        message = self.chat_room_ui.textEdit.toPlainText()

        self.chat_room_ui.textBrowser.append("Me: " + message)
        messager = "chatroomMessage_xyz*" + self.nickname + ":" + message
        print("sent: " + message)

        try:
            self.tcp_client.send(messager.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        self.chat_room_ui.textEdit.clear()

    def send_message_private2(self):
        messager = self.chat_ui_private.textEdit.toPlainText()
        self.chat_ui_private.textBrowser.append("Me: " + messager)
        messager = "private_xyz*" + messager

        print("sent: " + messager)

        try:
            self.tcp_client.send(messager.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        self.chat_ui_private.textEdit.clear()

    def send_message_private(self, sender):
        try:
            self.tcp_client.send(sender.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)

    def show_error(self, error_type, message):
        errorDialog = QtWidgets.QMessageBox()
        errorDialog.setText(message)
        errorDialog.setWindowTitle(error_type)
        errorDialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        errorDialog.exec_()

    def showdialogTalkingOut(self):

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msgt.setWindowTitle("Bilgilendirme")
        self.msgt.setDetailedText("")
        self.msg.setText("Karşı Taraf Konuşmadan ayrıldı ")
        self.msg.setInformativeText("Ok tuşuna basarak ana chat menüye dönebilirsiniz")
        print("msgBtnTalkingOuta girdi")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.buttonClicked.connect(self.msgbtnTalking)
        retval = self.msg.exec_()
        print("value of pressed message box button:", retval)

    def msgbtnTalking(self):
        print("msgBtnTalkingOuta girdi")
        self.connectWidget.setHidden(True)
        self.chatWidget.setVisible(True)
        self.privateChatWidget.setHidden(True)

    def showdialog(self):

        self.msgt = QMessageBox()
        self.msgt.setIcon(QMessageBox.Information)

        self.msgt.setText("This is a message box")
        self.msgt.setInformativeText("This is additional information")
        self.msgt.setWindowTitle("MessageBox demo")
        self.msgt.setDetailedText("The details are as follows:")
        self.msgt.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msgt.buttonClicked.connect(self.msgbtn)

        retval = self.msgt.exec_()
        print("value of pressed message box button:", retval)

    def msgbtn(self, i):
        print("Button pressed is:", i.text())
        if (i.text() == "OK"):
            self.send_message_private("accept_xyz")
            self.connectWidget.setHidden(True)
            self.chatWidget.setHidden(True)
            self.privateChatWidget.setVisible(True)
            # yeniSayfaKurulacakBurada
        else:
            self.send_message_private("not_accept_xyz")
            # devamke  sadece diğer tarafa bilgilendirme mesaji

    def showdialogNotAccept(self):
        self.msgr = QMessageBox()
        self.msgr.setIcon(QMessageBox.Information)

        self.msgr.setText("İsteğiniz Kabul edilmedi")
        self.msgr.setInformativeText("İsteğiniz gönderdiğiniz kişi tarafından kabul edilmedi")
        self.msgr.setWindowTitle("Bilgilendirme")
        self.msgr.setDetailedText(
            "İsteğiniz gönderdiğiniz kişi tarafından kabul edilmedi tekrar göndermek isterseniz tekrar tıklayabilirsiniz")
        self.msgr.setStandardButtons(QMessageBox.Ok)

        retval = self.msgr.exec_()
        print("value of pressed message box button:", retval)

    def turnBackMessage(self):
        message = "chatroom_turnback*"
        self.tcp_client.send(message.encode('utf-8'))

    def emojilerChat(self):
        self.chat_ui.pushButtonSmail.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonSmail.text()))
        self.chat_ui.pushButtonHeartFace.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonHeartFace.text()))
        self.chat_ui.pushButtonTaxi.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonTaxi.text()))
        # Layout2
        self.chat_ui.pushButtonGlassFace.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonGlassFace.text()))
        self.chat_ui.pushButtonStarFace.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonStarFace.text()))
        self.chat_ui.pushButtonRoket.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonRoket.text()))
        # Layout3
        self.chat_ui.pushButtonGozK.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonGozK.text()))
        self.chat_ui.pushButtonTongue.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonTongue.text()))
        self.chat_ui.pushButtonHandS.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonHandS.text()))
        self.chat_ui.pushButtonHandSOK.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonHandSOK.text()))
        self.chat_ui.pushButtonHandSW.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonHandSW.text()))
        self.chat_ui.pushButtonHandSa.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonHandSa.text()))
        self.chat_ui.pushButtonHeartB.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonHeartB.text()))
        self.chat_ui.pushButtonHeartBr.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonHeartBr.text()))
        self.chat_ui.pushButtonHug.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonHug.text()))
        self.chat_ui.pushButtonStrong.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonStrong.text()))
        self.chat_ui.pushButtonComp.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonComp.text()))
        self.chat_ui.pushButtonAngle.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonAngle.text()))
        self.chat_ui.pushButtonRose.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonRose.text()))
        self.chat_ui.pushButtonHmm.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonHmm.text()))
        self.chat_ui.pushButtonFire.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonFire.text()))
        self.chat_ui.pushButtonHan.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonHan.text()))
        self.chat_ui.pushButtonGa.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonGa.text()))
        self.chat_ui.pushButtonSad.clicked.connect(
            partial(self.emojiTextChat, action=self.chat_ui.pushButtonSad.text()))

    def emojiler_private(self):
        # Layout1
        self.chat_ui_private.pushButtonSmail.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonSmail.text()))
        self.chat_ui_private.pushButtonHeartFace.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonHeartFace.text()))
        self.chat_ui_private.pushButtonTaxi.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonTaxi.text()))
        # Layout2
        self.chat_ui_private.pushButtonGlassFace.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonGlassFace.text()))
        self.chat_ui_private.pushButtonStarFace.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonStarFace.text()))
        self.chat_ui_private.pushButtonRoket.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonRoket.text()))
        # Layout3
        self.chat_ui_private.pushButtonGozK.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonGozK.text()))
        self.chat_ui_private.pushButtonTongue.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonTongue.text()))
        self.chat_ui_private.pushButtonHandS.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonHandS.text()))
        self.chat_ui_private.pushButtonHandSOK.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonHandSOK.text()))
        self.chat_ui_private.pushButtonHandSW.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonHandSW.text()))
        self.chat_ui_private.pushButtonHandSa.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonHandSa.text()))
        self.chat_ui_private.pushButtonHeartB.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonHeartB.text()))
        self.chat_ui_private.pushButtonHeartBr.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonHeartBr.text()))
        self.chat_ui_private.pushButtonHug.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonHug.text()))
        self.chat_ui_private.pushButtonStrong.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonStrong.text()))
        self.chat_ui_private.pushButtonComp.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonComp.text()))
        self.chat_ui_private.pushButtonAngle.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonAngle.text()))
        self.chat_ui_private.pushButtonRose.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonRose.text()))
        self.chat_ui_private.pushButtonHmm.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonHmm.text()))
        self.chat_ui_private.pushButtonFire.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonFire.text()))
        self.chat_ui_private.pushButtonHan.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonHan.text()))
        self.chat_ui_private.pushButtonGa.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonGa.text()))
        self.chat_ui_private.pushButtonSad.clicked.connect(
            partial(self.emojiText, action=self.chat_ui_private.pushButtonSad.text()))

    def emojiler_chatRoom(self):

        # Layout1
        self.chat_room_ui.pushButtonSmail.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonSmail.text()))
        self.chat_room_ui.pushButtonHeartFace.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonHeartFace.text()))
        self.chat_room_ui.pushButtonTaxi.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonTaxi.text()))
        # Layout2
        self.chat_room_ui.pushButtonGlassFace.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonGlassFace.text()))
        self.chat_room_ui.pushButtonStarFace.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonStarFace.text()))
        self.chat_room_ui.pushButtonRoket.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonRoket.text()))
        # Layout3
        self.chat_room_ui.pushButtonGozK.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonGozK.text()))
        self.chat_room_ui.pushButtonTongue.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonTongue.text()))
        self.chat_room_ui.pushButtonHandS.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonHandS.text()))
        self.chat_room_ui.pushButtonHandSOK.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonHandSOK.text()))
        self.chat_room_ui.pushButtonHandSW.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonHandSW.text()))
        self.chat_room_ui.pushButtonHandSa.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonHandSa.text()))
        self.chat_room_ui.pushButtonHeartB.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonHeartB.text()))
        self.chat_room_ui.pushButtonHeartBr.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonHeartBr.text()))
        self.chat_room_ui.pushButtonHug.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonHug.text()))
        self.chat_room_ui.pushButtonStrong.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonStrong.text()))
        self.chat_room_ui.pushButtonComp.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonComp.text()))
        self.chat_room_ui.pushButtonAngle.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonAngle.text()))
        self.chat_room_ui.pushButtonRose.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonRose.text()))
        self.chat_room_ui.pushButtonHmm.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonHmm.text()))
        self.chat_room_ui.pushButtonFire.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonFire.text()))
        self.chat_room_ui.pushButtonHan.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonHan.text()))
        self.chat_room_ui.pushButtonGa.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonGa.text()))
        self.chat_room_ui.pushButtonSad.clicked.connect(
            partial(self.emojiTextChatRoom, action=self.chat_room_ui.pushButtonSad.text()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    sys.exit(app.exec())