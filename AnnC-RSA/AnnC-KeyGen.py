__author__ = 'RetR0'

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization


key_type = input ("\nSelect a Key size.\n\n\n1 - 1024 bits\n2 - 2048 bits (Recommended)\n3 - 3072 bits\n\n\nPlease enter a number : ")

if key_type == "1":
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=1024,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    key_input = input("\n\nEnter the name of the key file to create : ")
    priv_key_file = (key_input + "_private_key.pem")
    publ_key_file = (key_input + "_public_key.pem")

if key_type == "2":
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    key_input = input("\n\nEnter the name of the key file to create : ")
    priv_key_file = (key_input + "_private_key.pem")
    publ_key_file = (key_input + "_public_key.pem")

if key_type == "3":
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=3072,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    key_input = input("\n\nEnter the name of the key file to create : ")
    priv_key_file = (key_input + "_private_key.pem")
    publ_key_file = (key_input + "_public_key.pem")

try:
    with open (priv_key_file, 'wb') as f_privkeyfile:
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        f_privkeyfile.write(pem)

    with open (publ_key_file, 'wb') as f_publkeyfile:
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        f_publkeyfile.write(pem)
except:
    print ("\n")
    input ("Error : Invalid key name (press enter to continue)")
