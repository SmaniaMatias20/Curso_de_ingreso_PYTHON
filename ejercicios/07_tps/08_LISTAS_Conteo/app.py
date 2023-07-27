import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Smania

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                             columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

        self.lista = []

    def btn_comenzar_ingreso_on_click(self):
        
        numero_ingresado = ""

        while numero_ingresado != None:
            numero_ingresado = prompt("Numero", "Ingrese un numero")
            
            if numero_ingresado == None:
                break

            if numero_ingresado == "" or numero_ingresado.isalpha():
                continue
            
            numero_ingresado = int(numero_ingresado)

            self.lista.append(numero_ingresado)

    def btn_mostrar_estadisticas_on_click(self):

        acumulador_positivos = 0
        acumulador_negativos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_cero = 0
        minimo_negativo = 0
        maximo_positivo = 0
        promedio_negativos = 0

        for numero in self.lista:

            if numero > 0:

                if contador_positivos == 0:
                    maximo_positivo = numero

                if numero > maximo_positivo:
                    maximo_positivo = numero

                acumulador_positivos += numero
                contador_positivos += 1
            elif numero < 0:

                if contador_negativos == 0:
                    minimo_negativo = numero

                if numero < minimo_negativo:
                    minimo_negativo = numero

                acumulador_negativos += numero
                contador_negativos += 1
            else:
                contador_cero += 1  

        if contador_negativos != 0:
            promedio_negativos = acumulador_negativos // contador_negativos
        else:
            promedio_negativos = 0    

        alert("Trabajo Practico", f"""

          Punto A: La suma acumulada de los numeros negativos es: {acumulador_negativos}
        \nPunto B: La suma acumulada de los numeros positivos es: {acumulador_positivos}
        \nPunto C: La cantidad de numeros positivos es: {contador_positivos}
        \nPunto D: La cantidad de numeros negativos es: {contador_negativos}
        \nPunto E: La cantidad de 0(ceros) es: {contador_cero}
        \nPunto F: El minimo de los negativos es: {minimo_negativo}
        \nPunto G: El maximo de los positivos es: {maximo_positivo}
        \nPunto H: El promedio de los numeros negativos es: {promedio_negativos}

        """)

        self.lista.clear()


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
