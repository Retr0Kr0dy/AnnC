# AnnC

AnnC is an annonymous (temp user) TCP chat using python encrypted using RSA 3072

## Requirements : 

 - [Ptyhon 3.9](https://www.python.org/downloads/)
 
 - [cryptography lib](https://pypi.org/project/cryptography/)

## Usage :

### Server


Server execute the [AnnC-Serveur.py](https://github.com/Retr0Kr0dy/AnnC/blob/main/AnnC-RSA/AnnC-Serveur.py) script, set the IP of the interface used for listening, then set the port.


### Client


First, generate RSA keys unsing [AnnC-KeyGen.py](https://github.com/Retr0Kr0dy/AnnC/blob/main/AnnC-RSA/AnnC-KeyGen.py). 


RSA Cipher works by encrypting data with the same size as the key;


```
1024 bits lenght key = 62 bytes max encrypted data

2048 bits lenght key = 190 bytes maw encrypted data

3072 bits lenght key = 318 bytes max encrypted data

4096 bits lenght key = 446 bytes max encrypted data
```


Client execute the [AnnC-Client.py](https://github.com/Retr0Kr0dy/AnnC/blob/main/AnnC-RSA/AnnC-Client.py) script, set the IP to the IP of the server, set the port, then set the path to the private and the public key files, at the end set your nickname.

## How it works

When client chat, he's encrypting the plain text with the RSA public key, 
```
plain text = {nickname} + ":" + {message}
```
then the message is send the server. The server receive it and then broadcast the message to all client in the server clients list.

The server host the TCP connection, but can only see encrypted string.

When client receive the message, string is decrypted and then printed.

This way only client who possesed keys can read messages or send encrypted ones.
