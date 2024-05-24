import rsa
import pandas as pd
import base64
from datetime import datetime

# Inicializar: Llave privada

def get_key(path):
    with open(path, mode = "rb") as privatefile:
        keydata = privatefile.read()
    private_key = rsa.PrivateKey.load_pkcs1(keydata)
    return private_key

# Desencriptar: Elemento
""" def decrypt_element(element, path):
    private_key = get_key(path)
    decrypted = rsa.decrypt(base64.b64decode(element), private_key).decode('utf-8')
    try:
        return datetime.strptime(decrypted, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return decrypted """

def decrypt_element(element, path):
    private_key = get_key(path)
    try:
        decrypted = rsa.decrypt(base64.b64decode(element), private_key).decode('utf-8')
    except rsa.pkcs1.DecryptionError:
        return "ErrorLlaveIncorrecta"
    try:
        return datetime.strptime(decrypted, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return decrypted