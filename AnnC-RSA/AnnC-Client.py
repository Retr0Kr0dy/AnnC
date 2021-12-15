__author__ = 'RetR0'

import threading
import socket

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

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

private_key_file = input ("Import a private key file to use :")
try:
    with open (private_key_file, 'rb') as f_keyfile:
        private_key = serialization.load_pem_private_key(
            f_keyfile.read(),
            password=None,
            backend=default_backend()
        )
    print ("---Target locked---")
except:
    print ("Error : Key file not found")

public_key_file = input ("Import a public key file to use :")
with open(public_key_file, "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )
print ("---Target locked---")

nickname = (input ("\nChoose a nickname :") + " : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect ((host, port))

def main():
    while True:
        try:
            message = client.recv(8192)            
            decrypt_message (message)
            print (original_message)
        except:
            print("An error Occurred !")
            client.close()
            break

def send_message():
    while True:
        encrypt_message()
        message = encrypted_message
        client.send(message)

def encrypt_message():
    global message
    message = input("")
    message = (nickname + message).encode('utf-8')

    def encryption():
        global encrypted
        encrypted = public_key.encrypt(message,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )        
    encryption()
    global encrypted_message
    encrypted_message = encrypted

def decrypt_message(message):
    print ("\nRecieved message :")

    def decryption():
        global original_message
        original_message = private_key.decrypt(message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    
    decryption()

main_thread = threading.Thread(target=main)
main_thread.start()

send_message_thread = threading.Thread(target=send_message)
send_message_thread.start()
