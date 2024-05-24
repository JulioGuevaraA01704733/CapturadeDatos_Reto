import customtkinter
import os
import Transformations
import decryption
import tkinter


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

def popup_visualize(data):
    global pop_vis
    pop_vis = tkinter.Tk()
    pop_vis.title("Visualización")
    pop_vis.geometry("780x780")
    pop_vis.attributes("-topmost", True)
    label = tkinter.Label(pop_vis, text=data)
    label.pack(side="top", fill="x", pady=10)
    pop_vis.mainloop()


def visualize(workbook, names, sheet):
    names = [Transformations.clean_string(s) for s in names]
    id = Transformations.generate_id(names)
    path_dict = {"Legal": "Keys\private_key_L.txt", "Psicosocial": "Keys\private_key_P.txt", "Humanitario": "Keys\private_key_H.txt"}
    headers_dict = {"Legal": ["Orientaciones Legales", "Asesorías legales", "Solicitud de refugiado", "Regularización por razones humanitarias", 
                       "Regularización por unidad familiar", "Cambio de condición de estancia", "Renovaciones", "Reposición de documento migratorio", 
                       "Notificación de cambio de. Domicilio", "Notificación de cambio de nacionalidad", "Notificación de cambio de lugar de trabajo", 
                       "Canalización de las personas migrantes a los consulados de Honduras, Guatemala y el Salvador"],
                "Psicosocial": [
    'Inclusión (Trámite CURP)',
    'Inclusión (Obtención RFC)',
    'Inclusión (Obtención NSS)',
    'Inclusión (Afiliación IMSS)',
    'Inclusión (Acceso a vivienda)',
    'Inclusión (Apertura de Cta. Bancaria)',
    'Inclusión (Atención médica)',
    'Educación (Revalidación de estudios)',
    'Educación (Vinculación educativa)',
    'Empleabilidad (Capacitación técnica certificada)',
    'Empleabilidad (Canalización para recepción de apoyo para la capacitación)',
    'Empleabilidad (Capacitación / Orientación para ingresar al mercado laboral)'
]

                }
    path = path_dict.get(sheet)
    if os.path.exists(path):
        general_sheet = workbook.worksheet("General")
        specific_sheet = workbook.worksheet(sheet)
        specific_sheet_ids = specific_sheet.col_values(1)
        if id not in specific_sheet_ids: # Registro inexistente
            popup_error("Registro inexistente.")
        else:
            index = specific_sheet_ids.index(id) + 1
            values = specific_sheet.row_values(index)[1:]
            valuesG = general_sheet.row_values(index)
            headersG = ["ID", "Apellido Paterno", "Apellido Materno", "Nombre(s)", "Edad", "Género", "Nacionalidad"]
            headersS =  headers_dict.get(sheet)
            dispG = "\n\n".join([f"{headersG[i]} : {valuesG[i]}" for i in range(len(headersG)-1)])
            dispS = "\n\n".join([f"{headersS[i]} : {decryption.decrypt_element(values[i], path)}" for i in range(len(values))])
            if "ErrorLlaveIncorrecta" in dispS:
                popup_error("Llave Incorrecta \nAcceso no autorizado.")
                return
            disp = dispG + "\n\n" + dispS
            popup_visualize(disp)
    else:
        popup_error("No tiene la llave para visualizar\n los registros solicitados.")
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