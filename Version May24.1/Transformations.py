import re
import unicodedata
import hashlib


# Depurar: String
def clean_string(string):
    string = unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('utf-8') # Eliminar acentos
    string = string.title() # Capitalizar primera letra de cada palabra
    string = re.sub(r'[^\w\s]', '', string) # Eliminar caracteres no alfanumericos excepto espacios
    string = string.replace("\t", "") # Eliminar tabulaciones
    string = string.replace(' ', '_') # Reemplazar espacios entre palabras por "_"
    string = re.sub('_+', '_', string) # Asegurar que solo haya un máximo de un "_" entre palabras
    string = string.strip('_') # Eliminar "_" al inicio y al final de la cadena
    if not string: return "N/a"
    return string

def extract_uppercase(string):
    return ''.join(c for c in string if c.isupper())


def is_different(list1, list2):
    differences =[]
    for i in range(len(list1)):
        if list1[i] == "N/a":
            differences.append(0)
        elif list1[i] == list2[i]:
            differences.append(0)
        else:
            differences.append(1)
    return differences

def generate_id(names):
    idT = ''.join(names)
    h = hashlib.blake2s(digest_size=10)
    h.update(idT.encode())
    id = extract_uppercase(idT) + h.hexdigest() # Generar: identificador (Iniciales + Hash)
    return id

