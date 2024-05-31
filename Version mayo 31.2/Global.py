import customtkinter
import os
import Transformations
import decryption
import tkinter
import CTkClasses


""" def popup_error(msg):
    global pop
    pop = customtkinter.CTk()
    pop.title("Error")
    pop.geometry("320x180")
    pop.attributes('-topmost', True)

    label = customtkinter.CTkLabel(pop, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = customtkinter.CTkButton(pop, text="Okay", command=pop.destroy)
    B1.pack()
    pop.mainloop() """

def popup_error(msg, GUI):
    pop = tkinter.Toplevel(GUI)
    pop.title("Error")
    pop.geometry("320x180")
    pop.configure(bg='#2B2B2B') 
    pop.attributes('-topmost', True)
    
    label = tkinter.Label(pop, text=msg, bg='#2B2B2B', fg='white')
    label.pack(side="top", fill="x", pady=10)
    B1 = tkinter.Button(pop, text="Okay", command=pop.destroy, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10)
    B1.pack()
    pop.wait_window()

def popup_visualize(data, GUI):
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
    pop_vis.wait_window()


def visualize(workbook, names, sheet, GUI):
    names = [Transformations.clean_string(s) for s in names]
    id = Transformations.generate_id(names)
    path_dict = {"Legal": "Keys\private_key_L.txt", "Psicosocial": "Keys\private_key_P.txt", "Humanitario": "Keys\private_key_H.txt"}
    headers_dict = {"Legal": ["Orientaciones Legales", "Asesorías legales", "Solicitud de refugiado", "Regularización por razones humanitarias", 
                       "Regularización por unidad familiar", "Cambio de condición de estancia", "Renovaciones", "Reposición de documento migratorio", 
                       "Notificación de cambio de. Domicilio", "Notificación de cambio de nacionalidad", "Notificación de cambio de lugar de trabajo", 
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
    "Salud Mental y Apoyo Psicosocial (Canalización a servicios de psiquiatría)"
]                }
    path = path_dict.get(sheet)
    if os.path.exists(path):
        general_sheet = workbook.worksheet("General")
        specific_sheet = workbook.worksheet(sheet)
        specific_sheet_ids = specific_sheet.col_values(1)
        if id not in specific_sheet_ids: # Registro inexistente
            popup_error("Registro inexistente.", GUI)
        else:
            index = specific_sheet_ids.index(id) + 1
            values = specific_sheet.row_values(index)[1:]
            valuesG = general_sheet.row_values(index)
            headersG = ["ID", "Apellido Paterno", "Apellido Materno", "Nombre(s)", "Edad", "Género", "Nacionalidad"]
            headersS =  headers_dict.get(sheet)
            dispG = "\n\n".join([f"{headersG[i]} : {valuesG[i]}" for i in range(len(headersG)-1)])
            dispS = "\n\n".join([f"{headersS[i]} : {decryption.decrypt_element(values[i], path)}" for i in range(len(values))])
            if "ErrorLlaveIncorrecta" in dispS: # REVISE
                popup_error("Llave Incorrecta \nAcceso no autorizado.", GUI)
                return
            disp = dispG + "\n\n" + dispS
            popup_visualize(disp, GUI)
    else:
        popup_error("No tiene la llave para visualizar\n los registros solicitados.", GUI)
    return








""" def visualize(workbook, names, sheet):
    names = [Transformations.clean_string(s) for s in names]
    id = Transformations.generate_id(names)
    if sheet == "Legal":
        path = "Keys\private_key_L.txt"
    elif sheet == "Psicosocial":
        path = "Keys\private_key_P.txt"
    elif sheet == "Humanitario":
        path = "Keys\private_key_H.txt"
    print(path)
    if os.path.exists(path):
        if id not in workbook.worksheet("General").col_values(1): # Registro inexistente
            popup_error("Registro inexistente.")
        else:
            index = workbook.worksheet(sheet).find(query=id, in_column=1).row
            values = workbook.worksheet(sheet).row_values(index)[1:]
            valuesG = workbook.worksheet("General").row_values(index)
            dispG = ""
            dispS = ""
            for i in range(len(workbook.worksheet("General").row_values(1))-1):
                dispG = dispG + workbook.worksheet("General").row_values(1)[i] + " : " + valuesG[i] + "\n\n"
            for i in range(len(workbook.worksheet(sheet).row_values(index))-1):
                dispS = dispS + workbook.worksheet(sheet).row_values(1)[i] + " : " + decryption.decrypt_element(values[index], path) + "\n\n"
            disp = dispG + dispS
            print(disp)
            # CASO EN EL QUE LA LLAVE ESTÉ INCORRECTA
    else:
        popup_error("No tiene la llave para visualizar\n los registros solicitados.")
    return """