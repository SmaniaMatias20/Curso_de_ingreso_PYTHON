import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Smania

Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_negativo = 0
        acumulador_positivo = 0
        contador_negativo = 0
        contador_positivo = 0
        contador_cero = 0


        while True:
            numero_ingresado = prompt("Numero", "Ingrese un numero")

            if numero_ingresado == None:
                break

            numero_ingresado = int(numero_ingresado)

            if numero_ingresado != 0:
                if numero_ingresado > 0:
                    contador_positivo += 1
                    acumulador_positivo += numero_ingresado
                else:
                    contador_negativo += 1
                    acumulador_negativo += numero_ingresado
            else:
                contador_cero += 1

        diferencia = contador_positivo - contador_negativo

        alert("Ejercicio 10", f"""La suma acumulada de los numeros positivos es: {acumulador_positivo}
                                \nLa suma acumulada de los numeros negativos es: {acumulador_negativo}
                                \nLa cantidad de numeros positivos es: {contador_positivo}
                                \nLa cantidad de numeros negativos es: {contador_negativo}
                                \nLa cantidad de 0(ceros) ingresados es: {contador_cero}
                                \nLa diferencia entre la cantidad de positivos y la cantidad de negativos es: {diferencia}""")
               

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
