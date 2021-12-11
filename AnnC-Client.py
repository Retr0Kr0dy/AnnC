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
print ("        Annonymous TCP Chat x RSA 3072 (Client)")
print (" ----------------------------------------------\n")


host = input ("Enter the IP of the host server :")
port = int(input ("Enter the listening port of the host server :"))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect ((host, port))

nickname = input ("Choose a nickname :")

def main():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error Occurred !")
            client.close()
            break

def send_message():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

main_thread = threading.Thread(target=main)
main_thread.start()

send_message_thread = threading.Thread(target=send_message)
send_message_thread.start()
