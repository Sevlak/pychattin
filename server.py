import socket 
import threading

class TCPChatServer:
    """
    Creates a tcp chat server (duh).

    :param str ip: The server IP address.
    :param int port: The port that the server will listen to.
    """
    def __init__(self, ip: str, port: int):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.bind((ip, port))
        print(self.connection)
        self.connection.listen()
        self.clients = []

    def broadcast(self, message: str):
        """
        Broadcasts the message to all the clients.

        :param str message: The message to be broadcasted.
        """
        for client in self.clients:
            client.send(message)

    def client_handler(self, client):
        """
        Handles the communication with the client. 

        :param socket client: The client socket to be handled.
        """
        while True:
            msg = client.recv(2048)

            if(self.parseQuit(msg.decode('utf-8'))):
                self.clients.remove(client)
                client.close()
                break
            else:
                self.broadcast(msg)

    def parseQuit(self, message: str) -> bool:
        """
        Parses the client message to see if it is a quit command.

        :param str message: The message to be parsed.
        """
        message = message.replace(" ", "").split(":")
        return message[1] == "/q"

    def accept_connections(self):
        """
        Accepts incoming connections to the server. Designates a thread for each client.
        """
        while True:
            client_sock, addr = self.connection.accept()
            print(f"{addr} conectado")

            self.clients.append(client_sock)
            client_thread = threading.Thread(target=self.client_handler, args=(client_sock,))
            client_thread.start()
