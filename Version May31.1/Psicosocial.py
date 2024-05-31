import encryption
import Transformations
import customtkinter
import CTkClasses
import tkinter
import Global

class RegistroPsicosocial:
    def __init__(self, tab3, workbook, app):
        self.tab3 = tab3
        self.workbook = workbook
        self.app = app
        self.create_widgets()

    def create_widgets(self):
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tab3, width=600, height=600)
        self.scrollable_frame.grid(row=0, column=3, sticky="nsew", padx=0, pady=0)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        
        self.namesPLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Nombre(s):  ", fg_color = "transparent") # Nombre(s)
        self.namesPLabel.grid(row = 0, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.namesPEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.namesPEntry.grid(row = 0, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "w")

        self.surPPLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Apellido Paterno: ", fg_color = "transparent") # Apellido Paterno
        self.surPPLabel.grid(row = 1, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.surPPEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.surPPEntry.grid(row = 1, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "w")

        self.surMPLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Apellido Materno: ", fg_color = "transparent") # Apellida Materno
        self.surMPLabel.grid(row = 2, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
        self.surMPEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
        self.surMPEntry.grid(row = 2, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "w")

        self.incLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Inclusión 1era Vez: ", fg_color = "transparent")
        self.incLabel.grid(row = 3, column = 0, padx= 1, pady = 5, ipady = 0, sticky = "e")

        self.incVar1 = customtkinter.StringVar(value = "No")
        self.incCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Trámite CURP", variable=self.incVar1, onvalue="Sí", offvalue="No")
        self.incCB1.grid(row=4, column=1, padx=1, pady=5, sticky="w")

        self.incVar2 = customtkinter.StringVar(value = "No")
        self.incCB2 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Obtención RFC", variable=self.incVar2, onvalue="Sí", offvalue="No")
        self.incCB2.grid(row=5, column=1, padx=1, pady=5, sticky="w")

        self.incVar3 = customtkinter.StringVar(value = "No")
        self.incCB3 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Obtención NSS", variable=self.incVar3, onvalue="Sí", offvalue="No")
        self.incCB3.grid(row=6, column=1, padx=1, pady=5, sticky="w")

        self.incVar4 = customtkinter.StringVar(value = "No")
        self.incCB4 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Afiliación IMSS", variable=self.incVar4, onvalue="Sí", offvalue="No")
        self.incCB4.grid(row=7, column=1, padx=1, pady=5, sticky="w")

        self.incVar5 = customtkinter.StringVar(value = "No")
        self.incCB5 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Acceso a vivienda", variable=self.incVar5, onvalue="Sí", offvalue="No")
        self.incCB5.grid(row=8, column=1, padx=1, pady=5, sticky="w")

        self.incVar6 = customtkinter.StringVar(value = "No")
        self.incCB6 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Apertura Cta. Bancaria", variable=self.incVar6, onvalue="Sí", offvalue="No")
        self.incCB6.grid(row=9, column=1, padx=1, pady=5, sticky="w")

        self.incVar7 = customtkinter.StringVar(value = "No")
        self.incCB7 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Atención médica (Acompañamiento)", variable=self.incVar7, onvalue="Sí", offvalue="No")
        self.incCB7.grid(row=10, column=1, padx=1, pady=5, sticky="w")

        self.edLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Educación: ", fg_color = "transparent")
        self.edLabel.grid(row = 11, column = 0, padx= 1, pady = 5, ipady = 0, sticky = "e")

        self.edVar1 = customtkinter.StringVar(value = "No")
        self.edCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Revalidación de estudios (Acompañamiento)", variable=self.edVar1, onvalue="Sí", offvalue="No")
        self.edCB1.grid(row=12, column=1, padx=1, pady=5, sticky="w")

        self.edVar2 = customtkinter.StringVar(value = "No")
        self.edCB2 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Vinculación Educativa (Escolaridad obligatoria)", variable=self.edVar2, onvalue="Sí", offvalue="No")
        self.edCB2.grid(row=13, column=1, padx=1, pady=5, sticky="w")

        self.emLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Empleabilidad: ", fg_color = "transparent")
        self.emLabel.grid(row = 14, column = 0, padx= 1, pady = 5, ipady = 0, sticky = "e")

        self.emVar1 = customtkinter.StringVar(value = "No")
        self.emCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Capacitación técnica certificada (acompañamiento)", variable=self.emVar1, onvalue="Sí", offvalue="No")
        self.emCB1.grid(row=15, column=1, padx=1, pady=5, sticky="w")

        self.emVar2 = customtkinter.StringVar(value = "No")
        self.emCB2 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización para recepción de apoyo para la capacitación", variable=self.emVar2, onvalue="Sí", offvalue="No")
        self.emCB2.grid(row=16, column=1, padx=1, pady=5, sticky="w")

        self.emVar3 = customtkinter.StringVar(value = "No")
        self.emCB3 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Capacitación / Orientación para ingresar al mercado laboral", variable=self.emVar3, onvalue="Sí", offvalue="No")
        self.emCB3.grid(row=17, column=1, padx=1, pady=5, sticky="w")

        self.emVar4 = customtkinter.StringVar(value = "No")
        self.emCB4 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización a empresa u organización especializada para \nla vinculación laboral", variable=self.emVar4, onvalue="Sí", offvalue="No")
        self.emCB4.grid(row=18, column=1, padx=1, pady=5, sticky="w")

        self.emVar5 = customtkinter.StringVar(value = "No")
        self.emCB5 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización a una empresa", variable=self.emVar5, onvalue="Sí", offvalue="No")
        self.emCB5.grid(row=19, column=1, padx=1, pady=5, sticky="w")        

        self.emVar6 = customtkinter.StringVar(value = "No")
        self.emCB6 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización al SNE", variable=self.emVar6, onvalue="Sí", offvalue="No")
        self.emCB6.grid(row=20, column=1, padx=1, pady=5, sticky="w")    

        self.emVar7 = customtkinter.StringVar(value = "No")
        self.emCB7 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización a una bolsa de empleo", variable=self.emVar7, onvalue="Sí", offvalue="No")
        self.emCB7.grid(row=21, column=1, padx=1, pady=5, sticky="w")    

        self.emVar8 = customtkinter.StringVar(value = "No")
        self.emCB8 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización a organización especializada para el empleo", variable=self.emVar8, onvalue="Sí", offvalue="No")
        self.emCB8.grid(row=22, column=1, padx=1, pady=5, sticky="w")  

        self.idpLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Identificación y Protección: ", fg_color = "transparent")
        self.idpLabel.grid(row = 23, column = 0, padx= 1, pady = 5, ipady = 0, sticky = "e")

        self.idpVar1 = customtkinter.StringVar(value = "No")
        self.idpCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Necesidad específica de protección", variable=self.idpVar1, onvalue="Sí", offvalue="No")
        self.idpCB1.grid(row=24, column=1, padx=1, pady=5, sticky="w")

        self.smapLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Salud Mental y Apoyo Psicosocial: ", fg_color = "transparent")
        self.smapLabel.grid(row = 25, column = 0, padx= 1, pady = 5, ipady = 0, sticky = "e")

        self.smapVar1 = customtkinter.StringVar(value = "No")
        self.smapCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Recibieron atención psicológica y psicosocial fuera del \nalbergue", variable=self.smapVar1, onvalue="Sí", offvalue="No")
        self.smapCB1.grid(row=26, column=1, padx=1, pady=5, sticky="w")

        self.smapVar2 = customtkinter.StringVar(value = "No")
        self.smapCB2 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Identificación de necesidades psicosocial, orientación y \ncanalización", variable=self.smapVar2, onvalue="Sí", offvalue="No")
        self.smapCB2.grid(row=27, column=1, padx=1, pady=5, sticky="w")

        self.smapVar3 = customtkinter.StringVar(value = "No")
        self.smapCB3 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Acompañamiento para acceso a servicios", variable=self.smapVar3, onvalue="Sí", offvalue="No")
        self.smapCB3.grid(row=28, column=1, padx=1, pady=5, sticky="w")

        self.smapVar4 = customtkinter.StringVar(value = "No")
        self.smapCB4 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Primeros auxilios psicológicos", variable=self.smapVar4, onvalue="Sí", offvalue="No")
        self.smapCB4.grid(row=29, column=1, padx=1, pady=5, sticky="w")

        self.smapVar5 = customtkinter.StringVar(value = "No")
        self.smapCB5 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Psicoterapia (individual/familiar)", variable=self.smapVar5, onvalue="Sí", offvalue="No")
        self.smapCB5.grid(row=30, column=1, padx=1, pady=5, sticky="w")

        self.smapVar6 = customtkinter.StringVar(value = "No")
        self.smapCB6 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Psicoterapia Grupal", variable=self.smapVar6, onvalue="Sí", offvalue="No")
        self.smapCB6.grid(row=31, column=1, padx=1, pady=5, sticky="w")

        self.smapVar7 = customtkinter.StringVar(value = "No")
        self.smapCB7 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Talleres psicoeducativos", variable=self.smapVar7, onvalue="Sí", offvalue="No")
        self.smapCB7.grid(row=32, column=1, padx=1, pady=5, sticky="w")

        self.smapVar8 = customtkinter.StringVar(value = "No")
        self.smapCB8 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización a servicios de psiquiatría", variable=self.smapVar8, onvalue="Sí", offvalue="No")
        self.smapCB8.grid(row=33, column=1, padx=1, pady=5, sticky="w")

        self.submitLBtn = customtkinter.CTkButton(self.scrollable_frame, text="Registrar", width=50, command = lambda: new_entry(self.workbook, self.getPText(), self.app))
        self.submitLBtn.grid(row = 34, column = 0, padx=1,pady=5,ipady=0,sticky="e")

    def getPText(self):
        entriesPText = [self.surPPEntry, self.surMPEntry, self.namesPEntry]
        entriesPCheck = [self.incVar1, self.incVar2, self.incVar3, self.incVar4, self.incVar5, self.incVar6, self.incVar7, self.edVar1, 
                         self.edVar2, self.emVar1, self.emVar2, self.emVar3, self.emVar4, self.emVar5, self.emVar6, self.emVar7, 
                         self.emVar8, self.idpVar1, self.smapVar1, self.smapVar2, self.smapVar3, self.smapVar4, self.smapVar5,
                         self.smapVar6, self.smapVar7, self.smapVar8]
        return [entry.get(0.0, "end-1c") for entry in entriesPText] + [entryO.get() for entryO in entriesPCheck]

def test(data):
    print(data)

def new_entry(workbook, entry, GUI):
    global ver
    id = Transformations.generate_id([Transformations.clean_string(s) for s in entry[:3]])
    entry = [e if e else "N/a" for e in entry]
    entry = entry[3:]
    psi_sheet = workbook.worksheet("Psicosocial")
    cols = len(psi_sheet.row_values(1)) # MANUAL
    psi_ids = psi_sheet.col_values(1)
    if id not in psi_ids: # Registro no existente
        id2 = Global.similar_entries(id, psi_ids[1:], GUI)
        if id2 == id:
            CTkClasses.popup_error("Registre al individuo en la\n sección General antes de llevar\n a cabo el registro psicosocial.", GUI)
            return
        else: id = id2
    index = psi_ids.index(id) + 1
    existing_row = psi_sheet.row_values(index)[1:]
    if len(existing_row) == 0:  # Agregar registro Psicosocial
        encrypted_entries = [encryption.encrypt_element(e, "P") for e in entry]
        psi_sheet.update('B{}:{}'.format(index, 'AA' + str(index)), [encrypted_entries])  # Actualizar registro
    else:
        ver = CTkClasses.verification_popup("El sujeto ya cuenta con\n un registro psicosocial.\n ¿Desea actualizarlo?", GUI)
        #GUI.wait_window(pop)
        if ver == 1:  # Actualizar registro Legal
            values_to_update = []
            for i in range(cols - 1):
                if entry[i] != "N/a":
                    encrypted_entry = encryption.encrypt_element(entry[i], "P")
                    values_to_update.append(encrypted_entry)
                else: values_to_update.append(existing_row[i])
            psi_sheet.update('B{}:{}'.format(index, 'AA' + str(index)), [values_to_update])
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
    no_button.pack() """