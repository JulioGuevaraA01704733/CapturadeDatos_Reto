import rsa
import pandas as pd
import base64
from datetime import datetime

# Inicializar: Llave privada
def get_key(key):
    global private_key
    with open(key, mode='rb') as publicfile:
        keydata = publicfile.read()
    private_key = rsa.PrivateKey.load_pkcs1(keydata)

# Desencriptar: Elemento
def decrypt_element(element):
    decrypted = rsa.decrypt(base64.b64decode(element), private_key).decode('utf-8')
    try:
        return datetime.strptime(decrypted, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return decrypted
    
# Desencriptar: Base de datos
    # !!!renombrar variables!!!
    # !!!eliminar bases de datos no en uso!!!
def decrypt_database(filename, decryptOpt):
    xlsx = pd.ExcelFile(filename)
    df_general = pd.read_excel(xlsx, "General", index_col = 0)
    df_legal_encrypted = pd.read_excel(xlsx, "Legal", index_col = 0)
    df_psicosocial_encrypted = pd.read_excel(xlsx, "Psicosocial", index_col = 0)
    #df_humanitario_encrypted = pd.read_excel(xlsx, "Humanitario", index_col = 0)

    if decryptOpt == 1:
        df_legal = df_legal_encrypted.applymap(decrypt_element)
        df_legal_encrypted = df_legal.copy()

    if decryptOpt == 2:
        df_psicosocial = df_psicosocial_encrypted.applymap(decrypt_element)
        df_psicosocial_encrypted = df_psicosocial.copy()
    
    with pd.ExcelWriter(filename) as writer:
        df_general.to_excel(writer, sheet_name="General")
        df_legal_encrypted.to_excel(writer, sheet_name="Legal")
        df_psicosocial_encrypted.to_excel(writer, sheet_name="Psicosocial")
        #df_humanitario.to_excel(writer, sheet_name="Humanitario")

