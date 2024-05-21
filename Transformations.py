import re
import unicodedata


# Depurar: String
def clean_string(string):
    string = unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('utf-8') # Eliminar acentos
    string = string.title() # Capitalizar primera letra de cada palabra
    string = re.sub(r'[^\w\s]', '', string) # Eliminar caracteres no alfanumericos excepto espacios
    string = string.replace(' ', '_') # Reemplazar espacios entre palabras por "_"
    string = re.sub('_+', '_', string) # Asegurar que solo haya un máximo de un "_" entre palabras
    string = string.strip('_') # Eliminar "_" al inicio y al final de la cadena
    string = string.replace('\n', '') # Elminar saltos de línea
    return string

def extract_uppercase(string):
    return ''.join(c for c in string if c.isupper())



