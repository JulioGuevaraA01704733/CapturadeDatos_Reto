""" ARCHIVO SECUNDARIO: Define la interfaz y funcionamiento del registro psicosocial."""



# IMPORTAR: LIBRERÍAS
import customtkinter # Diseño de interfaz

# IMPORTAR: ARCHIVOS    
import Transformations # Transformaciones de variables
import CTkClasses # Clases de (custom)tkinter
import Global # Funciones generalizadas
import encryption # Encriptación de datos

# CLASE: REGISTRO PSICOSOCIAL
class RegistroPsicosocial:
    def __init__(self, tab3, workbook, app):
        self.tab3 = tab3
        self.workbook = workbook
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        # #Componente: Scrollbar
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tab3, width=600, height=600)
        self.scrollable_frame.grid(row=0, column=3, sticky="nsew", padx=0, pady=0)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        
        ## Componentes: Texto, cajas de texto, menus de opción multiple y botones
        n_rows = 0

        self.namesPLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Nombre(s):  ", fg_color = "transparent") # Nombre(s)
        self.namesPLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.namesPEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.namesPEntry.grid(row = n_rows, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "w")
        n_rows += 1

        self.surPPLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Apellido Paterno: ", fg_color = "transparent") # Apellido Paterno
        self.surPPLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.surPPEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.surPPEntry.grid(row = n_rows, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "w")
        n_rows += 1
        
        self.surMPLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Apellido Materno: ", fg_color = "transparent") # Apellida Materno
        self.surMPLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.surMPEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.surMPEntry.grid(row = n_rows, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "w")
        n_rows += 1
        
        self.incLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Inclusión 1era Vez: ", fg_color = "transparent")
        self.incLabel.grid(row = n_rows, column = 0, padx= 1, pady = 5, ipady = 0, sticky = "e")
        
        self.incVar1 = customtkinter.StringVar(value = "No")
        self.incCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Trámite CURP", variable=self.incVar1, onvalue="Sí", offvalue="No")
        self.incCB1.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.incVar2 = customtkinter.StringVar(value = "No")
        self.incCB2 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Obtención RFC", variable=self.incVar2, onvalue="Sí", offvalue="No")
        self.incCB2.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.incVar3 = customtkinter.StringVar(value = "No")
        self.incCB3 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Obtención NSS", variable=self.incVar3, onvalue="Sí", offvalue="No")
        self.incCB3.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.incVar4 = customtkinter.StringVar(value = "No")
        self.incCB4 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Afiliación IMSS", variable=self.incVar4, onvalue="Sí", offvalue="No")
        self.incCB4.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.incVar5 = customtkinter.StringVar(value = "No")
        self.incCB5 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Acceso a vivienda", variable=self.incVar5, onvalue="Sí", offvalue="No")
        self.incCB5.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.incVar6 = customtkinter.StringVar(value = "No")
        self.incCB6 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Apertura Cta. Bancaria", variable=self.incVar6, onvalue="Sí", offvalue="No")
        self.incCB6.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.incVar7 = customtkinter.StringVar(value = "No")
        self.incCB7 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Atención médica (Acompañamiento)", variable=self.incVar7, onvalue="Sí", offvalue="No")
        self.incCB7.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.edLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Educación: ", fg_color = "transparent")
        self.edLabel.grid(row=n_rows, column = 0, padx= 1, pady = 5, ipady = 0, sticky = "e")
        n_rows += 1
        
        self.edVar1 = customtkinter.StringVar(value = "No")
        self.edCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Revalidación de estudios (Acompañamiento)", variable=self.edVar1, onvalue="Sí", offvalue="No")
        self.edCB1.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.edVar2 = customtkinter.StringVar(value = "No")
        self.edCB2 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Vinculación Educativa (Escolaridad obligatoria)", variable=self.edVar2, onvalue="Sí", offvalue="No")
        self.edCB2.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.emLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Empleabilidad: ", fg_color = "transparent")
        self.emLabel.grid(row = n_rows, column = 0, padx= 1, pady = 5, ipady = 0, sticky = "e")
        n_rows += 1
        
        self.emVar1 = customtkinter.StringVar(value = "No")
        self.emCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Capacitación técnica certificada (acompañamiento)", variable=self.emVar1, onvalue="Sí", offvalue="No")
        self.emCB1.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.emVar2 = customtkinter.StringVar(value = "No")
        self.emCB2 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización para recepción de apoyo para la capacitación", variable=self.emVar2, onvalue="Sí", offvalue="No")
        self.emCB2.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.emVar3 = customtkinter.StringVar(value = "No")
        self.emCB3 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Capacitación / Orientación para ingresar al mercado laboral", variable=self.emVar3, onvalue="Sí", offvalue="No")
        self.emCB3.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.emVar4 = customtkinter.StringVar(value = "No")
        self.emCB4 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización a empresa u organización especializada para \nla vinculación laboral", variable=self.emVar4, onvalue="Sí", offvalue="No")
        self.emCB4.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.emVar5 = customtkinter.StringVar(value = "No")
        self.emCB5 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización a una empresa", variable=self.emVar5, onvalue="Sí", offvalue="No")
        self.emCB5.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")        
        n_rows += 1
        
        self.emVar6 = customtkinter.StringVar(value = "No")
        self.emCB6 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización al SNE", variable=self.emVar6, onvalue="Sí", offvalue="No")
        self.emCB6.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")    
        n_rows += 1
        
        self.emVar7 = customtkinter.StringVar(value = "No")
        self.emCB7 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización a una bolsa de empleo", variable=self.emVar7, onvalue="Sí", offvalue="No")
        self.emCB7.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")    
        n_rows += 1
        
        self.emVar8 = customtkinter.StringVar(value = "No")
        self.emCB8 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización a organización especializada para el empleo", variable=self.emVar8, onvalue="Sí", offvalue="No")
        self.emCB8.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")  
        n_rows += 1
        
        self.idpLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Identificación y Protección: ", fg_color = "transparent")
        self.idpLabel.grid(row = n_rows, column = 0, padx= 1, pady = 5, ipady = 0, sticky = "e")
        n_rows += 1
        
        self.idpVar1 = customtkinter.StringVar(value = "No")
        self.idpCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Necesidad específica de protección", variable=self.idpVar1, onvalue="Sí", offvalue="No")
        self.idpCB1.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.smapLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Salud Mental y Apoyo Psicosocial: ", fg_color = "transparent")
        self.smapLabel.grid(row = n_rows, column = 0, padx= 1, pady = 5, ipady = 0, sticky = "e")
        n_rows += 1
        
        self.smapVar1 = customtkinter.StringVar(value = "No")
        self.smapCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Recibieron atención psicológica y psicosocial fuera del \nalbergue", variable=self.smapVar1, onvalue="Sí", offvalue="No")
        self.smapCB1.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.smapVar2 = customtkinter.StringVar(value = "No")
        self.smapCB2 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Identificación de necesidades psicosocial, orientación y \ncanalización", variable=self.smapVar2, onvalue="Sí", offvalue="No")
        self.smapCB2.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.smapVar3 = customtkinter.StringVar(value = "No")
        self.smapCB3 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Acompañamiento para acceso a servicios", variable=self.smapVar3, onvalue="Sí", offvalue="No")
        self.smapCB3.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.smapVar4 = customtkinter.StringVar(value = "No")
        self.smapCB4 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Primeros auxilios psicológicos", variable=self.smapVar4, onvalue="Sí", offvalue="No")
        self.smapCB4.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.smapVar5 = customtkinter.StringVar(value = "No")
        self.smapCB5 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Psicoterapia (individual/familiar)", variable=self.smapVar5, onvalue="Sí", offvalue="No")
        self.smapCB5.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.smapVar6 = customtkinter.StringVar(value = "No")
        self.smapCB6 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Psicoterapia Grupal", variable=self.smapVar6, onvalue="Sí", offvalue="No")
        self.smapCB6.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.smapVar7 = customtkinter.StringVar(value = "No")
        self.smapCB7 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Talleres psicoeducativos", variable=self.smapVar7, onvalue="Sí", offvalue="No")
        self.smapCB7.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.smapVar8 = customtkinter.StringVar(value = "No")
        self.smapCB8 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización a servicios de psiquiatría", variable=self.smapVar8, onvalue="Sí", offvalue="No")
        self.smapCB8.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
        n_rows += 1
        
        self.submitLBtn = customtkinter.CTkButton(self.scrollable_frame, text="Registrar", width=50, command = lambda: new_entry(self.workbook, self.getPText(), self.app))
        self.submitLBtn.grid(row = n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
        n_rows += 1

    ## Función: Obtener datos del registro psicosocial | Lista
    def getPText(self):
        entriesPText = [self.surPPEntry, self.surMPEntry, self.namesPEntry]
        entriesPCheck = [self.incVar1, self.incVar2, self.incVar3, self.incVar4, self.incVar5, self.incVar6, self.incVar7, self.edVar1, 
                         self.edVar2, self.emVar1, self.emVar2, self.emVar3, self.emVar4, self.emVar5, self.emVar6, self.emVar7, 
                         self.emVar8, self.idpVar1, self.smapVar1, self.smapVar2, self.smapVar3, self.smapVar4, self.smapVar5,
                         self.smapVar6, self.smapVar7, self.smapVar8]
        return [entry.get(0.0, "end-1c") for entry in entriesPText] + [entryO.get() for entryO in entriesPCheck]



# FUNCIÓN: REGISTRAR/ACTUALIZAR DATOS EN LA BASE DE DATOS
def new_entry(workbook, entry, GUI):
    id = Transformations.generate_id([Transformations.clean_string(s) for s in entry[:3]]) # Generar: Identificador
    entry = [e if e else "N/a" for e in entry] # Remplazar: Registros vaciós -> "N/a"
    entry = entry[3:] # Eliminar: Nombres
    psi_sheet = workbook.worksheet("Psicosocial") # Seleccionar: Hoja de registro psicosocial
    cols = len(psi_sheet.row_values(1)) # Obtener: Nombres de columna
    psi_ids = psi_sheet.col_values(1) # Obtener: IDs de registros existentes
    
    ## Caso: Identificador inexistente en registro GENERAL o nombres mal escritos
    if id not in psi_ids:
        id2 = Global.similar_entries(id, psi_ids[1:], GUI)
        ### Caso: Identificador inexistente en regsitro GENERAL
        if id2 == id:
            #### Error: Se debe realizar el registro GENERAL antes del PSICOSOCIAL
            CTkClasses.popup_error("Registre al individuo en la\n sección General antes de llevar\n a cabo el registro psicosocial.", GUI)
            return
        ### Caso: Nombres mal escritos
        else: id = id2 # Corregir: Identificador del registro mal escrito(nombres)
    index = psi_ids.index(id) + 1
    existing_row = psi_sheet.row_values(index)[1:] # Obtener: Registro existnte (ya alamacenado)
    ## Caso: Generar nuevo registro    
    if len(existing_row) == 0:
        encrypted_entries = [encryption.encrypt_element(e, "P") for e in entry] # Encriptar datos a registrar
        psi_sheet.update('B{}:{}'.format(index, 'AA' + str(index)), [encrypted_entries]) # Insertar: Registros(encrypted entries) en la fila(index) a partir de la columna B del registro psicosocial(psi_sheet)
    ## Caso: Registro existente    
    else:
        ### Input: Confirmación para actualizar un registro existente
        ver = CTkClasses.verification_popup("El sujeto ya cuenta con\n un registro psicosocial.\n ¿Desea actualizarlo?", GUI)
        ### Caso: Actualizar registro existente
        if ver == 1:
            values_to_update = []
            for i in range(cols - 1):
                if entry[i] != "N/a": # Característica: No se atualizan datos existntes si el nuevo es "N/a"
                    encrypted_entry = encryption.encrypt_element(entry[i], "P") # Encriptar datos a registrar
                    values_to_update.append(encrypted_entry)
                else: values_to_update.append(existing_row[i])
            psi_sheet.update('B{}:{}'.format(index, 'AA' + str(index)), [values_to_update]) # Actualizar: Registros(values_to_update) en el rango B(index)-AA(index) del regitro psicosocial(psi_sheet)
        ### Caso: No actualizar registro existente        
        else: return

