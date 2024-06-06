""" ARCHIVO SECUNDARIO: Define la interfaz y funcionamiento de la visualización de registros."""


# IMPORTAR: LIBRERÍAS
import os # Lectura y escritura de archivos
import tkinter # Diesño de interfaz
import docx # Manejo de documentos word
import customtkinter # Diesño de interfaz

# IMPORTAR: ARCHIVOS    
import Transformations # Transformaciones de variables
import CTkClasses # Clases de (custom)tkinter
import Global # Funciones generalizadas
import decryption # Decriptación de datos



# CLASE: VISUALIZACIÓN DE REGISTROS
class Visualizar:
    def __init__(self, tab5, workbook, app):
        self.tab5 = tab5
        self.workbook = workbook
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        ## Componente: Scrollbar
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tab5, width=600, height=600)
        self.scrollable_frame.grid(row=0, column=3, sticky="nsew", padx=0, pady=0)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        
        ## Componentes: Texto, cajas de texto, menus de opción multiple y botones
        n_rows = 0

        self.namesVLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Nombre(s):  ", fg_color = "transparent") # Nombre(s)
        self.namesVLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.namesVEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.namesVEntry.grid(row = n_rows, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")
        n_rows += 1

        self.surPVLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Apellido Paterno: ", fg_color = "transparent") # Apellido Paterno
        self.surPVLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.surPVEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.surPVEntry.grid(row = n_rows, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")
        n_rows += 1

        self.surMVLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Apellido Materno: ", fg_color = "transparent") # Apellida Materno
        self.surMVLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.surMVEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.surMVEntry.grid(row = n_rows, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")
        n_rows += 1

        self.dbVLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Registros a Visualizar:  ", fg_color = "transparent") # Género
        self.dbVLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.dbVEntry = customtkinter.CTkOptionMenu(self.scrollable_frame, values = ["Legal", "Psicosocial", "Humanitario"])
        self.dbVEntry.grid(row = n_rows, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")
        n_rows += 1

        submitVBtn = customtkinter.CTkButton(self.scrollable_frame, text="Visualizar", width=50, command = lambda: # Registrar
                                                visualize(self.workbook, self.getVText(), self.dbVEntry.get(), self.app)) 
        submitVBtn.grid(row = n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

    ## Función: Obtener nombres de registro a visualizar | Lista
    def getVText(self):
        entriesVText = [self.surPVEntry, self.surMVEntry, self.namesVEntry]
        entry = [entryT.get(0.0, "end-1c") for entryT in entriesVText]
        return entry


# FUNCIÓN: VISUALIZAR REGISTROS
def visualize(workbook, names, sheet, GUI):
    names = [Transformations.clean_string(s) for s in names] # Depurar: nombres
    id = Transformations.generate_id(names) # Generar: Identificador
    ## Diccionarios: Directorio de llaves públicas | Columnas de registros
    path_dict = {"Legal": "Keys\private_key_L.txt", "Psicosocial": "Keys\private_key_P.txt", "Humanitario": "Keys\private_key_H.txt"}
    headers_dict = {"Legal": [
                        "Orientaciones Legales", 
                        "Asesorías legales", 
                        "Solicitud de refugiado", 
                        "Regularización por razones humanitarias", 
                        "Regularización por unidad familiar", 
                        "Cambio de condición de estancia", 
                        "Renovaciones", 
                        "Reposición de documento migratorio",
                        "Notificación de cambio de. Domicilio", 
                        "Notificación de cambio de nacionalidad", 
                        "Notificación de cambio de lugar de trabajo", 
                        "Canalización de las personas migrantes a los consulados de Honduras, Guatemala y el Salvador"],
                    "Psicosocial": [
                        "Inclusión (Trámite CURP)",
                        "Inclusión (Obtención RFC)",
                        "Inclusión (Obtención NSS)",
                        "Inclusión (Afiliación IMSS)",
                        "Inclusión (Acceso a vivienda)",
                        "Inclusión (Apertura de Cta. Bancaria)",
                        "Inclusión (Atención médica; Acompañamiento)",
                        "Educación (Revalidación de estudios; Acompañamiento)",
                        "Educación (Vinculación educativa; Escolaridad Obligatoria)",
                        "Empleabilidad (Capacitación técnica certificada; Acompañamiento)",
                        "Empleabilidad (Canalización para recepción de apoyo para la capacitación)",
                        "Empleabilidad (Capacitación / Orientación para ingresar al mercado laboral)",
                        "Empleabilidad (Canalización a empresa u organización especializada para la vinculación laboral)",
                        "Empleabilidad (Canalización a una empresa)",
                        "Empleabilidad (Canalización al SNE)",
                        "Empleabilidad (Canalización a una bolsa de empleo)",
                        "Empleabilidad (Canalización a organización especializada para el empleo)",
                        "Identificación y Protección (Necesidad específica de protección)",
                        "Salud Mental y Apoyo Psicosocial (Recibieron atención psicológica y psicosocial fuera del albergue)",
                        "Salud Mental y Apoyo Psicosocial (Identificación de necesidades psicosocial, orientación y canalización)",
                        "Salud Mental y Apoyo Psicosocial (Acompañamiento para acceso a servicios)",
                        "Salud Mental y Apoyo Psicosocial (Primeros auxilios psicológicos)",
                        "Salud Mental y Apoyo Psicosocial (Psicoterapia; individual/familiar)",
                        "Salud Mental y Apoyo Psicosocial (Psicoterapia Grupal)",
                        "Salud Mental y Apoyo Psicosocial (Talleres psicoeducativos)",
                        "Salud Mental y Apoyo Psicosocial (Canalización a servicios de psiquiatría)"],
                    "Humanitario":[
                        "Adulto, NNA, NNAnA", "Estado Civil", "Tipo de población",
                        "Documento identidad (Tarjeta de identidad de país de origen)",
                        "Documento de identidad (Certificado de nacionalidad / Acta de Nacimiento)",
                        "Documento de identidad (Pasaporte)", "Documento de identidad (CURP)",
                        "Documento de identidad (Documento Migratorio)", "Documento de identidad (Ningún documento)",
                        "Hijos", "¿Usted sabe leer y escribir?", "¿Cuál fue su último grado de estudio?",
                        "¿Cuál fue su último grado académico?", "Idiomas que domina (Inglés)",
                        "Idiomas que domina (Español)", "Idiomas que domina (Francés)",
                        "Idiomas que domina (Criollo haitiano)", "Idiomas que domina (Garifona)",
                        "Idiomas que domina (Portugués)", "Idioma que domina (Otro idioma)",
                        "Fecha en que salió de su país de origen (DD/MM/AAAA)",
                        "¿Cómo se encuentra viajando?", "¿Cómo viajó?",
                        "¿Por qué razón tomó la decisión de salir de su país?",
                        "Durante su viaje desde que salió de su país hasta antes de llegar a México, ¿Usted sufrió algún abuso a sus Derechos Humanos?",
                        "Cuando usted entró a territorio mexicano, ¿Usted vivió algún abuso o agresión?",
                        "En algún momento de su camino, ¿Usted le pagó a algún guía para viajar?",
                        "Fecha en que ingresó a México (DD/MM/AAAA)",
                        "¿Por dónde ingresó a México?", "¿Cuál es su destino final?",
                        "¿Cuenta con una red de apoyo en Monterrey?",
                        "¿Usted ha intentado ingresar a Estados Unidos?",
                        "¿Usted cuenta con una red de apoyo en Estados Unidos?",
                        "Descripción de la red de apoyo con la que cuenta en Estados Unidos",
                        "¿Usted ha estado en alguna estación migratoria?",
                        "Ante las vivencias de abuso de autoridad, agresiones y vulnerabilidad a Derechos Humanos, ¿Usted interpuso una denuncia formal?",
                        "¿Usted puede regresar a su país?", "¿Actualmente usted padece una enfermedad?",
                        "¿Se encuentra o encontraba en algún tratamiento médico?",
                        "¿Usted padece algún tipo de alergia?",
                        "En su trayecto por México, ¿Usted ha estado en algún otro albergue?",
                        "¿Se le brindó acceso al albergue de Casa Monarca?",
                        "Servicios brindados (Agua y Alimento)", "Servicios brindados (Alimento)",
                        "Servicios brindados (Kit de higiene)", "Servicios brindados (Ropa y calzado)",
                        "Servicios brindados (Acceso a higiene; Regadera)",
                        "Servicios brindados (Asesoría legal)", "Servicios brindados (Orientación legal)",
                        "Servicios brindados (Orientación en búsqueda de empleo)",
                        "Servicios brindados (Orientación en el acceso a la educación)",
                        "Servicios brindados (Orientación en la búsqueda de vivienda)",
                        "Servicios brindados (Orientación para acceder a servicios de salud)",
                        "Servicios brindados (Orientación a servicios psicológicos)",
                        "Servicios brindados (Canalización a servicios psicológicos)",
                        "Servicios brindados (Atención psicosocial)",
                        "Señales particulares", "Contacto de emergencia",
                        "Geográficamente, ¿Dónde se encuentra su contacto de emergencia?",
                        "Observaciones Finales"
                    ]}
    path = path_dict.get(sheet) # Inicializar: Llave privada
    ## Caso: Existe la llave privada apropiada
    if os.path.exists(path):
        general_sheet = workbook.worksheet("General") # Seleccionar: Hoja de registro general
        specific_sheet = workbook.worksheet(sheet) # Seleccionar: Hoja del registro a visualizar
        specific_sheet_ids = specific_sheet.col_values(1) # Obtener: IDs de registros existentes

        ### Caso: Identificador inexistente o nombres mal escritos
        if id not in specific_sheet_ids:
            id2 = Global.similar_entries(id, specific_sheet_ids[1:], GUI)
            #### Caso: Identificador inexistente en registros
            if id2 == id:
                #### Error: No existe el registro a visualizar
                CTkClasses.popup_error("Registro Inexistente", GUI)
                return
            #### Caso: Nombres mal escritos
            else: id = id2 # Corregir: Identificador del registro mal escrito(nombres)
        index = specific_sheet_ids.index(id) + 1
        values = specific_sheet.row_values(index)[1:]
        valuesG = general_sheet.row_values(index)
        headersG = ["ID", "Apellido Paterno", "Apellido Materno", "Nombre(s)", "Fecha de Nacimiento", "Edad al Momento del Registro", "Género", "Nacionalidad", "Departamento/Estado", "Fecha de Registro", "Número Telefónico de Contacto"]
        headersS =  headers_dict.get(sheet)
        dispG = "\n\n".join([f"{headersG[i]} : {valuesG[i]}" for i in range(len(headersG)-1)]) # Generar: String de registro general a deplegar ({columna n + : + dato n + \n} para todo dato n en registro general)
        dispS = "\n\n".join([f"{headersS[i]} : {decryption.decrypt_element(values[i], path)}" for i in range(len(values))]) # Generar: String de registro general a deplegar ({columna n + : + desencriptar(dato n) + \n} para todo dato n en registro general)
        ### Caso: LLave privada incorrecta
        if "ErrorLlaveIncorrecta" in dispS:
            #### Error: La llave de desencriptación es incorrecta
            CTkClasses.popup_error("Llave Incorrecta \nAcceso no autorizado.", GUI)
            return
        disp = dispG + "\n\n" + dispS
        ### Ventana Emergente: Datos a visualizar
        popup_visualize(disp, GUI, id, sheet)
    ## Caso: No existe la llave privada apropiada
    else:
        ### Error: No existe la llave privada apropiada
        CTkClasses.popup_error("No tiene la llave para visualizar\n los registros solicitados.", GUI)
    return



# VENTANA EMERGENTE: VISUALIZAR Y GUARDAR REGISTROS
def popup_visualize(data, GUI, id, sheet):
    global pop_vis
    pop_vis = tkinter.Toplevel(GUI)
    pop_vis.title("Visualización")
    pop_vis.geometry("780x780")
    pop_vis.attributes("-topmost", True)

    scrollable_frame = customtkinter.CTkScrollableFrame(pop_vis, width=600, height=600)
    scrollable_frame.grid(row=0, column=3, sticky="nsew", padx=0, pady=0)
    scrollable_frame.grid_rowconfigure(0, weight=1)
    scrollable_frame.grid_columnconfigure(0, weight=1)
    label = tkinter.Label(scrollable_frame, text=data)
    label.pack(side="top", fill="x", pady=10)
    button = tkinter.Button(scrollable_frame, text="Guardar Registro", command = lambda: save_data(data, id, sheet), bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10)
    button.pack()
    
    pop_vis.wait_window()



# FUNCIÓN: ESRIBIR DOCUMENTO WORD CON DATOS VISUALIZADOS
def save_data(data, title, sheet):
    doc = docx.Document()
    doc.add_paragraph(data)
    doc.save(sheet +"-" + title + "-" + ".docx")