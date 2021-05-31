from functools import partial

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import client_ui
import connect_ui
import private_ui
import time
import sys
import socket
import random

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
        message = message.decode()

        #print(message)
        self.signal.emit(message)

    def receive_clientOnline(self):
        message = self.client_socket.recv(1024)
        message = message.decode()

class Client(object):
    buttonList=[]
    send_message_clientName="client_xyz-"
    nickname = ""
    fileName=""
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
    def __init__(self):
        self.messages = []
        self.takedClints=[]
        self.mainWindow = QtWidgets.QMainWindow()
        self.buttonListi()

        # add widgets to the application window
        self.connectWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)
        self.privateChatWidget= QtWidgets.QWidget(self.mainWindow)
        self.fileDir=QFileDialog(self.mainWindow)




        self.connect_ui = connect_ui.Ui_Form()
        self.connect_ui.setupUi(self.connectWidget)
        self.connect_ui.pushButton.clicked.connect(self.btn_connect_clicked)

        self.chatWidget.setHidden(True)
        self.chat_ui = client_ui.Ui_Form()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.pushButton.clicked.connect(self.send_message)

        self.privateChatWidget.setHidden(True)
        self.chat_ui_private = private_ui.Ui_Form_Private()
        self.chat_ui_private.setupUi(self.privateChatWidget)
        self.chat_ui_private.pushButton.clicked.connect(self.send_message_private2)
        self.chat_ui_private.pushButtonSelect.clicked.connect(self.selectFile)
        self.chat_ui_private.pushButtonSend.clicked.connect(self.sendFile)
        self.mainWindow.setGeometry(QtCore.QRect(1080, 20, 800, 800))
        self.mainWindow.setWindowTitle("Client3")
        self.mainWindow.show()

        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def selectFile(self):
            #self.fileDir.setVisible(True)
            self.fileName =self.fileDir.getOpenFileName(self.fileDir,'Open file','.')
            #self.myTextBox.setText(fileName)
            try:
              self.fileName=str(self.fileName)
              self.fileName=self.fileName.split(",")
              self.fileName=self.fileName[0][2:len(self.fileName[0])-1]
              print(self.fileName)

            except Exception:
                print(Exception)
            #self.fileDir.setHidden(True)
    def sendFile(self):
            sentence = "SEND"

            self.tcp_client.send(sentence.encode('utf-8'))
            print(self.fileName)
            self.tcp_client.send(self.fileName.encode('utf-8'))

            f = open(self.fileName, "rb")

            print('Sending file to server...')
            message='BEGIN'

            self.tcp_client.send(message.encode('utf-8'))
            time.sleep(1)
            while True:
                data = f.read(1024)
                print('Sending data', data.decode('utf-8'))
                self.tcp_client.send(data)
                print('Sent data', data.decode('utf-8'))
                if not data:
                    print('Breaking from sending data')
                    break
            time.sleep(1)
            message='ENDED'
            self.tcp_client.send(message.encode('utf-8'))  # I used the same size of the BEGIN token
            f.close()


    def btn_connect_clicked(self):
        host = self.connect_ui.hostTextEdit.toPlainText()
        port = self.connect_ui.portTextEdit.toPlainText()
        self.nickname = self.connect_ui.nameTextEdit.toPlainText()

        if len(host) == 0:
            host = "192.168.2.86"

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

        if self.connect(host, port,self.nickname):
            self.connectWidget.setHidden(True)
            self.chatWidget.setVisible(True)

            self.recv_thread = ReceiveThread(self.tcp_client)
            self.recv_thread.signal.connect(self.show_message)
            self.recv_thread.start()
            print("[INFO] recv thread started")

    def clearLayout(self,layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    def show_message(self, message):
        print("gelen mesaj:", message)

        if message[0:2]=='+ ':
            i=0
            print(message)
            print(self.chat_ui.vbox.isEmpty(),"  i=" ,i)
            '''
            while self.chat_ui.vbox.isEmpty()!=True:
                widgetToRemove = self.chat_ui.vbox.itemAt(i).widget()
                self.chat_ui.vbox.removeWidget(widgetToRemove)
                widgetToRemove.setParent(None)
                i+=1
                print("Yapildi ")
            '''
            self.buttonList.clear()
            self.clearLayout(self.chat_ui.vbox)
            self.buttonListi()
            self.chat_ui.textBrowser2.clear()
            #self.chat_ui.vbox
            message=str(message).split("*")
            for i in range(len(message)-1):
                strmessage=str(message[i])
                messageNickAndPorts = message[i].split("-")
                nicks = messageNickAndPorts[0][2:]
                ports = messageNickAndPorts[1]
                self.buttonList[i].setVisible(True)
                self.buttonList[i].setText(nicks)
                self.buttonList[i].clicked.connect(partial(self.printName,action=strmessage))
                self.chat_ui.textBrowser2.append(message[i])
                self.chat_ui.vbox.addWidget(self.buttonList[i])


            print("bitti")
        elif message=="question_xyz":
          print("istek geldi")
          self.showdialog()
        elif message=="GET":

            print('Get içine girdi dosya adı yollanması bekleniyor')
            yenigelen =self.tcp_client.recv(1024)
            file_names = yenigelen.decode('utf-8')
            print("serverdam gelenler =",yenigelen.decode('utf-8'))
            print("filename= ", file_names)
            file_names ="client.txt"
            print("file name altı")
            f = open(file_names, "wb")
            print('Receiving file from client..')

            while True:
                data =self.tcp_client.recv(1024)
                print('sonraki gelen data decode=', data.decode('utf-8'))
                if data.decode('utf-8') == 'BEGIN':
                    print("begine girdi")
                    continue
                elif data.decode('utf-8') == 'ENDED':
                    print('Breaking from file write')
                    break
                elif not data:
                    print('data yok')
                    break
                else:
                    print('Received: ', data.decode('utf-8'))
                    f.write(data)
                    print('Wrote to file', data.decode('utf-8'))
                print("data bekleniyor")

            f.close()
            print("burada bitiyor")
            print('Done receiving file')

        elif (message[0:12] == "private_xyz*"):
            self.chat_ui_private.textBrowser.append(message[12:])
        elif message == "match_xyz":
            self.connectWidget.setHidden(True)
            self.chatWidget.setHidden(True)
            self.privateChatWidget.setVisible(True)
        else:
            self.chat_ui.textBrowser.append(message)

    def printName(self,action):
        messageNickAndPorts = action.split("-")
        nicks = messageNickAndPorts[0][2:]
        ports = messageNickAndPorts[1]
        send_message_clientName = "client_xyz-" + str(nicks)
        print(send_message_clientName == ("client_xyz-"+str(self.nickname)),"send message name=",send_message_clientName
              ,"client name =", "client_xyz_+ "+str(self.nickname))
        if send_message_clientName == ("client_xyz-"+str(self.nickname)):
                 print("say noo")
        else:
           print(send_message_clientName)
           self.send_message_private(send_message_clientName)



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

    def send_message_private2(self):
        messager = self.chat_ui_private.textEdit.toPlainText()
        self.chat_ui_private.textBrowser.append("Me: " + messager)
        messager="private_xyz*"+messager

        print("sent: " + messager)

        try:
            self.tcp_client.send(messager.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        self.chat_ui_private.textEdit.clear()

    def send_message_private(self,sender):
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

    def showdialog(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)

        self.msg.setText("This is a message box")
        self.msg.setInformativeText("This is additional information")
        self.msg.setWindowTitle("MessageBox demo")
        self.msg.setDetailedText("The details are as follows:")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.buttonClicked.connect(self.msgbtn)

        retval = self.msg.exec_()
        print( "value of pressed message box button:", retval)

    def msgbtn(self,i):
        print ("Button pressed is:", i.text())
        if(i.text()=="OK"):
          self.send_message_private("accept_xyz")
          self.connectWidget.setHidden(True)
          self.chatWidget.setHidden(True)
          self.privateChatWidget.setVisible(True)
          #yeniSayfaKurulacakBurada
        else:
          self.send_message_private("not_accept_xyz")
          #devamke  sadece diğer tarafa bilgilendirme mesaji
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    sys.exit(app.exec())