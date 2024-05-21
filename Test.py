import unicodedata
import re
import hashlib

def clean_string(string):
    string = unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('utf-8') # Eliminar acentos
    string = string.title() # Capitalizar primera letra de cada palabra
    string = re.sub(r'[^\w\s]', '', string) # Eliminar caracteres no alfanumericos excepto espacios
    string = string.replace(' ', '_') # Reemplazar espacios entre palabras por "_"
    string = re.sub('_+', '_', string) # Asegurar que solo haya un máximo de un "_" entre palabras
    string = string.strip('_') # Eliminar "_" al inicio y al final de la cadena
    string = string.replace('\n', '') # Elminar saltos de línea
    return string

def extract_uppercase(cadena):
    return ''.join(c for c in cadena if c.isupper())


""" a = "Armendáriz"
b = "Torres"
c = "David Fernando   2\n"
list = [a,b,c]

list_clean = [clean_string(entry) for entry in list]

print(list_clean)

abc = ''.join(list_clean[:3])
print(abc)

id = hash(abc)

print(id)

ABC = extract_uppercase(abc)
print(ABC)

id = ABC + str(id)

print(id) """

string = "ArmendarizTorresDavid_Fernando"
h = hashlib.blake2s(digest_size=10)
h.update(string.encode())
print(h.hexdigest())