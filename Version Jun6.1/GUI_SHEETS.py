""" ARCHIVO PRINCIPAL: Establce la conexión a la base de datos en Google Sheets y genera (ejecuta) la interfáz."""



# IMPORTAR: LIBRERÍAS
## Manejo de Google Sheets
import gspread
from google.oauth2.service_account import Credentials
## Diseño de interfaz
import customtkinter

# IMPORTAR: ARCHIVOS
import General # Registro general
import Legal # Registro legal
import Psicosocial # Registro psicosocial
import Humanitario # Registro humanitario
import Visualize # Visualizar registros



# CONEXIÓN: Google Sheets
scopes = ["https://www.googleapis.com/auth/spreadsheets"] # APIs
creds = Credentials.from_service_account_file("Keys/credentials.json", scopes = scopes) # Archivo: Credenciales
client = gspread.authorize(creds)

workbook_id = "1HewbEoj2xByzpHS4Td9nD-uqubhSD0-Hi-pfu0dnQQI" # Archivo: Google Sheets | Base datos | ID
workbook = client.open_by_key(workbook_id)



# INICIALIZAR: INTERFAZ
app = customtkinter.CTk()
app.title("Encriptación de Base de Datos")
app.geometry("720x780")
app.attributes('-topmost', True)
app.update()
app.attributes('-topmost', False)

## Inicializar: Pestañas
tab = customtkinter.CTkTabview(app, width=620, height=680)
tab.grid(row=0,column=0,sticky="w",padx=50,pady=20)

## Pestaña: Registro General
tab1 = tab.add("Registro General")
rg_instance = General.RegistroGeneral(tab1, workbook, app)

## Pestaña: Registro Legal
tab2 = tab.add("Registro Legal")
rl_instance = Legal.RegistroLegal(tab2, workbook, app)

## Pestaña: Registro Psicosocial
tab3 = tab.add("Registro Psicosocial")
rp_instance = Psicosocial.RegistroPsicosocial(tab3, workbook, app)

## Pestaña: Registro Humanitario
tab4 = tab.add("Registro Humanitario")
rh_instance = Humanitario.RegistroHumanitario(tab4, workbook, app)

## Pestaña: Visualizar Registros
tab5 = tab.add("Visualizar Registros")
v_instance = Visualize.Visualizar(tab5, workbook, app)


# GENERAR: INTERFAZ
app.mainloop()

