__author__ = 'RetR0'

import threading
import socket


print ("\n")
print (" ______________________________________________")
print ("************************************************")
print ("""  █████████                           █████████ 
 ███░░░░░███                         ███░░░░░███
░███    ░███  ████████   ████████   ███     ░░░ 
░███████████ ░░███░░███ ░░███░░███ ░███         
░███░░░░░███  ░███ ░███  ░███ ░███ ░███         
░███    ░███  ░███ ░███  ░███ ░███ ░░███     ███
█████   █████ ████ █████ ████ █████ ░░█████████ 
░░░░░   ░░░░░ ░░░░ ░░░░░ ░░░░ ░░░░░   ░░░░░░░░░  
                                                """)
print ("************************************************")
print ("        Annonymous TCP Chat x RSA 3072 (Server)")
print (" ----------------------------------------------\n")

host = input ("Enter the IP of the host server (or leave empty for localhost) :")

if len(host) == 0:
    host = '127.0.0.1' 

port = int(input ("Enter the listening port of the host server :"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients_list = []

def broadcast(message):
    print (message)
    for client in clients_list:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(3072)
            print ("\nEncrypted message :\n")
            broadcast(message)
            print ("\nbroadcoasted !!!\n----------------")
        except:
            index = clients_list.index(client)
            clients_list.remove(client)
            client.close
            break

def main():
    while True:
        client, address = server.accept()
        print (f"\nNew user connected at {address}")
        clients_list.append(client)
        print (clients_list)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print (f'\nServer is running on {host} using port {port}...')

main()
