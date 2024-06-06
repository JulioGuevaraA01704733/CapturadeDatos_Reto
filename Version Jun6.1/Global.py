""" ARCHIVO AUXILIAR: Almacena funciones generalizadas utilizadas en múltiples documentos."""



# IMPORTAR: LIBRERÍAS
import customtkinter # Diesño de interfaz
import tkinter # Diesño de interfaz
import re # Expresiones Regulares
from difflib import SequenceMatcher # Comparar pares de datos



# FUNCION: DETECTA IDENTIFICADORES SIMILARES AL INGRESADO Y PREGUNTA AL USUARIO SI QUISO ESCRIBIR ALGUNO DE LOS SIMILARES | String
def similar_entries(id, ids, GUI):
    prefix = id.split("-")[0]
    similar_ids = [item for item in ids if item.startswith(prefix)]
    similar_ids = [item for item in similar_ids if SequenceMatcher(None, item, id).ratio() >= 0.8] # Lista: Identificadores con similitud del 80% al id ingresado
    
    ## Caso: Existen identificadores similares
    if len(similar_ids) != 0:
        similar_names = []
        for name in similar_ids:
            name = name.split("-")[1:]
            name = "".join(name)
            name = name.replace("_", "")
            name = re.findall('[A-Z][^A-Z]*', name)    
            first_element = name.pop(0)
            name.append(first_element)  
            second_element = name.pop(0)
            name.append(second_element)   
            name = " ".join(name)
            similar_names.append(name)
        global value
        value = id

        ### Caso: Se desea seleccioanr uno de los identificadores similares
        def on_ok():
            global value
            value = similar_ids[similar_names.index(namesEntry.get())]
            popup.destroy()

        ### Caso: Se desea conservar el identificador ingresado
        def on_cancel():
            global value
            value = id
            popup.destroy()

        ### Ventana Emergente: Lista y selección de identificadores similares
        popup = tkinter.Toplevel(GUI)

        popup.title("Registro Similar")
        popup.geometry("420x180")
        popup.configure(bg='#2B2B2B') 
        popup.attributes('-topmost', True)

        queryLabel = tkinter.Label(popup, text="¿Quiso escribir alguno de los\n siguientes nombres?", bg='#2B2B2B', fg='white', font=(tkinter.font, 12))
        queryLabel.pack(padx=10, pady=10)

        namesEntry = customtkinter.CTkOptionMenu(popup, values=similar_names)
        namesEntry.pack(padx=10, pady=10,)

        ok_button = tkinter.Button(popup, text="Sí", command=on_ok, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10, font=(tkinter.font, 12))
        ok_button.pack(side=tkinter.LEFT, padx=10, pady=5)

        cancel_button = tkinter.Button(popup, text="No", command=on_cancel, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10, font=(tkinter.font, 12))
        cancel_button.pack(side=tkinter.RIGHT, padx=10, pady=5)

        popup.wait_window()
        return value
    ## Caso: No existen identificadores similares
    else: return id