import rsa
import pandas as pd
import base64
from datetime import datetime

# Inicializar: Llaves
with open("Keys\public_key_H.txt", mode='rb') as publicfile: # Llave Humanitaria
    keydata_H = publicfile.read()
public_key_H = rsa.PublicKey.load_pkcs1(keydata_H)

with open("Keys\public_key_L.txt", mode='rb') as publicfile: # Llave Legal
    keydata_L = publicfile.read()
public_key_L = rsa.PublicKey.load_pkcs1(keydata_L)

with open("Keys\public_key_P.txt", mode='rb') as publicfile: # Llave Psicosocial
    keydata_P = publicfile.read()
public_key_P = rsa.PublicKey.load_pkcs1(keydata_P)

# Encriptar: Valor
def encrypt_element(element, sheet):
    if sheet == "L":
        public_key = public_key_L
    if sheet == "P":
        public_key = public_key_P
    if sheet == "H":
        public_key = public_key_H
    if isinstance(element, pd.Timestamp):
        element = element.strftime('%Y-%m-%d %H:%M:%S')
    encrypted = rsa.encrypt(str(element).encode(), public_key)
    return base64.b64encode(encrypted).decode('utf-8')