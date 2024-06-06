""" ARCHIVO SECUNDARIO: Define la interfaz y funcionamiento del registro legal."""



# IMPORTAR: LIBRERÍAS
import customtkinter # Diseño de interfaz

# IMPORTAR: ARCHIVOS    
import Transformations # Transformaciones de variables
import CTkClasses # Clases de (custom)tkinter
import Global # Funciones generalizadas
import encryption # Encriptación de datos



# CLASE: REGISTRO GENERAL
class RegistroLegal:
    def __init__(self, tab2, workbook, app):
        self.tab2 = tab2
        self.workbook = workbook
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        # Componente: Scrollbar
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tab2, width=600, height=600)
        self.scrollable_frame.grid(row=0, column=3, sticky="nsew", padx=0, pady=0)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        ## Componentes: Texto, cajas de texto, menus de opción multiple y botones
        n_rows = 0

        self.namesLLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Nombre(s):  ", fg_color = "transparent") # Nombre(s)
        self.namesLLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.namesLEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.namesLEntry.grid(row = n_rows, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")
        n_rows += 1

        self.surPLLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Apellido Paterno: ", fg_color = "transparent") # Apellido Paterno
        self.surPLLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.surPLEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.surPLEntry.grid(row = n_rows, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")
        n_rows += 1

        self.surMLLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Apellido Materno: ", fg_color = "transparent") # Apellida Materno
        self.surMLLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.surMLEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.surMLEntry.grid(row = n_rows, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")
        n_rows += 1

        self.L2Label = customtkinter.CTkLabel(self.scrollable_frame, text="Orientaciones Legales:  ", fg_color="transparent")
        self.L2Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L2Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L2Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

        self.L3Label = customtkinter.CTkLabel(self.scrollable_frame, text="Asesorías Legales:  ", fg_color="transparent")
        self.L3Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L3Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L3Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

        self.L4Label = customtkinter.CTkLabel(self.scrollable_frame, text="Solicitud de Refugiado:  ", fg_color="transparent")
        self.L4Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L4Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L4Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

        self.L5Label = customtkinter.CTkLabel(self.scrollable_frame, text="Regularización por Razones Humanitarias:  ", fg_color="transparent")
        self.L5Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L5Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L5Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

        self.L6Label = customtkinter.CTkLabel(self.scrollable_frame, text="Regularización por Unidad Familiar:  ", fg_color="transparent")
        self.L6Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L6Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L6Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

        self.L7Label = customtkinter.CTkLabel(self.scrollable_frame, text="Cambio de Condición de Estancia:  ", fg_color="transparent")
        self.L7Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L7Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L7Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

        self.L8Label = customtkinter.CTkLabel(self.scrollable_frame, text="Renovaciones:  ", fg_color="transparent")
        self.L8Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L8Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L8Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

        self.L9Label = customtkinter.CTkLabel(self.scrollable_frame, text="Resposición de Documento Migratorio:  ", fg_color="transparent")
        self.L9Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L9Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L9Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

        self.L10Label = customtkinter.CTkLabel(self.scrollable_frame, text="Notificación de Cambio de Domicilio:  ", fg_color="transparent")
        self.L10Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L10Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L10Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

        self.L11Label = customtkinter.CTkLabel(self.scrollable_frame, text="Notificación de Cambio de Nacionalidad:  ", fg_color="transparent")
        self.L11Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L11Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L11Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

        self.L12Label = customtkinter.CTkLabel(self.scrollable_frame, text="Notificación de Cambio de Lugar de Trabajo:  ", fg_color="transparent")
        self.L12Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L12Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L12Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

        self.L13Label = customtkinter.CTkLabel(self.scrollable_frame, text="Canalización de las Personas Migrantes a \nlos consulados de Honduras, \nGuatemala y el Salvador:  ", fg_color="transparent")
        self.L13Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        self.L13Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.L13Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

        self.submitLBtn = customtkinter.CTkButton(self.scrollable_frame, text="Registrar", width=50, command = lambda: new_entry(self.workbook, self.getLText(), self.app))
        self.submitLBtn.grid(row = n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

    ## Función: Obtener datos del registro legal | Lista
    def getLText(self):
        entriesLText = [self.surPLEntry, self.surMLEntry, self.namesLEntry, self.L2Entry, self.L3Entry, self.L4Entry, self.L5Entry, self.L6Entry, self.L7Entry, self.L8Entry, self.L9Entry, self.L10Entry, self.L11Entry, self.L12Entry, self.L13Entry]
        return [entry.get(0.0, "end-1c") for entry in entriesLText]



# FUNCIÓN: REGISTRAR/ACTUALIZAR DATOS EN LA BASE DE DATOS
def new_entry(workbook, entry, GUI):
    id = Transformations.generate_id([Transformations.clean_string(s) for s in entry[:3]]) # Generar: Identificador
    entry = [e if e else "N/a" for e in entry] # Remplazar: Registros vaciós -> "N/a"
    entry = entry[3:] # Eliminar: Nombres
    legal_sheet = workbook.worksheet("Legal") # Seleccionar: Hoja de registro legal
    cols = len(legal_sheet.row_values(1)) # Obtener: Nombres de columna
    legal_ids = legal_sheet.col_values(1) # Obtener: IDs de registros existentes

    ## Caso: Identificador inexistente en registro GENERAL o nombres mal escritos
    if id not in legal_ids:
        id2 = Global.similar_entries(id, legal_ids[1:], GUI)
        ### Caso: Identificador inexistente en regsitro GENERAL
        if id2 == id:
            #### Error: Se debe realizar el registro GENERAL antes del LEGAL
            CTkClasses.popup_error("Registre al individuo en la\n sección General antes de llevar\n a cabo el registro psicosocial.", GUI)
            return
        ### Caso: Nombres mal escritos
        else: id = id2 # Corregir: Identificador del registro mal escrito(nombres)
    index = legal_ids.index(id) + 1
    existing_row = legal_sheet.row_values(index)[1:] # Obtener: Registro existnte (ya alamacenado)
    ## Caso: Generar nuevo registro
    if len(existing_row) == 0:
        encrypted_entries = [encryption.encrypt_element(e, "L") for e in entry] # Encriptar datos a registrar
        legal_sheet.update('B{}:{}'.format(index, "M", str(index)), [encrypted_entries]) # Insertar: Registros(encrypted entries) en la fila(index) a partir de la columna B del registro legal(legal_sheet)
    ## Caso: Registro existente
    else:
        ### Input: Confirmación para actualizar un registro existnte
        ver = CTkClasses.verification_popup("El sujeto ya cuenta con\n un registro legal.\n ¿Desea actualizarlo?", GUI)
        ### Caso: Actualizar registro existente
        if ver == 1:
            values_to_update = []
            for i in range(cols - 1):
                if entry[i] != "N/a": # Característica: No se atualizan datos existntes si el nuevo es "N/a"
                    encrypted_entry = encryption.encrypt_element(entry[i], "L") # Encriptar datos a registrar
                    values_to_update.append(encrypted_entry)
                else: values_to_update.append(existing_row[i])
            legal_sheet.update('B{}:{}'.format(index, "M", str(index)), [values_to_update]) # Actualizar: Registros(values_to_update) en el rango B(index)-M(index) del regitro legal(legal_sheet)
        ### Caso: No actualizar registro existente
        else: return