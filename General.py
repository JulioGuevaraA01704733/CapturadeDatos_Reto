import Transformations
import CTkClasses
import customtkinter
import hashlib

def choice(option):
    global ver
    ver = option
    pop.destroy()


def verification_popup(text_ver, GUI):
    global pop
    pop = CTkClasses.ToplevelWindow(GUI)
    pop.title("Verificación")
    pop.geometry("320x180")
    pop.attributes('-topmost', True)

    pop_label = customtkinter.CTkLabel(pop, text = text_ver)
    pop_label.pack()

    yes_button = customtkinter.CTkButton(pop, text = "Sí", command = lambda: choice(1))
    yes_button.pack()

    no_button = customtkinter.CTkButton(pop, text="No", command = lambda: choice(0))
    no_button.pack()

def get_last_shape(sheet):
    idx = len(sheet.col_values(1))
    cols = len(sheet.row_values(idx))
    return idx, cols

# Función: Generar/editar registro General
def new_entry(workbook, entry, GUI):
    global ver
    entry = [Transformations.clean_string(s) for s in entry] # Depurar: strings
    idT = ''.join(entry[:3])
    h = hashlib.blake2s(digest_size=10)
    h.update(idT.encode())
    id = Transformations.extract_uppercase(idT) + h.hexdigest() # Generar: identificador (Iniciales + Hash)
    cols = len(workbook.worksheet("General").row_values(1))
    if id not in workbook.worksheet("General").col_values(1): # Nuevo registro
        index = len(workbook.worksheet("General").col_values(1))
        for i in range (cols-1): # Agregar registro
            workbook.worksheet("General").update_cell(index+1, 1, id)
            workbook.worksheet("General").update_cell(index+1, i+2, entry[i])
            index = len(workbook.worksheet("Legal").col_values(1)) # Registro "vacío" en Legal
            workbook.worksheet("Legal").update_cell(index+1, 1, id)
            index = len(workbook.worksheet("Psicosocial").col_values(1)) # Registro "vacio" en psicosocial
            workbook.worksheet("Psicosocial").update_cell(index+1, 1, id)
    else: # Registro repetido
        verification_popup("El sujeto ya existe dentro\n de la base de datos.\n ¿Desesa actualizarlo?", GUI)
        GUI.wait_window(pop)
        if ver == 1: # Sobrescribir
            index = workbook.workshee("General").findall(query=id, in_column=1)-1
            existing_entry = workbook.worksheet("General").row_values(index+1)[1:]
            elements_TU = [0 if entry[i] == existing_entry[i] else 1 for i in range(len(entry))]
            for i in range(cols-1): # Actualizar registro
                if elements_TU[i]:
                    workbook.worksheet("General").update_cell(index+1, 1, id)
                    workbook.worksheet("General").update_cell(index+1, i+2, entry[i])
        else: # No sobrescribir
            return
    

    """ for i in range (cols-1): # Actualizar / agregar registro
        workbook.worksheet("General").update_cell(index+1, 1, id)
        workbook.worksheet("General").update_cell(index+1, i+2, entry[i])
    idx, cols = get_last_shape(workbook.worksheet("Legal")) # Generar registro vacío en "Legal"
    workbook.worksheet("Legal").update_cell(idx+1, 1, id)
    idx, cols = get_last_shape(workbook.worksheet("Psicosocial")) # Generar registro vacío en "Psicosocial"
    workbook.worksheet("Psicosocial").update_cell(idx+1, 1, id)

 """
