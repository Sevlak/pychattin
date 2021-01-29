import socket
import threading

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('127.0.0.1', 7532))
nickname = input("Seu nome: ")

def chat():
    while True:
        try:    
            server_message = connection.recv(2048).decode("utf-8")
            print(server_message)
        except:
            print("Erro ocorreu")
            connection.close()
            break    

def send_message():
    while True:
        user_message = f'{nickname}: {input("")}'
        connection.send(bytes(user_message, "utf-8"))
        
recv_thread = threading.Thread(name='receiver',target=chat)
recv_thread.start()

send_thread = threading.Thread(name='messager', target=send_message)
send_thread.start()


