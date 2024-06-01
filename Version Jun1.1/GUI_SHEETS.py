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
import Humanitario

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
app.attributes('-topmost', True)


# Pestañas
tab = customtkinter.CTkTabview(app, width=620, height=680)
tab.grid(row=0,column=0,sticky="w",padx=50,pady=20)

tab1 = tab.add("Registro General")
rg_instance = General.RegistroGeneral(tab1, workbook, app)

tab2 = tab.add("Registro Legal")
rl_instance = Legal.RegistroLegal(tab2, workbook, app)

tab3 = tab.add("Registro Psicosocial")
rp_instance = Psicosocial.RegistroPsicosocial(tab3, workbook, app)


tab4 = tab.add("Registro Humanitario")
rh_instance = Humanitario.RegistroHumanitario(tab4, workbook, app)

tab5 = tab.add("Visualizar Registros")

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
                                        Global.visualize(workbook, getVText(), dbVEntry.get(), app)) 
submitVBtn.grid(row = 4, column = 0, padx=1,pady=5,ipady=0,sticky="e")


app.mainloop()

