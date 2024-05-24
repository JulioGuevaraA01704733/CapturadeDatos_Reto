# Importar: Librerías
import gspread
from google.oauth2.service_account import Credentials
import tkinter.filedialog
import customtkinter

# Importar: Archivos
import General
import Legal
import CTkClasses
import Global
import Transformations
import Psicosocial

# Conectar a google sheets
scopes = ["https://www.googleapis.com/auth/spreadsheets"] 
creds = Credentials.from_service_account_file("Keys/credentials.json", scopes = scopes)
client = gspread.authorize(creds)

workbook_id = "1HewbEoj2xByzpHS4Td9nD-uqubhSD0-Hi-pfu0dnQQI" # Archivo: Google Sheets | Base datos | ID
workbook = client.open_by_key(workbook_id)

# Inicializar: Interfaz
app = customtkinter.CTk()
app.title("Encriptación de Base de Datos")
app.geometry("720x780")

# Pestañas
tab = customtkinter.CTkTabview(app, width=620, height=680)
tab.grid(row=0,column=0,sticky="w",padx=50,pady=20)

tab1 = tab.add("Registro General")
tab2 = tab.add("Registro Legal")
tab3 = tab.add("Registro Psicosocial")
tab4 = tab.add("Registro Humanitario")
tab5 = tab.add("Visualizar Registros")

# Pestaña: Registro General
def getGText(): # Obtener Registros
    entriesGText = [surPGEntry, surMGEntry, namesGEntry, ageGEntry]
    entriesGOption = [genderGEntry, nationalityGEntry]
    entry = [entryT.get(0.0, "end-1c") for entryT in entriesGText] + [entryO.get() for entryO in entriesGOption]
    print(entry)
    return entry

