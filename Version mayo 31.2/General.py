import Transformations
import CTkClasses
import customtkinter
import hashlib
import datetime

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

        self.namesGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Nombre(s): ", fg_color="transparent")
        self.namesGLabel.grid(row=0, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.namesGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.namesGEntry.grid(row=0, column=1, padx=1, pady=5, ipady=0, sticky="e")

        self.surPGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Apellido Paterno: ", fg_color="transparent")
        self.surPGLabel.grid(row=1, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.surPGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.surPGEntry.grid(row=1, column=1, padx=1, pady=5, ipady=0, sticky="e")

        self.surMGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Apellido Materno: ", fg_color="transparent")
        self.surMGLabel.grid(row=2, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.surMGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.surMGEntry.grid(row=2, column=1, padx=1, pady=5, ipady=0, sticky="e")

        self.dobGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Fecha de Nacimiento (DD/MM/YYYY): ", fg_color="transparent")
        self.dobGLabel.grid(row=3, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.dobGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.dobGEntry.grid(row=3, column=1, padx=1, pady=5, ipady=0, sticky="e")

        self.ageGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Edad al Momento de Registro: ", fg_color="transparent")
        self.ageGLabel.grid(row=4, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.ageGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.ageGEntry.grid(row=4, column=1, padx=1, pady=5, ipady=0, sticky="e")

        self.genderGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Género: ", fg_color="transparent")
        self.genderGLabel.grid(row=5, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.genderGEntry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Hombre", "Mujer", "Hombre LGBTTTIQ+", "Mujer LGBTTTIQ+"])
        self.genderGEntry.grid(row=5, column=1, padx=1, pady=5, ipady=0, sticky="e")

        self.nationalityGLabel = customtkinter.CTkLabel(self.scrollable_frame, text="Nacionalidad: ", fg_color="transparent")
        self.nationalityGLabel.grid(row=6, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.nationalityGEntry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["México", "Estados Unidos de América", "Guatemala", "Honduras",
                                                                                "El Salvador", "Venezuela", "Nicaragua", "Haití", "Colombia", "Cuba",
                                                                                "Argentina", "Afganistán", "Siria", "Alemania", "Brasil", "Perú",
                                                                                "Guayana Francesa", "Belice", "Panamá", "Ecuador"])
        self.nationalityGEntry.grid(row=6, column=1, padx=1, pady=5, ipady=0, sticky="e")

        self.stateGLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Departamento / Estado: ", fg_color = "transparent")
        self.stateGLabel.grid(row=7, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.stateGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.stateGEntry.grid(row=7, column=1, padx=1, pady=5, ipady=0, sticky="e")

        self.dateGLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Fecha de Registro (DD/MM/YYYY): ", fg_color = "transparent")
        self.dateGLabel.grid(row=8, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.dateGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.dateGEntry.grid(row=8, column=1, padx=1, pady=5, ipady=0, sticky="e")

        self.phoneGLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Número Telefónico de Contacto: ", fg_color = "transparent")
        self.phoneGLabel.grid(row=9, column=0, padx=1, pady=5, ipady=0, sticky="e")
        self.phoneGEntry = customtkinter.CTkTextbox(self.scrollable_frame, width=300, height=10)
        self.phoneGEntry.grid(row=9, column=1, padx=1, pady=5, ipady=0, sticky="e")


        self.submitGBtn = customtkinter.CTkButton(self.scrollable_frame, text="Registrar", width=50,
                                                  command=lambda: new_entry(self.workbook, self.getGText(), self.app))
        self.submitGBtn.grid(row=10, column=0, padx=1, pady=5, ipady=0, sticky="e")

    def getGText(self): # Obtener Registros
        entriesGText1 = [self.surPGEntry, self.surMGEntry, self.namesGEntry, self.dobGEntry]
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
            """ existing_entry = general_sheet.row_values(index)[1:]
            elements_TU = Transformations.is_different(entry, existing_entry)
            values_to_update = [id if i == 0 else (entry[i-1] if elements_TU[i-1] else existing_entry[i-1]) for i in range(len(existing_entry)+1)][1:] """
            general_sheet.update('B{}:{}'.format(index, chr(65+len(entry))), [entry]) # Actualizar registro
        else: return
