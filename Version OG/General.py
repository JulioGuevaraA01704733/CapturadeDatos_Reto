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
""" def new_entry(workbook, entry, GUI):
    global ver
    entry = [Transformations.clean_string(s) for s in entry] # Depurar: strings
    id = Transformations.generate_id(entry[:3])
    cols = len(workbook.worksheet("General").row_values(1))
    all_entries = workbook.worksheet("General").col_values(1)
    if id not in all_entries: # Nuevo registro
        index = len(all_entries)
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
            index = workbook.worksheet("General").find(query=id, in_column=1).row
            existing_entry = workbook.worksheet("General").row_values(index)[1:]
            elements_TU = Transformations.is_different(entry, existing_entry)
            for i in range(cols-1): # Actualizar registro
                if elements_TU[i]:
                    workbook.worksheet("General").update_cell(index, i+2, entry[i])
        else: # No sobrescribir
            return """

def new_entry(workbook, entry, GUI):
    global ver
    entry = [Transformations.clean_string(s) for s in entry] # Depurar: strings
    id = Transformations.generate_id(entry[:3])
    general_sheet = workbook.worksheet("General")
    num_entries = general_sheet.col_values(1)
    if id not in num_entries: # Nuevo registro
        index = len(num_entries)
        values_to_insert = [id] + entry
        general_sheet.insert_row(values_to_insert, index+1) # Insertar registro
        for sheet_name in ["Legal", "Psicosocial"]:
            sheet = workbook.worksheet(sheet_name)
            sheet.update_cell(len(sheet.col_values(1))+1, 1, id)
    else: # Registro repetido
        verification_popup("El sujeto ya existe dentro\n de la base de datos.\n ¿Desesa actualizarlo?", GUI)
        GUI.wait_window(pop)
        if ver == 1: # Actualizar
            index = general_sheet.find(query=id, in_column=1).row
            existing_entry = general_sheet.row_values(index)[1:]
            elements_TU = Transformations.is_different(entry, existing_entry)
            values_to_update = [id if i == 0 else (entry[i-1] if elements_TU[i-1] else existing_entry[i-1]) for i in range(len(existing_entry)+1)][1:]
            general_sheet.update('B{}:{}'.format(index, chr(65+len(values_to_update))), [values_to_update]) # Actualizar registro
