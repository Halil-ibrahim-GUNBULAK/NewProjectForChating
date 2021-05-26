from functools import partial

from PyQt5 import QtCore, QtWidgets
import client_ui
import connect_ui
import time
import sys
import socket
import random

from PyQt5.QtWidgets import QMessageBox


class ReceiveThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)
    signal2 = QtCore.pyqtSignal(str)
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




        self.connect_ui = connect_ui.Ui_Form()
        self.connect_ui.setupUi(self.connectWidget)
        self.connect_ui.pushButton.clicked.connect(self.btn_connect_clicked)

        self.chatWidget.setHidden(True)
        self.chat_ui = client_ui.Ui_Form()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.pushButton.clicked.connect(self.send_message)



        self.mainWindow.setGeometry(QtCore.QRect(1080, 20, 800, 800))
        self.mainWindow.show()

        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
          #yeniSayfaKurulacakBurada
        else:
          self.send_message_private("not_accept_xyz")
          #devamke  sadece diğer tarafa bilgilendirme mesaji
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    sys.exit(app.exec())