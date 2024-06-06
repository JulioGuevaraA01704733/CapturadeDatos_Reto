""" ARCHIVO AUXILIAR: Almacena la función de desencriptación RSA de datos."""



# IMPORTAR: LIBRERÍAS
import rsa # Encriptación RSA
import base64 # Codificación
import math # Funciones matemáticas



# FUNCIÓN: INICIALIZA LA LLAVE PRIVADA
def get_key(path):
    with open(path, mode = "rb") as privatefile:
        keydata = privatefile.read()
    private_key = rsa.PrivateKey.load_pkcs1(keydata)
    return private_key


# FUNCIÓN: DESENCRIPTAR DATO | String
def decrypt_element(element, path):
    private_key = get_key(path) # Inicializar: Llave privada apropiada
    
    ## Caso: El mensaje a desencriptar se debe segmentar
    if "\n" in element:
        element = element.split('\n')  # Segmentar: Mensaje en cada salto de línea
        decrypted_strings = []
        ### Desencriptar: Cada segmento del mensaje
        for string in element:
            try:
                decrypted = rsa.decrypt(base64.b64decode(string), private_key).decode('utf-8')
            #### Caso: La llave utilizada es incorrecta
            except rsa.pkcs1.DecryptionError:
                return "ErrorLlaveIncorrecta"
            decrypted_strings.append(decrypted)
        decrypted = ''.join(decrypted_strings) # Concatenar: Segmentos de mensaje desencriptado
    ## Caso: El mensaje a desencriptar no se debe segmentar
    else:
        try:
            decrypted = rsa.decrypt(base64.b64decode(element), private_key).decode('utf-8')
        ### Caso: La llave utilizada es incorrecta
        except rsa.pkcs1.DecryptionError:
            return "ErrorLlaveIncorrecta"
    return decrypted