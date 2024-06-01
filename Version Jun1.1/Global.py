import customtkinter
import os
import Transformations
import decryption
import tkinter
import CTkClasses
import re
import docx
from difflib import SequenceMatcher


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

def save_data(data, title, sheet):
    doc = docx.Document()
    doc.add_paragraph(data)
    doc.save(sheet +"-" + title + "-" + ".docx")

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
],
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
]                }
    path = path_dict.get(sheet)
    if os.path.exists(path):
        general_sheet = workbook.worksheet("General")
        specific_sheet = workbook.worksheet(sheet)
        specific_sheet_ids = specific_sheet.col_values(1)
        if id not in specific_sheet_ids: # Registro inexistente
            id2 = similar_entries(id, specific_sheet_ids[1:], GUI)
            if id2 == id:
                CTkClasses.popup_error("Registro Inexistente", GUI)
                return
            else: id = id2        
        index = specific_sheet_ids.index(id) + 1
        values = specific_sheet.row_values(index)[1:]
        valuesG = general_sheet.row_values(index)
        headersG = ["ID", "Apellido Paterno", "Apellido Materno", "Nombre(s)", "Fecha de Nacimiento", "Edad al Momento del Registro", "Género", "Nacionalidad", "Departamento/Estado", "Fecha de Registro", "Número Telefónico de Contacto"]
        headersS =  headers_dict.get(sheet)
        dispG = "\n\n".join([f"{headersG[i]} : {valuesG[i]}" for i in range(len(headersG)-1)])
        dispS = "\n\n".join([f"{headersS[i]} : {decryption.decrypt_element(values[i], path)}" for i in range(len(values))])
        if "ErrorLlaveIncorrecta" in dispS: # REVISE
            popup_error("Llave Incorrecta \nAcceso no autorizado.", GUI)
            return
        disp = dispG + "\n\n" + dispS
        popup_visualize(disp, GUI, id, sheet)
    else:
        popup_error("No tiene la llave para visualizar\n los registros solicitados.", GUI)
    return


""" def similar_entries(id, ids, GUI):
    prefix = id.split("-")[0]
    similar_ids = [item for item in ids if item.startswith(prefix)]
    if len(similar_ids) != 0:
        similar_names = []
        for name in similar_ids:
            name = name.split("-")[1:]
            name = "".join(name)
            name = name.replace("_", "")
            name = re.findall('[A-Z][^A-Z]*', name)    
            first_element = name.pop(0)
            name.append(first_element)  
            second_element = name.pop(0)
            name.append(second_element)   
            name = " ".join(name)
            similar_names.append(name)
        global value
        value = None
        def on_ok():
            global value
            value = similar_ids[similar_names.index(namesEntry.get())]
            popup.destroy()

        def on_cancel():
            global value
            value = id
            popup.destroy()
        popup = tkinter.Toplevel(GUI)  # Use the app (main window) as the parent

        popup.title("Registro Similar")
        popup.geometry("420x180")
        popup.configure(bg='#2B2B2B') 
        popup.attributes('-topmost', True)

        queryLabel = tkinter.Label(popup, text="¿Quiso escribir alguno de los\n siguientes nombres?", bg='#2B2B2B', fg='white', font=(tkinter.font, 12))
        queryLabel.pack(padx=10, pady=10)

        namesEntry = customtkinter.CTkOptionMenu(popup, values=similar_names)
        namesEntry.pack(padx=10, pady=10,)

        ok_button = tkinter.Button(popup, text="Sí", command=on_ok, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10, font=(tkinter.font, 12))
        ok_button.pack(side=tkinter.LEFT, padx=10, pady=5)

        cancel_button = tkinter.Button(popup, text="No", command=on_cancel, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10, font=(tkinter.font, 12))
        cancel_button.pack(side=tkinter.RIGHT, padx=10, pady=5)

        popup.wait_window()
    return value """


def similar_entries(id, ids, GUI):
    prefix = id.split("-")[0]
    similar_ids = [item for item in ids if item.startswith(prefix)]
    similar_ids = [item for item in similar_ids if SequenceMatcher(None, item, id).ratio() >= 0.8]
    if len(similar_ids) != 0:
        similar_names = []
        for name in similar_ids:
            name = name.split("-")[1:]
            name = "".join(name)
            name = name.replace("_", "")
            name = re.findall('[A-Z][^A-Z]*', name)    
            first_element = name.pop(0)
            name.append(first_element)  
            second_element = name.pop(0)
            name.append(second_element)   
            name = " ".join(name)
            similar_names.append(name)
        global value
        value = id
        def on_ok():
            global value
            value = similar_ids[similar_names.index(namesEntry.get())]
            popup.destroy()

        def on_cancel():
            global value
            value = None
            popup.destroy()
        popup = tkinter.Toplevel(GUI)  # Use the app (main window) as the parent

        popup.title("Registro Similar")
        popup.geometry("420x180")
        popup.configure(bg='#2B2B2B') 
        popup.attributes('-topmost', True)

        queryLabel = tkinter.Label(popup, text="¿Quiso escribir alguno de los\n siguientes nombres?", bg='#2B2B2B', fg='white', font=(tkinter.font, 12))
        queryLabel.pack(padx=10, pady=10)

        namesEntry = customtkinter.CTkOptionMenu(popup, values=similar_names)
        namesEntry.pack(padx=10, pady=10,)

        ok_button = tkinter.Button(popup, text="Sí", command=on_ok, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10, font=(tkinter.font, 12))
        ok_button.pack(side=tkinter.LEFT, padx=10, pady=5)

        cancel_button = tkinter.Button(popup, text="No", command=on_cancel, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10, font=(tkinter.font, 12))
        cancel_button.pack(side=tkinter.RIGHT, padx=10, pady=5)

        popup.wait_window()
        return value
    else: return id


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