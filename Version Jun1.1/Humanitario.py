import encryption
import Transformations
import customtkinter
import CTkClasses
import Global

bold_font = ("Helvetica", 14, "bold")

class RegistroHumanitario:
    def __init__(self, tab4, workbook, app):
        self.tab4 = tab4
        self.workbook = workbook
        self.app = app
        self.create_widgets()

    def create_widgets(self):
            self.scrollable_frame = customtkinter.CTkScrollableFrame(self.tab4, width=600, height=600)
            self.scrollable_frame.grid(row=0, column=3, sticky="nsew", padx=0, pady=0)
            self.scrollable_frame.grid_rowconfigure(0, weight=1)
            self.scrollable_frame.grid_columnconfigure(0, weight=1)

            n_rows = 0

            self.namesHLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Nombre(s):  ", fg_color = "transparent") # Nombre(s)
            self.namesHLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
            self.namesHEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.namesHEntry.grid(row = n_rows, column = 1, padx = 1, pady = 5, ipady = 0, sticky = "e")
            n_rows += 1

            self.surPHLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Apellido Paterno: ", fg_color = "transparent") # Apellido Paterno
            self.surPHLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
            self.surPHEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.surPHEntry.grid(row = n_rows, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")
            n_rows += 1

            self.surMHLabel = customtkinter.CTkLabel(self.scrollable_frame, text = "Apellido Materno: ", fg_color = "transparent") # Apellida Materno
            self.surMHLabel.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
            self.surMHEntry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.surMHEntry.grid(row = n_rows, column = 1, padx= 1, pady = 5, ipady = 0, sticky = "e")
            n_rows += 1

            self.H1Label = customtkinter.CTkLabel(self.scrollable_frame, text = "Adulto, NNA, NNAnA:  ", fg_color = "transparent") # Nombre(s)
            self.H1Label.grid(row = n_rows, column = 0, padx = 1, pady = 5, ipady = 0, sticky = "e")
            self.H1Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Adulto",
                                                                            "Niña acompañada.",
                                                                            "Niño acompañado.",
                                                                            "Adolescente acompañado.",
                                                                            "Niña no acompañada.",
                                                                            "Niño no acompañado.",
                                                                            "Adolescente no acompañado."])
            self.H1Entry.grid(row= n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H6Label = customtkinter.CTkLabel(self.scrollable_frame, text="Estado Civil.  ", fg_color="transparent")
            self.H6Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H6Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Casada / Casado.",
                                                                "Divorciada / Divorciado.",
                                                                "Soltera / Soltero.",
                                                                "Separada / Separado.",
                                                                "Viuda / Viudo.",
                                                                "Unión Libre."])
            self.H6Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H7Label = customtkinter.CTkLabel(self.scrollable_frame, text="Tipo de población.  ", fg_color="transparent")
            self.H7Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H7Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Tránsito.",
                                                                "MPP.",
                                                                "Retornados.",
                                                                "Refugiados.",
                                                                "Desplazados internos.",
                                                                "Otra movilidad."])
            self.H7Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H8Label = customtkinter.CTkLabel(self.scrollable_frame, text="Documento de identidad.  ", fg_color="transparent")
            self.H8Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            n_rows += 1

            self.docVar1 = customtkinter.StringVar(value = "No")
            self.docCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Tarjeta de identidad de país de origen", variable=self.docVar1, onvalue="Sí", offvalue="No")
            self.docCB1.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.docVar2 = customtkinter.StringVar(value = "No")
            self.docCB2 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Certificado de nacionalidad / Acta de Nacimiento", variable=self.docVar2, onvalue="Sí", offvalue="No")
            self.docCB2.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1
            self.docVar3 = customtkinter.StringVar(value = "No")
            self.docCB3 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Pasaporte", variable=self.docVar3, onvalue="Sí", offvalue="No")
            self.docCB3.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1
            self.docVar4 = customtkinter.StringVar(value = "No")
            self.docCB4 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Curp", variable=self.docVar4, onvalue="Sí", offvalue="No")
            self.docCB4.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1
            self.docVar5 = customtkinter.StringVar(value = "No")
            self.docCB5 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Documento Migratorio", variable=self.docVar5, onvalue="Sí", offvalue="No")
            self.docCB5.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1
            self.docVar6 = customtkinter.StringVar(value = "No")
            self.docCB6 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Ningún documento", variable=self.docVar6, onvalue="Sí", offvalue="No")
            self.docCB6.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.H9Label = customtkinter.CTkLabel(self.scrollable_frame, text="Hijos.  ", fg_color="transparent")
            self.H9Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H9Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H9Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H10Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Usted sabe leer y escribir?  ", fg_color="transparent")
            self.H10Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H10Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H10Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H11Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Cuál fue su último grado de estudio?  ", fg_color="transparent")
            self.H11Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H11Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Preescolar.",
                                                                "Primaria.",
                                                                "Secundaria",
                                                                "Preparatoria",
                                                                "Bachillerato técnico",
                                                                "Licenciatura",
                                                                "Sin escolarizar"])
            self.H11Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H12Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Cuál fue su último grado académico?  ", fg_color="transparent")
            self.H12Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H12Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.H12Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H13Label = customtkinter.CTkLabel(self.scrollable_frame, text="Idiomas que domina.  ", fg_color="transparent")
            self.H13Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            n_rows += 1
            self.idiomaVar1 = customtkinter.StringVar(value = "No")
            self.idiomaCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Inglés", variable=self.idiomaVar1, onvalue="Sí", offvalue="No")
            self.idiomaCB1.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1
            self.idiomaVar2 = customtkinter.StringVar(value = "No")
            self.idiomaCB2 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Español", variable=self.idiomaVar2, onvalue="Sí", offvalue="No")
            self.idiomaCB2.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1
            self.idiomaVar3 = customtkinter.StringVar(value = "No")
            self.idiomaCB3 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Francés", variable=self.idiomaVar3, onvalue="Sí", offvalue="No")
            self.idiomaCB3.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1
            self.idiomaVar4 = customtkinter.StringVar(value = "No")
            self.idiomaCB4 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Criollo haitiano", variable=self.idiomaVar4, onvalue="Sí", offvalue="No")
            self.idiomaCB4.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1
            self.idiomaVar5 = customtkinter.StringVar(value = "No")
            self.idiomaCB5 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Garífona", variable=self.idiomaVar5, onvalue="Sí", offvalue="No")
            self.idiomaCB5.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1
            self.idiomaVar6 = customtkinter.StringVar(value = "No")
            self.idiomaCB6 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Portugués", variable=self.idiomaVar6, onvalue="Sí", offvalue="No")
            self.idiomaCB6.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1
            self.idiomaVar7 = customtkinter.StringVar(value = "No")
            self.idiomaCB7 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Otro idioma", variable=self.idiomaVar7, onvalue="Sí", offvalue="No")
            self.idiomaCB7.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.H14Label = customtkinter.CTkLabel(self.scrollable_frame, text="Fecha en que salió de su país de origen \n (DD/MM/AAAA):  ", fg_color="transparent")
            self.H14Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H14Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.H14Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H15Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Cómo se encuentra viajando?  ", fg_color="transparent")
            self.H15Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H15Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Sola/o", "Acompañada/o"])
            self.H15Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H16Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Cómo viajó?  ", fg_color="transparent")
            self.H16Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H16Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.H16Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H17Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Por qué razón tomó la decisión de salir de su país?  ", fg_color="transparent")
            self.H17Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H17Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.H17Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H18Label = customtkinter.CTkLabel(self.scrollable_frame, text="Durante su viaje desde que salió de su \n país hasta antes de llegar a México, ¿Usted \n sufrió de algún abuso a sus Derechos Humanos?  ", fg_color="transparent")
            self.H18Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H18Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H18Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H19Label = customtkinter.CTkLabel(self.scrollable_frame, text="Cuando usted entró a territorio mexicano, \n ¿Usted vivió algún abuso o agresión?  ", fg_color="transparent")
            self.H19Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H19Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H19Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H20Label = customtkinter.CTkLabel(self.scrollable_frame, text="En algún momento de su camino, \n ¿Usted le pagó a algún guía para viajar?  ", fg_color="transparent")
            self.H20Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H20Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H20Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H21Label = customtkinter.CTkLabel(self.scrollable_frame, text="Fecha en que ingresó a México (DD/MM/AAAA):  ", fg_color="transparent")
            self.H21Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H21Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.H21Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H22Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Por dónde ingresó a México?  ", fg_color="transparent")
            self.H22Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H22Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Tapachula.",
                                                                "Tenosoique."
                                                                "Chetumal.",
                                                                "Palenque.",
                                                                "Matamoros.",
                                                                "Reynosa.",
                                                                "Veracruz.",
                                                                "Tabasco.",
                                                                "Chiapas"])
            self.H22Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H23Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Cuál es su destino final?  ", fg_color="transparent")
            self.H23Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H23Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["México.",
                                                                "Estados Unidos.",
                                                                "Regresar a mi país de origen."])
            self.H23Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H24Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Cuenta con una red de apoyo en Monterrey?  ", fg_color="transparent")
            self.H24Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H24Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H24Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H25Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Usted ha intentado ingresar a Estados Unidos?  ", fg_color="transparent")
            self.H25Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H25Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H25Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H26Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Usted cuenta con una \n red de apoyo en Estados Unidos?  ", fg_color="transparent")
            self.H26Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H26Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H26Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H27Label = customtkinter.CTkLabel(self.scrollable_frame, text="Descripción de la red de apoyo \n con la que cuenta en Estados Unidos.  ", fg_color="transparent")
            self.H27Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H27Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.H27Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H28Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Usted ha estado en alguna estación migratoria?  ", fg_color="transparent")
            self.H28Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H28Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H28Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H29Label = customtkinter.CTkLabel(self.scrollable_frame, text="Ante las vivencias de abuso de autoridad, \n agresiones y vulnerabilidad a Derechos Humanos, \n ¿Usted interpuso una denuncia formal?  ", fg_color="transparent")
            self.H29Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H29Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H29Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H30Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Usted puede regresar a su país?  ", fg_color="transparent")
            self.H30Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H30Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H30Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H31Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Actualmente usted padece alguna enfermedad?  ", fg_color="transparent")
            self.H31Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H31Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H31Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H32Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Se encuentra o encontraba \n en algún tratamiento médico?  ", fg_color="transparent")
            self.H32Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H32Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.H32Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H33Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Usted padece algún tipo de alergia?  ", fg_color="transparent")
            self.H33Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H33Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H33Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H34Label = customtkinter.CTkLabel(self.scrollable_frame, text="En su trayecto por México, \n ¿Usted se ha estado en algún otro albergue?  ", fg_color="transparent")
            self.H34Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H34Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H34Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H35Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Se le brindó acceso al albergue de Casa Monarca?  ", fg_color="transparent")
            self.H35Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H35Entry = customtkinter.CTkOptionMenu(self.scrollable_frame, values=["Si.", "No."])
            self.H35Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1


            NoticeLabel = customtkinter.CTkLabel(self.scrollable_frame, text="PARA USO INTERNO, SE CUBRE DE AC", font=bold_font, fg_color="transparent")
            NoticeLabel.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            NoticeLabel2 = customtkinter.CTkLabel(self.scrollable_frame, text="UERDO AL RESULTADO DE LA ENTREVISTA", font=bold_font, fg_color="transparent")
            NoticeLabel2.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1
            NoticeLabel3 = customtkinter.CTkLabel(self.scrollable_frame, text="NO SON PREGUNTAS QUE SE LE ", font=bold_font, fg_color="transparent")
            NoticeLabel3.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            NoticeLabel4 = customtkinter.CTkLabel(self.scrollable_frame, text="REALICEN A LA PERSONA DE INTERÉS", font=bold_font, fg_color="transparent")
            NoticeLabel4.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H36Label = customtkinter.CTkLabel(self.scrollable_frame, text="¿Cuáles servicios se le brindaron a la persona?  ", fg_color="transparent")
            self.H36Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            n_rows += 1

            self.serviciosVar1 = customtkinter.StringVar(value = "No")
            self.serviciosCB1 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Agua y alimento", variable=self.serviciosVar1, onvalue="Sí", offvalue="No")
            self.serviciosCB1.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar2 = customtkinter.StringVar(value = "No")
            self.serviciosCB2 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Alimento", variable=self.serviciosVar2, onvalue="Sí", offvalue="No")
            self.serviciosCB2.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar3 = customtkinter.StringVar(value = "No")
            self.serviciosCB3 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Kit de higiene", variable=self.serviciosVar3, onvalue="Sí", offvalue="No")
            self.serviciosCB3.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar4 = customtkinter.StringVar(value = "No")
            self.serviciosCB4 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Ropa y calzado", variable=self.serviciosVar4, onvalue="Sí", offvalue="No")
            self.serviciosCB4.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar5 = customtkinter.StringVar(value = "No")
            self.serviciosCB5 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Acceso a higiene (Regadera)", variable=self.serviciosVar5, onvalue="Sí", offvalue="No")
            self.serviciosCB5.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar6 = customtkinter.StringVar(value = "No")
            self.serviciosCB6 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Asesoría legal", variable=self.serviciosVar6, onvalue="Sí", offvalue="No")
            self.serviciosCB6.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar7 = customtkinter.StringVar(value = "No")
            self.serviciosCB7 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Orientación legal", variable=self.serviciosVar7, onvalue="Sí", offvalue="No")
            self.serviciosCB7.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar8 = customtkinter.StringVar(value = "No")
            self.serviciosCB8 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Orientación en búsqueda de empleo", variable=self.serviciosVar8, onvalue="Sí", offvalue="No")
            self.serviciosCB8.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar9 = customtkinter.StringVar(value = "No")
            self.serviciosCB9 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Orientación en el acceso a la educación", variable=self.serviciosVar9, onvalue="Sí", offvalue="No")
            self.serviciosCB9.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar10 = customtkinter.StringVar(value = "No")
            self.serviciosCB10 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Orientación en la búsqueda de vivienda", variable=self.serviciosVar10, onvalue="Sí", offvalue="No")
            self.serviciosCB10.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar11 = customtkinter.StringVar(value = "No")
            self.serviciosCB11 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Orientación para acceder a servicios de salud", variable=self.serviciosVar11, onvalue="Sí", offvalue="No")
            self.serviciosCB11.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar12 = customtkinter.StringVar(value = "No")
            self.serviciosCB12 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Orientación a servicios psisológicos", variable=self.serviciosVar12, onvalue="Sí", offvalue="No")
            self.serviciosCB12.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar13 = customtkinter.StringVar(value = "No")
            self.serviciosCB13 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Canalización a servicios psicológicos", variable=self.serviciosVar13, onvalue="Sí", offvalue="No")
            self.serviciosCB13.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            self.serviciosVar14 = customtkinter.StringVar(value = "No")
            self.serviciosCB14 = customtkinter.CTkCheckBox(self.scrollable_frame, text="Atención psicosocial", variable=self.serviciosVar14, onvalue="Sí", offvalue="No")
            self.serviciosCB14.grid(row=n_rows, column=1, padx=1, pady=5, sticky="w")
            n_rows += 1

            '''
            SUBIDA DE ARCHIVOS
            '''

            self.H40Label = customtkinter.CTkLabel(self.scrollable_frame, text="Señas particulares.  ", fg_color="transparent")
            self.H40Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H40Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.H40Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H41Label = customtkinter.CTkLabel(self.scrollable_frame, text="Contacto de emergencia.  ", fg_color="transparent")
            self.H41Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H41Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.H41Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H42Label = customtkinter.CTkLabel(self.scrollable_frame, text="Geográficamente, ¿Dónde se \n encuentra su contacto de emergencia?  ", fg_color="transparent")
            self.H42Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H42Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.H42Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            self.H43Label = customtkinter.CTkLabel(self.scrollable_frame, text="Observaciones finales.  ", fg_color="transparent")
            self.H43Label.grid(row=n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            self.H43Entry = customtkinter.CTkTextbox(self.scrollable_frame, width = 300, height = 10)
            self.H43Entry.grid(row=n_rows, column = 1, padx=1,pady=5,ipady=0,sticky="w")
            n_rows += 1

            #NOMBRE ?
            self.submitPBtn = customtkinter.CTkButton(self.scrollable_frame, text="Registrar", width=50, command = lambda: new_entry(self.workbook, self.getHText(), self.app))
            #self.submitPBtn = customtkinter.CTkButton(self.scrollable_frame, text="Registrar", width=50, command = lambda: print(self.getHText()))
            self.submitPBtn.grid(row = n_rows, column = 0, padx=1,pady=5,ipady=0,sticky="e")
            n_rows += 1

    def getHText(self):
        entriesHText1 = [self.surPHEntry, self.surMHEntry, self.namesHEntry]
        entriesHChoice1 = [self.H1Entry, self.H6Entry, self.H7Entry, self.docVar1, self.docVar2, self.docVar3, self.docVar4, self.docVar5, self.docVar6, 
                           self.H9Entry, self.H10Entry, self.H11Entry] 
        entriesHText2 = [self.H12Entry]
        entriesHChoice2 = [self.idiomaVar1, self.idiomaVar2, self.idiomaVar3, self.idiomaVar4, self.idiomaVar5, self.idiomaVar6, self.idiomaVar7]
        entriesHText3 = [self.H14Entry]
        entriesHChoice3 = [self.H15Entry]
        entriesHText4 = [self.H16Entry, self.H17Entry]
        entriesHChoice4 = [self.H18Entry, self.H19Entry, self.H20Entry]
        entriesHText5 = [self.H21Entry]
        entriesHChoice5 = [self.H22Entry, self.H23Entry, self.H24Entry, self.H25Entry, self.H26Entry]
        entriesHText6 = [self.H27Entry]
        entriesHChoice6 = [self.H28Entry, self.H29Entry, self.H30Entry, self.H31Entry]
        entriesHText7 = [self.H32Entry]
        entriesHChoice7 = [self.H33Entry, self.H34Entry, self.H35Entry, self.serviciosVar1, self.serviciosVar2, self.serviciosVar3, self.serviciosVar4, 
                           self.serviciosVar5, self.serviciosVar6, self.serviciosVar7, self.serviciosVar8, self.serviciosVar9, self.serviciosVar10, 
                           self.serviciosVar11, self.serviciosVar12, self.serviciosVar13, self.serviciosVar14]
        entriesHText8 = [self.H40Entry, self.H41Entry, self.H42Entry, self.H43Entry]
        entry = [entryT.get(0.0, "end-1c") for entryT in entriesHText1] + [entryO.get() for entryO in entriesHChoice1] + [entryT.get(0.0, "end-1c") for entryT in entriesHText2] + [entryO.get() for entryO in entriesHChoice2] + [entryT.get(0.0, "end-1c") for entryT in entriesHText3] + [entryO.get() for entryO in entriesHChoice3] + [entryT.get(0.0, "end-1c") for entryT in entriesHText4] + [entryO.get() for entryO in entriesHChoice4] + [entryT.get(0.0, "end-1c") for entryT in entriesHText5] + [entryO.get() for entryO in entriesHChoice5] + [entryT.get(0.0, "end-1c") for entryT in entriesHText6] + [entryO.get() for entryO in entriesHChoice6] + [entryT.get(0.0, "end-1c") for entryT in entriesHText7] + [entryO.get() for entryO in entriesHChoice7] + [entryT.get(0.0, "end-1c") for entryT in entriesHText8]
        return entry

def new_entry(workbook, entry, GUI):
    global ver
    id = Transformations.generate_id([Transformations.clean_string(s) for s in entry[:3]])
    entry = [e if e else "N/a" for e in entry]
    entry = entry[3:]
    hum_sheet = workbook.worksheet("Humanitario")
    cols = len(hum_sheet.row_values(1)) # MANUAL
    hum_ids = hum_sheet.col_values(1)
    if id not in hum_ids: # Registro no existente
        id2 = Global.similar_entries(id, hum_ids[1:], GUI)
        if id2 == id:
            CTkClasses.popup_error("Registre al individuo en la\n sección General antes de llevar\n a cabo el registro psicosocial.", GUI)
            return
        else: id = id2
    index = hum_ids.index(id) + 1
    existing_row = hum_sheet.row_values(index)[1:]
    if len(existing_row) == 0:  # Agregar registro Humanitario
        encrypted_entries = [encryption.encrypt_element(e, "H") for e in entry]
        hum_sheet.update('B{}:{}'.format(index, 'BI' + str(index)), [encrypted_entries])  # Actualizar registro
    else:
        ver = CTkClasses.verification_popup("El sujeto ya cuenta con\n un registro humanitario.\n ¿Desea actualizarlo?", GUI)
        #GUI.wait_window(pop)
        if ver == 1:  # Actualizar registro Legal
            values_to_update = []
            for i in range(cols - 1):
                if entry[i] != "N/a":
                    encrypted_entry = encryption.encrypt_element(entry[i], "H")
                    values_to_update.append(encrypted_entry)
                else: values_to_update.append(existing_row[i])
            hum_sheet.update('B{}:{}'.format(index, 'BI' + str(index)), [values_to_update])
        else:  # No sobrescribir
            return
