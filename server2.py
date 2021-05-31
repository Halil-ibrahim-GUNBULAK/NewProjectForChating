import socket
import threading
import time


class Server(object):

    def __init__(self, hostname, port):
        self.clients = {}
        self.istekListesi = {}
        self.machList={}
        # create server socket
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # start server
        self.tcp_server.bind(("192.168.2.86", port))
        self.tcp_server.listen(8)

        print("[INFO] Server running on {}:{}".format(hostname, port))

        while True:
            connection, address = self.tcp_server.accept()
            nickname = connection.recv(1024)
            nickname = nickname.decode()
            self.clients[nickname] = connection
            self.send_onlineClients()
            # start a thread for the client
            threading.Thread(target=self.receive_message, args=(connection, nickname), daemon=True).start()

            print("[INFO] Connection from {}:{} AKA {}".format(address[0], address[1], nickname))

    def istekListesiTara(self,string):

        for i in range(len(self.istekListesi)):
           print("string değer", string, " self icindeki deger", self.istekListesi[i])
           if self.istekListesi[i] == string:
               return  i

        return -1

    def receive_message(self, connection, nickname):
        print("[INFO] Waiting for messages")
        while True:
            try:
                msg = connection.recv(1024)
                message=msg.decode()

                if(message[0:11]=="client_xyz-"):
                    gelen=str(message).split("-")
                    nicks=gelen[1]
                    print(self.clients[nicks].getpeername())
                    message1="question_xyz"
                    print("gönderilecek diğer tarafa")
                    self.clients[nicks].send(message1.encode())
                    #print(nickname + ": " + msg.decode()+"and  question do u want? :"+nicks)
                    self.istekListesi[len(self.istekListesi)]=nickname
                    print(len(self.istekListesi))
                    self.istekListesi[len(self.istekListesi)]=nicks
                    self.machList[nickname]=nicks
                    self.machList[nicks]=nickname

                elif (message[0:12] == "private_xyz*"):

                    print("gelen mesaj "+message[12:])
                    print("gelen kişi ",nickname," gidecek kişi",self.machList[nickname])
                    giden_mesaj=message[0:12]+nickname+":"+message[12:]
                    self.send_messageAccept(giden_mesaj, self.machList[nickname])

                elif message=="accept_xyz":
                    print("kabul edildi mesaji servera ulaştı")
                    deger=self.istekListesiTara(nickname)
                    if deger==-1:
                        print("böyle bir isim bulunamadı")
                    else:
                        sendNick=self.machList[nickname]
                        messages="match_xyz"
                        self.send_messageAccept(messages,sendNick)

                elif message == "not_accept_xyz":
                    print("kabul edildi mesaji servera ulaştı")
                    deger = self.istekListesiTara(nickname)
                    if deger == -1:
                        print("böyle bir isim bulunamadı")
                    else:
                        sendNick = self.machList[nickname]
                        messages = "not_accept_xyz"
                        self.send_messageAccept(messages, sendNick)


                elif message == "private_out_talking":
                    print("kabul edildi mesaji servera ulaştı")
                    deger = self.istekListesiTara(nickname)
                    if deger == -1:
                        print("böyle bir isim bulunamadı")
                    else:
                        sendNick = self.machList[nickname]
                        messages = "private_out_talking"
                        self.send_messageAccept(messages, sendNick)

                elif message== 'SEND':
                    print('Received SEND command from client. Awaitng filename')
                    client_request = connection.recv(1024)
                    file_name = client_request.decode("utf-8")
                    file_name=str(file_name).split("/")
                    print("filename= ",file_name[len(file_name)-1])
                    file_name="server_"+file_name[len(file_name)-1]
                    print("file name altı")
                    f = open(file_name, "wb")
                    print('Receiving file from client..')

                    while True:
                      try:

                        data = connection.recv(1024)
                        print("buraya kadar geldi")
                        print('data decode=', data.decode('utf-8','ignore'))
                        if data.decode('utf-8','ignore') =='BEGIN':
                            print("begine girdi")
                            continue
                        elif data.decode('utf-8','ignore') =='ENDED':
                            print('Breaking from file write')
                            break
                        elif not data:
                            print('data yok')
                            break
                        else:

                            f.write(data)
                            print('Wrote to file', data.decode('utf-8','ignore'))
                        print("data bekleniyor")

                      except Exception:

                          print(Exception.args)


                    f.close()

                    print('Done receiving file')

                    time.sleep(1)
                    sentence = "GET"
                    gidici = self.machList[nickname]

                    print("self nick name", gidici)
                    time.sleep(3)
                    self.clients[gidici].send(sentence.encode('utf-8'))

                    time.sleep(1)

                    tamam = "tamam client listeni oyalamak için bir yöntem"
                    self.clients[gidici].send(tamam.encode('utf-8'))
                    self.clients[gidici].send(file_name.encode('utf-8'))
                    time.sleep(1)
                    messages = 'BEGIN'
                    self.clients[gidici].send(tamam.encode('utf-8'))
                    self.clients[gidici].send(messages.encode('utf-8'))

                    # I used the same size of the BEGIN token
                    time.sleep(1)
                    counter=0

                    with open(file_name, 'rb') as f:
                        while True:
                           counter+=1

                           data = f.read(2048)

                           print("self.gidici=",self.clients[gidici],"giden mesaj=",data.decode('utf-8','ignore'))

                           self.clients[gidici].sendall(tamam.encode('utf-8'))
                           time.sleep(0.05)
                           self.clients[gidici].sendall(data)
                           time.sleep(0.25)

                           if not data:
                               print('Breaking from sending data')
                               break
                    time.sleep(4)
                    messages = 'ENDED'
                    self.clients[gidici].sendall(messages.encode('utf-8'))




                    print("self.gidici2 son taraf=",self.clients[gidici])
                    f.close()
                    print("olay bitti bile")


                elif message=="not_accept_xyz":
                    print("kabul edilmedi mesaji servera ulaştı")
                else:
                    self.send_message(msg, nickname)
                    print(nickname + ": " + msg.decode())
            except:
                connection.close()

                #remove user from users list
                del(self.clients[nickname])
                self.send_onlineClients()
                break

        print(nickname, " disconnected")


    def send_message(self, message, sender):
        if len(self.clients) > 0:
            for nickname in self.clients:
                if nickname != sender:
                    msg = sender + ": " + message.decode()
                    self.clients[nickname].send(msg.encode())
    def send_onlineClients(self):
        if len(self.clients) > 0:
            msg=""
            for nickname in self.clients:
                    msg = msg+"+ "+nickname+"-"+str(self.clients[nickname].getpeername())+"*"
            print(msg)
            for nickname in self.clients:
                      self.clients[nickname].send(msg.encode())

    def send_messageAccept(self, message, nickname):
                    self.clients[nickname].send(message.encode('utf-8'))



if __name__ == "__main__":
    port = 5555
    hostname = "192.168.2.86"

    chat_server = Server(hostname, port)