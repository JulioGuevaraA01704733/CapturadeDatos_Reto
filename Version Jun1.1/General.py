import Transformations
import CTkClasses
import customtkinter
import hashlib
import datetime
import Global

# GUI
class RegistroGeneral:
    def __init__(self, tab1, workbook, app):
        self.tab1 = tab1
        self.workbook = workbook
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tab1, width=600, height=600)
        self.scrollable_frame.grid(row=0, column=3, sticky="nsew", padx=0, pady=0)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        n_rows = 0

        self.namesGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Nombre(s): ", fg_color="transparent")
        self.namesGLabel.grid(row=n_rows, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.namesGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.namesGEntry.grid(row=n_rows, column=1, padx=1, pady=5, ipady=0, sticky="e")
        
        n_rows += 1

        self.surPGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Apellido Paterno: ", fg_color="transparent")
        self.surPGLabel.grid(row=n_rows, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.surPGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.surPGEntry.grid(row=n_rows, column=1, padx=1, pady=5, ipady=0, sticky="e")

        n_rows += 1

        self.surMGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Apellido Materno: ", fg_color="transparent")
        self.surMGLabel.grid(row=n_rows, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.surMGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.surMGEntry.grid(row=n_rows, column=1, padx=1, pady=5, ipady=0, sticky="e")

        n_rows += 1

        self.dobGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Fecha de Nacimiento (DD/MM/YYYY): ", fg_color="transparent")
        self.dobGLabel.grid(row=n_rows, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.dobGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.dobGEntry.grid(row=n_rows, column=1, padx=1, pady=5, ipady=0, sticky="e")

        n_rows += 1

        self.ageGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Edad al Momento de Registro: ", fg_color="transparent")
        self.ageGLabel.grid(row=n_rows, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.ageGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.ageGEntry.grid(row=n_rows, column=1, padx=1, pady=5, ipady=0, sticky="e")

        n_rows += 1

        self.genderGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Género: ", fg_color="transparent")
        self.genderGLabel.grid(row=n_rows, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.genderGEntry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Hombre", "Mujer", "Hombre LGBTTTIQ+", "Mujer LGBTTTIQ+"])
        self.genderGEntry.grid(row=n_rows, column=1, padx=1, pady=5, ipady=0, sticky="e")

        n_rows += 1

        self.nationalityGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Nacionalidad: ", fg_color="transparent")
        self.nationalityGLabel.grid(row=n_rows, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.nationalityGEntry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["México", "Estados Unidos de América", "Guatemala", "Honduras",
                                                                                "El Salvador", "Venezuela", "Nicaragua", "Haití", "Colombia", "Cuba",
                                                                                "Argentina", "Afganistán", "Siria", "Alemania", "Brasil", "Perú",
                                                                                "Guayana Francesa", "Belice", "Panamá", "Ecuador"])
        self.nationalityGEntry.grid(row=n_rows, column=1, padx=1, pady=5, ipady=0, sticky="e")

        n_rows += 1

        self.stateGLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Departamento / Estado: ", fg_color = "transparent")
        self.stateGLabel.grid(row=n_rows, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.stateGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.stateGEntry.grid(row=n_rows, column=1, padx=1, pady=5, ipady=0, sticky="e")

        n_rows += 1

        self.dateGLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Fecha de Registro (DD/MM/YYYY): ", fg_color = "transparent")
        self.dateGLabel.grid(row=n_rows, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.dateGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.dateGEntry.grid(row=n_rows, column=1, padx=1, pady=5, ipady=0, sticky="e")

        n_rows += 1

        self.phoneGLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Número Telefónico de Contacto: ", fg_color = "transparent")
        self.phoneGLabel.grid(row=n_rows, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.phoneGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.phoneGEntry.grid(row=n_rows, column=1, padx=1, pady=5, ipady=0, sticky="e")

        n_rows += 1

        self.submitGBtn = customtkinter.CTkButton(self.scrollable_frame, text="Registrar", width=50,
                                                  command=lambda: new_entry(self.workbook, self.getGText(), self.app))
        self.submitGBtn.grid(row=n_rows, column=0, padx=1, pady=5, ipady=0, sticky="e")

    def getGText(self): # Obtener Registros
        entriesGText1 = [self.surPGEntry, self.surMGEntry, self.namesGEntry, self.dobGEntry, self.ageGEntry]
        entriesGOption = [self.genderGEntry, self.nationalityGEntry]
        entriesGText2 = [self.stateGEntry, self.dateGEntry, self.phoneGEntry]
        entry = [entryT.get(0.0, "end-1c") for entryT in entriesGText1] + [entryO.get() for entryO in entriesGOption] + [entryT.get(0.0, "end-1c") for entryT in entriesGText2]
        return entry


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
    no_button.pack()

def get_last_shape(sheet):
    idx = len(sheet.col_values(1))
    cols = len(sheet.row_values(idx))
    return idx, cols """

# Función: Generar/editar registro General
def new_entry(workbook, entry, GUI):
    global ver
    entry = [Transformations.clean_string(s) for s in entry] # Depurar: strings
    id = Transformations.generate_id(entry[:3])
    general_sheet = workbook.worksheet("General")
    all_entries = general_sheet.col_values(1)
    if id not in all_entries: # Nuevo registro
        all_entries_initials = [item.split("-")[0] for item in all_entries]
        if id.split("-")[0] not in all_entries_initials:
            index = len(all_entries)
            values_to_insert = [id] + entry
            general_sheet.insert_row(values_to_insert, index+1) # Insertar registro
            for sheet_name in ["Legal", "Psicosocial", "Humanitario"]:
                sheet = workbook.worksheet(sheet_name)
                sheet.update_cell(len(sheet.col_values(1))+1, 1, id) # !!! PENDIENTE indice general -> indice especificio
            return
        else:
            id2 = Global.similar_entries(id, all_entries[1:], GUI)
            if id2 == id:
                index = len(all_entries)
                values_to_insert = [id] + entry
                general_sheet.insert_row(values_to_insert, index+1) # Insertar registro
                for sheet_name in ["Legal", "Psicosocial", "Humanitario"]:
                    sheet = workbook.worksheet(sheet_name)
                    sheet.update_cell(len(sheet.col_values(1))+1, 1, id) # !!! PENDIENTE indice general -> indice especificio
                return
            else: id = id2
    ver = CTkClasses.verification_popup("El sujeto ya existe dentro\n de la base de datos.\n ¿Desesa actualizarlo?", GUI)
    if ver == 1: # Actualizar
        index = general_sheet.find(query=id, in_column=1).row
        existing_entry = general_sheet.row_values(index)
        values_to_update = []
        current_id = existing_entry[0]
        existing_entry = existing_entry[1:]
        if Transformations.generate_id(entry[:3]) != current_id:
            ver2 = CTkClasses.verification_popup("Desea actualizar el nombre\n" + existing_entry[2] + " " + existing_entry [0] + " " 
                                            + existing_entry[1] + "\n a " + entry[2] + " " + entry[0] + " " + entry[1] + "?", GUI)
        else: ver2 = 0
        if ver2 == 1:
            for i in range(len(entry)):
                if entry[i] != "N/a":
                    values_to_update.append(entry[i])
                else: values_to_update.append(existing_entry[i])
            correct_id = Transformations.generate_id(entry[:3])
            values_to_update.insert(0, correct_id)
            general_sheet.update('A{}:{}'.format(index, 'K' + str(index)), [values_to_update]) # Actualizar registro
            for sheet_name in ["Legal", "Psicosocial", "Humanitario"]:
                sheet = workbook.worksheet(sheet_name)
                sheet.update_cell(index, 1, correct_id)
        else:
            entry = entry[3:]
            existing_entry = existing_entry[3:]
            for i in range(len(entry)):
                if entry[i] != "N/a":
                    values_to_update.append(entry[i])
                else: values_to_update.append(existing_entry[i])
            general_sheet.update('E{}:{}'.format(index, 'K' + str(index)), [values_to_update])
        return
    else: return


""" def new_entry(workbook, entry, GUI):
    global ver
    entry = [Transformations.clean_string(s) for s in entry] # Depurar: strings
    id = Transformations.generate_id(entry[:3])
    general_sheet = workbook.worksheet("General")
    all_entries = general_sheet.col_values(1)
    print(Global.similar_entries(id, all_entries[1:], GUI))
    if id not in all_entries: # Nuevo registro
        index = len(all_entries)
        values_to_insert = [id] + entry
        general_sheet.insert_row(values_to_insert, index+1) # Insertar registro
        for sheet_name in ["Legal", "Psicosocial"]:
            sheet = workbook.worksheet(sheet_name)
            sheet.update_cell(len(sheet.col_values(1))+1, 1, id) # !!! PENDIENTE indice general -> indice especificio
    else: # Registro repetido
        ver = CTkClasses.verification_popup("El sujeto ya existe dentro\n de la base de datos.\n ¿Desesa actualizarlo?", GUI)
        if ver == 1: # Actualizar
            index = general_sheet.find(query=id, in_column=1).row
            existing_entry = general_sheet.row_values(index)[1:]
            values_to_update = []
            for i in range(len(entry)):
                if entry[i] != "N/a":
                    values_to_update.append(entry[i])
                else: values_to_update.append(existing_entry[i])
            general_sheet.update('B{}:{}'.format(index, chr(65+len(entry))), [values_to_update]) # Actualizar registro
        else: return """