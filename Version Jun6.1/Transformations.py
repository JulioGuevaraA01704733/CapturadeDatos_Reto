""" ARCHIVO AUXILIAR: Almacena funciones de transformaciones de datos utilizadas en múltiples documentos."""



# IMPORTAR: LIBRERÍAS
import re # Expresiones regulares
import unicodedata # Formato unicode de string
from datetime import datetime # Manejo de fechas



# FUNCIÓN: DEPURAR STRING | String
def clean_string(string):
    try: # Formatear fechas
        date_obj = datetime.strptime(string, '%d/%m/%Y')
        string = date_obj.strftime('%d/%m/%Y')
    except ValueError:
        string = unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('utf-8') # Eliminar: Acentos
        string = string.title() # Capitalizar: Primera letra de cada palabra
        string = re.sub(r'[^\w\s]', '', string) # Eliminar: Caracteres no alfanumericos excepto espacios
        string = string.replace("\t", "") # Eliminar: Tabulaciones
        string = string.replace(' ', '_') # Reemplazar: Espacios entre palabras por "_"
        string = re.sub('_+', '_', string) # Característica: Asegurar que solo haya un máximo de un "_" entre palabras
        string = string.strip('_') # Eliminar: "_" al inicio y al final de la cadena
        if not string: return "N/a" # Remplazar: "" -> "N/a"
    return string



# FUNCIÓN: EXTRAR Y CONCATENAR MAYUSCULAS DE STRING | String
def extract_uppercase(string):
    return ''.join(c for c in string if c.isupper())



# FUNCIÓN: GENERAR IDENTIFICADOR | String
def generate_id(names):
    idT = ''.join(names)
    id = extract_uppercase(idT) + "-" + idT
    """ Ejemplo:
            names = ["Garza", "García", "Carlos_Santiago"]
            idT =  "GarzaGarcíaCarlos_Santiago" 
            id = "GGCS-GarzaGarcíaCarlos_Santiago"
    """
    return id



# FUNCIÓN: INSERTAR SALTO DE LINEA EN INTERVALOS ESPECIFICADOS | String
def add_newlines(text, interval):
    return "\n".join(text[i:i + interval] for i in range(0, len(text), interval))
