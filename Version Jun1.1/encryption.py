import rsa
import pandas as pd
import base64
from datetime import datetime
import math
import Transformations

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
    N = public_key_P.n
    binary_N = bin(N)
    key_bits = len(binary_N) - 2
    element_binary = str(''.join(format(i, '08b') for i in bytearray(element, encoding ='utf-8')))
    element_bits = len(element_binary)
    if element_bits >= 0.8*key_bits:
        splits = math.ceil(element_bits/(key_bits*0.8)) + 1
        intervals = math.floor(len(element)/splits)
        element = Transformations.add_newlines(element, intervals)
        element = element.split('\n')
        encrypted_strings = []
        for string in element:
            encrypted = rsa.encrypt(str(string).encode(), public_key)
            encrypted_strings.append(base64.b64encode(encrypted).decode('utf-8'))
        encrypted = '\n'.join(encrypted_strings)
        return encrypted
    else: encrypted = rsa.encrypt(str(element).encode(), public_key)

    return base64.b64encode(encrypted).decode('utf-8')