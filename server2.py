import socket
import threading

class Server(object):
    istekListesi=[]
    def __init__(self, hostname, port):
        self.clients = {}

        # create server socket
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # start server
        self.tcp_server.bind(("192.168.2.86", port))
        self.tcp_server.listen(5)

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
                elif message=="accept_xyz":
                    print("kabul edildi mesaji servera ulaştı")
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

if __name__ == "__main__":
    port = 5555
    hostname = "192.168.2.86"

    chat_server = Server(hostname, port)