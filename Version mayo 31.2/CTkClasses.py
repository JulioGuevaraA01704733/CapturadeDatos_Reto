import customtkinter
import General
import tkinter as tk


import tkinter as tk

def verification_popup(string, GUI):
    global value
    value = None

    def on_ok():
        global value
        value = 1
        popup.destroy()

    def on_cancel():
        global value
        value = 0
        popup.destroy()
    popup = tk.Toplevel(GUI)  # Use the app (main window) as the parent

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


def popup_error(msg, GUI):
    pop = tk.Toplevel(GUI)
    pop.title("Error")
    pop.geometry("320x180")
    pop.configure(bg='#2B2B2B') 
    pop.attributes('-topmost', True)

    label = tk.Label(pop, text=msg, bg='#2B2B2B', fg='white', font=(tk.font, 12))
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(pop, text="Okay", command=pop.destroy, bg='#1F6AA5', fg='white', relief='solid', borderwidth=1, highlightthickness=10, font=(tk.font, 12))
    B1.pack()
    pop.wait_window()


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

def CenterWindowToDisplay(Screen: customtkinter, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"
