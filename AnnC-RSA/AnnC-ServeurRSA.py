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
# names_list = []

def broadcast(message):
    for client in clients_list:
        client.send(message)
        print (message)

def handle(client):
    while True:
        try:
            message = client.recv(8192)
            print ("msg")
            print (message)
            print ("yes it work now got to encode")
            client.send(message)
            print (clients_list)
            print (client)	
            message = message.encode('utf-8')
            print ("encoded")
            print (message)
            for client in clients_list:
                client.send(message)
            # broadcast(str_msg)
            print ("broadcoast")
        except:
            index = clients_list.index(client)
            clients_list.remove(client)
            client.close
            # nickname = names_list[index]
            # names_list.remove(nickname)
            # broadcast(f'{nickname} left the chat!'.encode('ascii'))
            break

def main():
    while True:
        client, address = server.accept()
        print (f"\nNew user connected at {address}")

        # client.send('NICK'.encode('ascii'))
        # nickname = client.recv(1024).decode('ascii')
        # names_list.append(nickname)
        clients_list.append(client)
        print (clients_list)
        # print (f'\n{address} as set his nickname to {nickname}')

        # broadcast(f'{nickname} joined the chat !'.encode('ascii'))
        # client.send('Connected to the server !'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print (f'\nServer is running on {host} using port {port}...')

main()
