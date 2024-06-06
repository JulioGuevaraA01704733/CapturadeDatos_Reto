""" ARCHIVO AUXILIAR: Almacena clases de interfaces tkinter generalizas utilizadas en múltiples documentos."""



# IMPORTAR: LIBRERÍAS
import tkinter as tk # Diseño de interfaz



# CLASE: VENTANA EMERGENTA PARA SOLICITAR UNA CONFIRMACIÓN POR PARTE DEL USUARIO | Binario
def verification_popup(string, GUI):
    global value
    value = None

    ## Caso: Si se confirma
    def on_ok():
        global value
        value = 1
        popup.destroy()

    ## Caso: No se confirma
    def on_cancel():
        global value
        value = 0
        popup.destroy()
    popup = tk.Toplevel(GUI)

    popup.title("Verificación")
    popup.geometry("320x180")
    popup.configure(bg='#2B2B2B') 
    popup.attributes('-topmost', True)

    label = tk.Label(popup, text=string, bg='#2B2B2B', fg='white', font=(tk.font, 12))
    label.pack(padx=10, pady=10)

    ok_button = tk.Button(popup, text="Sí", command=on_ok, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10, font=(tk.font, 12))
    ok_button.pack(side=tk.LEFT, padx=10, pady=5)

    cancel_button = tk.Button(popup, text="No", command=on_cancel, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10, font=(tk.font, 12))
    cancel_button.pack(side=tk.RIGHT, padx=10, pady=5)

    popup.wait_window()

    return value



# CLASE: VENTANA EMERGENTE DE MENSAJE DE ERROR
def popup_error(msg, GUI):
    pop = tk.Toplevel(GUI)
    pop.title("Error")
    pop.geometry("320x180")
    pop.configure(bg='#2B2B2B') 
    pop.attributes('-topmost', True)

    label = tk.Label(pop, text=msg, bg='#2B2B2B', fg='white', font=(tk.font, 12))
    label.pack(side="top", fill="x", pady=10)
    btn = tk.Button(pop, text="Okay", command=pop.destroy, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10, font=(tk.font, 12))
    btn.pack()
    pop.wait_window()


