'Chat Room Connection - Client-To-Client'
import threading
import socket
host = '192.168.6.103'
port = 5990
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []


def broadcast(message):   
    for client in clients:
        client.send(message)

# Function to handle clients'connections


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break
# Main function to receive the clients connection


z