namesGLabel = customtkinter.CTkLabel(tab1, text = "Nombre(s):  ", fg_color = "transparent") # Nombre(s)
namesGLabel.grid(row = 0, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
namesGEntry = customtkinter.CTkTextbox(tab1, width = 300, height = 10)
namesGEntry.grid(row = 0, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")

surPGLabel = customtkinter.CTkLabel(tab1, text = "Apellido Paterno: ", fg_color = "transparent") # Apellido Paterno
surPGLabel.grid(row = 1, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
surPGEntry = customtkinter.CTkTextbox(tab1, width = 300, height = 10)
surPGEntry.grid(row = 1, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")

surMGLabel = customtkinter.CTkLabel(tab1, text = "Apellido Materno: ", fg_color = "transparent") # Apellida Materno
surMGLabel.grid(row = 2, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
surMGEntry = customtkinter.CTkTextbox(tab1, width = 300, height = 10)
surMGEntry.grid(row = 2, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")

ageGLabel = customtkinter.CTkLabel(tab1, text = "Edad:  ", fg_color = "transparent") # Edad
ageGLabel.grid(row = 3, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
ageGEntry = customtkinter.CTkTextbox(tab1, width = 300, height = 10)
ageGEntry.grid(row=3, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")

genderGLabel = customtkinter.CTkLabel(tab1, text = "Género:  ", fg_color = "transparent") # Género
genderGLabel.grid(row = 4, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
genderGEntry = customtkinter.CTkOptionMenu(tab1, values = ["Hombre", "Mujer", "Hombre LGBTTTIQ+", "Mujer LGBTTTIQ+"])
genderGEntry.grid(row = 4, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")

nationalityGLabel = customtkinter.CTkLabel(tab1, text="Nacionalidad:  ", fg_color="transparent") # Nacionalidad
nationalityGLabel.grid(row=5, column = 0, padx=1,pady=5,ipady=0,sticky="e")
nationalityGEntry = customtkinter.CTkOptionMenu(tab1, values=["México", "Estados Unidos de America", "Guatemala", "Honduras", 
                                                              "El Salvador", "Venezuela", "Nicaragua", "Haití", "Colombia", "Cuba", 
                                                              "Argentina", "Afganistan", "Siria", "Alemania", "Brasil", "Perú", 
                                                              "Guayana Francesa", "Belice", "Panamá", "Ecuador"])
nationalityGEntry.grid(row=5, column = 1, padx=1,pady=5,ipady=0,sticky="e")

submitGBtn = customtkinter.CTkButton(tab1, text="Registrar", width=50, command = lambda: # Registrar
                                     General.new_entry(workbook, getGText(), app)) 
submitGBtn.grid(row = 7, column = 0, padx=1,pady=5,ipady=0,sticky="e")



# Pestaña: Registro Legal
def getLText():
    entriesLText = [surPLEntry, surMLEntry, namesLEntry, L2Entry, L3Entry, L4Entry, L5Entry, L6Entry, L7Entry, L8Entry, L9Entry, L10Entry, L11Entry, L12Entry, L13Entry]
    return [entry.get(0.0, "end-1c") for entry in entriesLText]

namesLLabel = customtkinter.CTkLabel(tab2, text = "Nombre(s):  ", fg_color = "transparent") # Nombre(s)
namesLLabel.grid(row = 0, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
namesLEntry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
namesLEntry.grid(row = 0, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")

surPLLabel = customtkinter.CTkLabel(tab2, text = "Apellido Paterno: ", fg_color = "transparent") # Apellido Paterno
surPLLabel.grid(row = 1, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
surPLEntry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
surPLEntry.grid(row = 1, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")

surMLLabel = customtkinter.CTkLabel(tab2, text = "Apellido Materno: ", fg_color = "transparent") # Apellida Materno
surMLLabel.grid(row = 2, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
surMLEntry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
surMLEntry.grid(row = 2, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")

L2Label = customtkinter.CTkLabel(tab2, text="Orientaciones Legales:  ", fg_color="transparent")
L2Label.grid(row=3, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L2Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L2Entry.grid(row=3, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L3Label = customtkinter.CTkLabel(tab2, text="Asesorías Legales:  ", fg_color="transparent")
L3Label.grid(row=4, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L3Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L3Entry.grid(row=4, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L4Label = customtkinter.CTkLabel(tab2, text="Solicitud de Refugiado:  ", fg_color="transparent")
L4Label.grid(row=5, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L4Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L4Entry.grid(row=5, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L5Label = customtkinter.CTkLabel(tab2, text="Regularización por Razones Humanitarias:  ", fg_color="transparent")
L5Label.grid(row=6, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L5Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L5Entry.grid(row=6, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L6Label = customtkinter.CTkLabel(tab2, text="Regularización por Unidad Familiar:  ", fg_color="transparent")
L6Label.grid(row=7, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L6Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L6Entry.grid(row=7, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L7Label = customtkinter.CTkLabel(tab2, text="Cambio de Condición de Estancia:  ", fg_color="transparent")
L7Label.grid(row=8, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L7Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L7Entry.grid(row=8, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L8Label = customtkinter.CTkLabel(tab2, text="Renovaciones:  ", fg_color="transparent")
L8Label.grid(row=9, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L8Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L8Entry.grid(row=9, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L9Label = customtkinter.CTkLabel(tab2, text="Resposición de Documento Migratorio:  ", fg_color="transparent")
L9Label.grid(row=10, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L9Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L9Entry.grid(row=10, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L10Label = customtkinter.CTkLabel(tab2, text="Notificación de Cambio de Domicilio:  ", fg_color="transparent")
L10Label.grid(row=11, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L10Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L10Entry.grid(row=11, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L11Label = customtkinter.CTkLabel(tab2, text="Notificación de Cambio de Nacionalidad:  ", fg_color="transparent")
L11Label.grid(row=12, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L11Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L11Entry.grid(row=12, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L12Label = customtkinter.CTkLabel(tab2, text="Notificación de Cambio de Lugar de Trabajo:  ", fg_color="transparent")
L12Label.grid(row=13, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L12Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L12Entry.grid(row=13, column = 1, padx=1,pady=5,ipady=0,sticky="e")

L13Label = customtkinter.CTkLabel(tab2, text="Canalización de las Personas Migrantes a \nlos consulados de Honduras, \nGuatemala y el Salvador:  ", fg_color="transparent")
L13Label.grid(row=14, column = 0, padx=1,pady=5,ipady=0,sticky="e")
L13Entry = customtkinter.CTkTextbox(tab2, width = 300, height = 10)
L13Entry.grid(row=14, column = 1, padx=1,pady=5,ipady=0,sticky="e")

submitLBtn = customtkinter.CTkButton(tab2, text="Registrar", width=50, command = lambda: Legal.new_entry(workbook, getLText(), app))
submitLBtn.grid(row = 15, column = 0, padx=1,pady=5,ipady=0,sticky="e")


# Pestaña: Psicosocial
def getPText():
    entriesPText = [surPPEntry, surMPEntry, namesPEntry, P2Entry, P3Entry, P4Entry, P5Entry, P6Entry, P7Entry, P8Entry, P9Entry, P10Entry, P11Entry, P12Entry, P13Entry]
    return [entry.get(0.0, "end-1c") for entry in entriesPText]

namesPLabel = customtkinter.CTkLabel(tab3, text = "Nombre(s):  ", fg_color = "transparent") # Nombre(s)
namesPLabel.grid(row = 0, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
namesPEntry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
namesPEntry.grid(row = 0, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")

surPPLabel = customtkinter.CTkLabel(tab3, text = "Apellido Paterno: ", fg_color = "transparent") # Apellido Paterno
surPPLabel.grid(row = 1, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
surPPEntry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
surPPEntry.grid(row = 1, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")

surMPLabel = customtkinter.CTkLabel(tab3, text = "Apellido Materno: ", fg_color = "transparent") # Apellida Materno
surMPLabel.grid(row = 2, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
surMPEntry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
surMPEntry.grid(row = 2, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")

P2Label = customtkinter.CTkLabel(tab3, text="Inclusión (Trámite CURP):  ", fg_color="transparent")
P2Label.grid(row=3, column = 0, padx=1,pady=5,ipady=0,sticky="e")
P2Entry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
P2Entry.grid(row=3, column = 1, padx=1,pady=5,ipady=0,sticky="e")

P3Label = customtkinter.CTkLabel(tab3, text="Inclusión (Obtención RFC):  ", fg_color="transparent")
P3Label.grid(row=4, column = 0, padx=1,pady=5,ipady=0,sticky="e")
P3Entry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
P3Entry.grid(row=4, column = 1, padx=1,pady=5,ipady=0,sticky="e")

P4Label = customtkinter.CTkLabel(tab3, text="Inclusión (Obtención NSS):  ", fg_color="transparent")
P4Label.grid(row=5, column = 0, padx=1,pady=5,ipady=0,sticky="e")
P4Entry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
P4Entry.grid(row=5, column = 1, padx=1,pady=5,ipady=0,sticky="e")

P5Label = customtkinter.CTkLabel(tab3, text="Inclusión (Afiliación IMSS):  ", fg_color="transparent")
P5Label.grid(row=6, column = 0, padx=1,pady=5,ipady=0,sticky="e")
P5Entry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
P5Entry.grid(row=6, column = 1, padx=1,pady=5,ipady=0,sticky="e")

P6Label = customtkinter.CTkLabel(tab3, text="Inclusión (Acceso a vivienda):  ", fg_color="transparent")
P6Label.grid(row=7, column = 0, padx=1,pady=5,ipady=0,sticky="e")
P6Entry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
P6Entry.grid(row=7, column = 1, padx=1,pady=5,ipady=0,sticky="e")

P7Label = customtkinter.CTkLabel(tab3, text="Inclusión (Apertura de Cta. Bancaria):  ", fg_color="transparent")
P7Label.grid(row=8, column = 0, padx=1,pady=5,ipady=0,sticky="e")
P7Entry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
P7Entry.grid(row=8, column = 1, padx=1,pady=5,ipady=0,sticky="e")

P8Label = customtkinter.CTkLabel(tab3, text="Inclusión (Atención médica):  ", fg_color="transparent")
P8Label.grid(row=9, column = 0, padx=1,pady=5,ipady=0,sticky="e")
P8Entry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
P8Entry.grid(row=9, column = 1, padx=1,pady=5,ipady=0,sticky="e")

P9Label = customtkinter.CTkLabel(tab3, text="Educación (Revalidación de estudios):  ", fg_color="transparent")
P9Label.grid(row=10, column = 0, padx=1,pady=5,ipady=0,sticky="e")
P9Entry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
P9Entry.grid(row=10, column = 1, padx=1,pady=5,ipady=0,sticky="e")

P10Label = customtkinter.CTkLabel(tab3, text="Educación (Vinculación educativa):  ", fg_color="transparent")
P10Label.grid(row=11, column = 0, padx=1,pady=5,ipady=0,sticky="e")
P10Entry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
P10Entry.grid(row=11, column = 1, padx=1,pady=5,ipady=0,sticky="e")

P11Label = customtkinter.CTkLabel(tab3, text="Empleabilidad (Capacitación técnica certificada):  ", fg_color="transparent")
P11Label.grid(row=12, column = 0, padx=1,pady=5,ipady=0,sticky="e")
P11Entry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
P11Entry.grid(row=12, column = 1, padx=1,pady=5,ipady=0,sticky="e")

P12Label = customtkinter.CTkLabel(tab3, text="Empleabilidad (Canalización para recepción de \napoyo para la capacitación):  ", fg_color="transparent")
P12Label.grid(row=13, column = 0, padx=1,pady=5,ipady=0,sticky="e")
P12Entry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
P12Entry.grid(row=13, column = 1, padx=1,pady=5,ipady=0,sticky="e")

P13Label = customtkinter.CTkLabel(tab3, text="Empleabilidad (Capacitación / Orientación para \ningresar al mercado laboral):  ", fg_color="transparent")
P13Label.grid(row=14, column = 0, padx=1,pady=5,ipady=0,sticky="e")
P13Entry = customtkinter.CTkTextbox(tab3, width = 300, height = 10)
P13Entry.grid(row=14, column = 1, padx=1,pady=5,ipady=0,sticky="e")

submitPBtn = customtkinter.CTkButton(tab3, text="Registrar", width=50, command = lambda: Psicosocial.new_entry(workbook, getPText(), app))
submitPBtn.grid(row = 15, column = 0, padx=1,pady=5,ipady=0,sticky="e")




# Pestaña: Visaulizar
def getVText():
    entriesVText = [surPVEntry, surMVEntry, namesVEntry]
    entry = [entryT.get(0.0, "end-1c") for entryT in entriesVText]
    return entry

namesVLabel = customtkinter.CTkLabel(tab5, text = "Nombre(s):  ", fg_color = "transparent") # Nombre(s)
namesVLabel.grid(row = 0, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
namesVEntry = customtkinter.CTkTextbox(tab5, width = 300, height = 10)
namesVEntry.grid(row = 0, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")

surPVLabel = customtkinter.CTkLabel(tab5, text = "Apellido Paterno: ", fg_color = "transparent") # Apellido Paterno
surPVLabel.grid(row = 1, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
surPVEntry = customtkinter.CTkTextbox(tab5, width = 300, height = 10)
surPVEntry.grid(row = 1, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")

surMVLabel = customtkinter.CTkLabel(tab5, text = "Apellido Materno: ", fg_color = "transparent") # Apellida Materno
surMVLabel.grid(row = 2, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
surMVEntry = customtkinter.CTkTextbox(tab5, width = 300, height = 10)
surMVEntry.grid(row = 2, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")

dbVLabel = customtkinter.CTkLabel(tab5, text = "Registros a Visualizar:  ", fg_color = "transparent") # Género
dbVLabel.grid(row = 3, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
dbVEntry = customtkinter.CTkOptionMenu(tab5, values = ["Legal", "Psicosocial", "Humanitario"])
dbVEntry.grid(row = 3, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")

submitVBtn = customtkinter.CTkButton(tab5, text="Visualizar", width=50, command = lambda: # Registrar
                                        Global.visualize(workbook, getVText(), dbVEntry.get())) 
submitVBtn.grid(row = 4, column = 0, padx=1,pady=5,ipady=0,sticky="e")


app.mainloop()

