import socket 
import threading

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
connection.bind(('', 7532)) # o socket no endereço especificado

connection.listen(10) #consegue se conectar a no máximo 10 clientes

clients = []
nicknames = []

def broadcast(message: str):
    for client in clients:
        client.send(message)

def client_handler(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg)
        except:
            print("Yeehaw")
            client.close()
            break

def accept_connection():
    while True:
        client_sock, addr = connection.accept()
        print(f"{addr} conectado")

        clients.append(client_sock)
        client_thread = threading.Thread(target=client_handler, args=(client_sock,))
        client_thread.start()

print("Server up")
accept_connection()