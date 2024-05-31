import encryption
import Transformations
import customtkinter
import CTkClasses
import decryption
import tkinter

class RegistroLegal:
    def __init__(self, tab2, workbook, app):
        self.tab2 = tab2
        self.workbook = workbook
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tab2, width=600, height=600)
        self.scrollable_frame.grid(row=0, column=3, sticky="nsew", padx=0, pady=0)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.namesLLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Nombre(s):  ", fg_color = "transparent") # Nombre(s)
        self.namesLLabel.grid(row = 0, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.namesLEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.namesLEntry.grid(row = 0, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")

        self.surPLLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Apellido Paterno: ", fg_color = "transparent") # Apellido Paterno
        self.surPLLabel.grid(row = 1, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.surPLEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.surPLEntry.grid(row = 1, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")

        self.surMLLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Apellido Materno: ", fg_color = "transparent") # Apellida Materno
        self.surMLLabel.grid(row = 2, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.surMLEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.surMLEntry.grid(row = 2, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")

        self.L2Label = customtkinter.CTkLabel(self.scrollable_frame, text="Orientaciones Legales:  ", fg_color="transparent")
        self.L2Label.grid(row=3, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L2Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L2Entry.grid(row=3, column = 1, padx=1,pady=5,ipady=0,sticky="e")

        self.L3Label = customtkinter.CTkLabel(self.scrollable_frame, text="Asesorías Legales:  ", fg_color="transparent")
        self.L3Label.grid(row=4, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L3Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L3Entry.grid(row=4, column = 1, padx=1,pady=5,ipady=0,sticky="e")

        self.L4Label = customtkinter.CTkLabel(self.scrollable_frame, text="Solicitud de Refugiado:  ", fg_color="transparent")
        self.L4Label.grid(row=5, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L4Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L4Entry.grid(row=5, column = 1, padx=1,pady=5,ipady=0,sticky="e")

        self.L5Label = customtkinter.CTkLabel(self.scrollable_frame, text="Regularización por Razones Humanitarias:  ", fg_color="transparent")
        self.L5Label.grid(row=6, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L5Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L5Entry.grid(row=6, column = 1, padx=1,pady=5,ipady=0,sticky="e")

        self.L6Label = customtkinter.CTkLabel(self.scrollable_frame, text="Regularización por Unidad Familiar:  ", fg_color="transparent")
        self.L6Label.grid(row=7, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L6Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L6Entry.grid(row=7, column = 1, padx=1,pady=5,ipady=0,sticky="e")

        self.L7Label = customtkinter.CTkLabel(self.scrollable_frame, text="Cambio de Condición de Estancia:  ", fg_color="transparent")
        self.L7Label.grid(row=8, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L7Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L7Entry.grid(row=8, column = 1, padx=1,pady=5,ipady=0,sticky="e")

        self.L8Label = customtkinter.CTkLabel(self.scrollable_frame, text="Renovaciones:  ", fg_color="transparent")
        self.L8Label.grid(row=9, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L8Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L8Entry.grid(row=9, column = 1, padx=1,pady=5,ipady=0,sticky="e")

        self.L9Label = customtkinter.CTkLabel(self.scrollable_frame, text="Resposición de Documento Migratorio:  ", fg_color="transparent")
        self.L9Label.grid(row=10, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L9Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L9Entry.grid(row=10, column = 1, padx=1,pady=5,ipady=0,sticky="e")

        self.L10Label = customtkinter.CTkLabel(self.scrollable_frame, text="Notificación de Cambio de Domicilio:  ", fg_color="transparent")
        self.L10Label.grid(row=11, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L10Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L10Entry.grid(row=11, column = 1, padx=1,pady=5,ipady=0,sticky="e")

        self.L11Label = customtkinter.CTkLabel(self.scrollable_frame, text="Notificación de Cambio de Nacionalidad:  ", fg_color="transparent")
        self.L11Label.grid(row=12, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L11Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L11Entry.grid(row=12, column = 1, padx=1,pady=5,ipady=0,sticky="e")

        self.L12Label = customtkinter.CTkLabel(self.scrollable_frame, text="Notificación de Cambio de Lugar de Trabajo:  ", fg_color="transparent")
        self.L12Label.grid(row=13, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L12Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L12Entry.grid(row=13, column = 1, padx=1,pady=5,ipady=0,sticky="e")

        self.L13Label = customtkinter.CTkLabel(self.scrollable_frame, text="Canalización de las Personas Migrantes a \nlos consulados de Honduras, \nGuatemala y el Salvador:  ", fg_color="transparent")
        self.L13Label.grid(row=14, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L13Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L13Entry.grid(row=14, column = 1, padx=1,pady=5,ipady=0,sticky="e")

        self.submitLBtn = customtkinter.CTkButton(self.scrollable_frame, text="Registrar", width=50, command = lambda: new_entry(self.workbook, self.getLText(), self.app))
        self.submitLBtn.grid(row = 15, column = 0, padx=1,pady=5,ipady=0,sticky="e")

    def getLText(self):
        entriesLText = [self.surPLEntry, self.surMLEntry, self.namesLEntry, self.L2Entry, self.L3Entry, self.L4Entry, self.L5Entry, self.L6Entry, self.L7Entry, self.L8Entry, self.L9Entry, self.L10Entry, self.L11Entry, self.L12Entry, self.L13Entry]
        return [entry.get(0.0, "end-1c") for entry in entriesLText]



def new_entry(workbook, entry, GUI):
    global ver
    id = Transformations.generate_id([Transformations.clean_string(s) for s in entry[:3]])
    entry = [e if e else "N/a" for e in entry]
    entry = entry[3:]
    legal_sheet = workbook.worksheet("Legal")
    cols = len(legal_sheet.row_values(1)) # MMANUAL
    legal_ids = legal_sheet.col_values(1)
    if id not in legal_ids: # Registro no existente
        CTkClasses.popup_error("Registre al individuo en la\n sección General antes de llevar\n a cabo el registro legal.", GUI)
        return
    index = legal_ids.index(id) + 1
    existing_row = legal_sheet.row_values(index)[1:]
    if len(existing_row) == 0:  # Agregar registro Legal
        encrypted_entries = [encryption.encrypt_element(e, "L") for e in entry]
        legal_sheet.update('B{}:{}'.format(index, chr(65 + len(encrypted_entries))), [encrypted_entries])# Actualizar registro
    else:
        ver = CTkClasses.verification_popup("El sujeto ya cuenta con\n un registro legal.\n ¿Desea actualizarlo?", GUI)
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




""" def get_loc(sheet, id):
    cell = sheet.find(id)
    idx = cell.row
    return idx
 """
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



""" def popup_error(msg):
    pop = tkinter.Tk()
    pop.title("Error")
    pop.geometry("320x180")
    pop.configure(bg='#2B2B2B') 
    pop.attributes('-topmost', True)

    label = tkinter.Label(pop, text=msg, bg='#2B2B2B', fg='white')
    label.pack(side="top", fill="x", pady=10)
    B1 = tkinter.Button(pop, text="Okay", command=pop.destroy, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10)
    B1.pack()
    pop.mainloop() """

""" def choice(option):
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
    no_button.pack() """