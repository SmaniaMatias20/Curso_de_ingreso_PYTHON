import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	El departamento de Construcción Rural requiere una herramienta que facilite el calculo de materiales necesarios 
a la hora de realizar un alambrado permetral, se le solicita al usuario que ingrese el ancho y el largo del terreno.

    A. Informar los metros cuadrados del terreno y los metros lineales del perimetro
    B. Informar la cantidad de postes de quebracho Grueso de 2.4 mts (van cada 250 mts lineales y en las esquinas).
    C. Informar la cantidad de postes de quebracho Fino de 2.2 mts (van cada 12 mts lineales, si en es lugar no se encuentra el poste grueso).
    D. Informar la cantidad de varillas (van cada 2 mts lineales).
    E. Informar la cantidad de alambre alta resistencia 17/15 considerando 7 hilos.

    EJ 36 MTS X 24 MTS 
    (G)Poste Quebracho Grueso de 2.4 mts
    (V)Poste Quebracho Fino de 2.2 mts
    (F)Varillas
    
    G V V V V V F V V V V V F V V V V V G
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    F                                   F
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    V                                   V
    G V V V V V F V V V V V F V V V V V G
    
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Largo")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_largo = customtkinter.CTkEntry(master=self)
        self.txt_largo.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Ancho")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)

        self.txt_ancho = customtkinter.CTkEntry(master=self)
        self.txt_ancho.grid(row=1, column=1)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="CALCULAR", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):

        #PuntoA
        largo = self.txt_largo.get()
        ancho = self.txt_ancho.get()
        largo = float(largo)
        ancho = float(ancho)

        metros_cuadrados = largo * ancho
        metros_lineales = (largo + ancho) * 2
        primer_mensaje = f"Los metros cuadrados del terreno son {metros_cuadrados}m2 ... y los metros lineales del perimetro son {metros_lineales}".format()

        alert(title="Punto A", message=primer_mensaje)

        #PuntoB
        esquinas = 4
        distancia_postes_gruesos = 250
        postes_gruesos = esquinas + (metros_lineales - (distancia_postes_gruesos * esquinas)) / distancia_postes_gruesos
        postes_gruesos = round(postes_gruesos)
        
        segundo_mensaje = f"Se necesitaran {postes_gruesos} postes de quebracho grueso de 2.4mts."

        alert(title="Punto B", message=segundo_mensaje)

        #PuntoC
        distancia_postes_finos = 12
        postes_finos = (metros_lineales / distancia_postes_finos) + (metros_lineales - distancia_postes_gruesos * esquinas) // distancia_postes_gruesos - 4 - (metros_lineales / 1500)
        postes_finos = round(postes_finos)

        tercer_mensaje = f"Se necesitaran {postes_finos} postes de quebracho fino de 2.2mts."

        alert(title="Punto C", message=tercer_mensaje)

        #PuntoD
        distancia_varillas = 2
        varillas = metros_lineales / distancia_varillas

        cuarto_mensaje = f"Se necesitaran {varillas} varillas"

        alert(title="Punto D", message=cuarto_mensaje)

        #PuntoE
        hilos = 7
        metros_alambre = metros_lineales * hilos

        quinto_mensaje = f"Se necesitaran {metros_alambre} metros de alambre"

        alert(title="Punto E", message=quinto_mensaje)

        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
