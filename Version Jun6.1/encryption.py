""" ARCHIVO AUXILIAR: Almacena la función de encriptación RSA de datos."""


# IMPORTAR: LIBRERÍAS
import rsa # Encriptación RSA
import base64 # Codificación
import math # Funciones matemáticas

# IMPORTAR: ARCHIVOS
import Transformations # Transformaciones de variables



# INICIALIZAR: Llaves de encriptación públicas
with open("Keys\public_key_H.txt", mode='rb') as publicfile: # Llave: Humanitaria
    keydata_H = publicfile.read()
public_key_H = rsa.PublicKey.load_pkcs1(keydata_H)

with open("Keys\public_key_L.txt", mode='rb') as publicfile: # Llave: Legal
    keydata_L = publicfile.read()
public_key_L = rsa.PublicKey.load_pkcs1(keydata_L)

with open("Keys\public_key_P.txt", mode='rb') as publicfile: # Llave: Psicosocial
    keydata_P = publicfile.read()
public_key_P = rsa.PublicKey.load_pkcs1(keydata_P)



# FUNCIÓN: ENCRIPTAR DATO | String
def encrypt_element(element, sheet):
    ## Selección: Llave pública a utilizar
    if sheet == "L":
        public_key = public_key_L
    if sheet == "P":
        public_key = public_key_P
    if sheet == "H":
        public_key = public_key_H

    N = public_key_P.n
    binary_N = bin(N)
    key_bits = len(binary_N) - 2 # Longitud de llave pública (bits)
    element_binary = str(''.join(format(i, '08b') for i in bytearray(element, encoding ='utf-8')))
    element_bits = len(element_binary) # Longitud de mensaje (bits)
    ## Caso: El mensaje a encriptar es mayor(bits) que la llave
    if element_bits >= 0.8*key_bits: # Caracterísica: Se consideran ciertos bits en la llave para el esquema de relleno
        splits = math.ceil(element_bits/(key_bits*0.8)) + 1
        intervals = math.floor(len(element)/splits)
        element = Transformations.add_newlines(element, intervals)
        element = element.split('\n') # Lista: Mensaje segmentado en substrings de longitud menor a la de la llave
        encrypted_strings = []
        ### Encriptar: Cada segmento del mensaje
        for string in element:
            encrypted = rsa.encrypt(str(string).encode(), public_key)
            encrypted_strings.append(base64.b64encode(encrypted).decode('utf-8'))
        encrypted = '\n'.join(encrypted_strings) # Concatenar: Segmentos del mensaje encriptados con un caracter divisor "\n"
        return encrypted
    ## Caso: El mensaje a encriptar es menor(bits) que la llave
    else: encrypted = rsa.encrypt(str(element).encode(), public_key)
    return base64.b64encode(encrypted).decode('utf-8')
