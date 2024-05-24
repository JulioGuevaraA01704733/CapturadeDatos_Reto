import encryption
import Transformations
import customtkinter
import CTkClasses
import decryption
import tkinter

""" def popup_error(msg):
    pop = customtkinter.CTk()
    pop.title("Registro no encontrado")
    pop.geometry("320x180")
    pop.attributes('-topmost', True)

    label = customtkinter.CTkLabel(pop, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = customtkinter.CTkButton(pop, text="Okay", command=pop.destroy)
    B1.pack()
    pop.mainloop() """

def popup_error(msg):
    pop = tkinter.Tk()
    pop.title("Error")
    pop.geometry("320x180")
    pop.configure(bg='#2B2B2B') 
    pop.attributes('-topmost', True)

    label = tkinter.Label(pop, text=msg, bg='#2B2B2B', fg='white')
    label.pack(side="top", fill="x", pady=10)
    B1 = tkinter.Button(pop, text="Okay", command=pop.destroy, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10)
    B1.pack()
    pop.mainloop()

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

def new_entry(workbook, entry, GUI):
    global ver
    id = Transformations.generate_id([Transformations.clean_string(s) for s in entry[:3]])
    entry = [e if e else "N/a" for e in entry]
    entry = entry[3:]
    legal_sheet = workbook.worksheet("Legal")
    cols = len(legal_sheet.row_values(1)) # MMANUAL
    legal_ids = legal_sheet.col_values(1)
    if id not in legal_ids: # Registro no existente
        popup_error("Registre al individuo en la\n sección General antes de llevar\n a cabo el registro legal.")
        return
    index = legal_ids.index(id) + 1
    existing_row = legal_sheet.row_values(index)[1:]
    if len(existing_row) == 0:  # Agregar registro Legal
        encrypted_entries = [encryption.encrypt_element(e, "L") for e in entry]
        legal_sheet.update('B{}:{}'.format(index, chr(65 + len(encrypted_entries))), [encrypted_entries])# Actualizar registro
    else:
        verification_popup("El sujeto ya cuenta con\n un registro legal.\n ¿Desea actualizarlo?", GUI)
        GUI.wait_window(pop)
        if ver == 1:  # Actualizar registro Legal
            values_to_update = []
            for i in range(cols - 1):
                if entry[i] != "N/a":
                    encrypted_entry = encryption.encrypt_element(entry[i], "L")
                    values_to_update.append(encrypted_entry)
                else: values_to_update.append(existing_row[i])
            legal_sheet.update('B{}:{}'.format(index, chr(65 + len(values_to_update))), [values_to_update])
        else:  # No sobrescribir
            return




def get_loc(sheet, id):
    cell = sheet.find(id)
    idx = cell.row
    return idx

""" def new_entry(workbook, entry, GUI):
    global ver
    entry = [Transformations.clean_string(s) for s in entry] # Depurar: strings
    id = Transformations.generate_id(entry[:3])
    entry = entry[3:]
    cols = len(workbook.worksheet("Legal").row_values(1))
    if id not in workbook.worksheet("Legal").col_values(1): # Individuo no registrado en general
        popup_error("Registre al individuo en la\n sección General antes de llevar\n a cabo el registro legal.")
        return
    else:
        index = workbook.worksheet("Legal").find(query=id, in_column=1).row
        if len(workbook.worksheet("Legal").row_values(index)) == 1: # Agregar registro Legal
            for i in range(cols-1):
                encrypted_entry = encryption.encrypt_element(entry[i], "L")
                workbook.worksheet("Legal").update_cell(index, i+2, encrypted_entry)
        else:
            verification_popup("El sujeto ya cuenta con\n un registro legal.\n ¿Desesa actualizarlo?", GUI)
            GUI.wait_window(pop)
            if ver == 1: # Actualizar registro Legal
                for i in range(cols-1):
                    if entry[i] != "N/a":
                        encrypted_entry = encryption.encrypt_element(entry[i], "L")
                        workbook.worksheet("Legal").update_cell(index, i+2, encrypted_entry)
            else: # No sobrescribir
                return
            return """