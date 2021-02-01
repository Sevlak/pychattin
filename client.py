import socket
import threading
import os

class TCPChatClient:
    """
    Creates a TCP chat client (duh).

    :param str ip: The IP you want to connect to.
    :param int port: The port you want to connect to.

    """
    def chat(self):
        """
        Handles the messages from the server.
        """
        while True:
            try:
                server_message = self.connection.recv(2048).decode("utf-8")
                print(server_message)
            except:
                print("An error has ocurred")
                self.connection.close()
                break

    def send_message(self):
        """
        Handles the messages sent to the server.
        """
        while True:
            user_message = f'{self.nickname}: {input("")}'
            self.connection.send(bytes(user_message, "utf-8"))
            if (user_message == f"{self.nickname}: /q"):
                os._exit(1)

    def __init__(self, ip: str, port: int):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
        self.nickname = input("Nickname: ")

        recv_thread = threading.Thread(name='receiver',target=self.chat)
        recv_thread.start()
        send_thread = threading.Thread(name='messager', target=self.send_message)
        send_thread.start()






