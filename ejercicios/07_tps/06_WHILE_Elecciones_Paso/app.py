'''
Nombre: Matias
Apellido: Smania

De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        respuesta = True
        acumulador_edades = 0
        maximo_votos = 0 
        minimo_votos = 0
        acumulador_votos = 0
        contador_candidatos = 0

        while respuesta:
            nombre_ingresado = prompt("Nombre", "Ingrese su nombre")
            while nombre_ingresado == None or not nombre_ingresado.isalpha():
                nombre_ingresado = prompt("Nombre", "Error! Ingrese su nombre correctamente")

            edad_ingresada = prompt("Edad", "Ingrese su edad")
            while edad_ingresada == None or not edad_ingresada.isdigit():
                edad_ingresada = prompt("Edad", "Error! Ingrese su edad correctamente")

            edad_ingresada = int(edad_ingresada)

            if edad_ingresada > 25 and edad_ingresada < 90:
                acumulador_edades += edad_ingresada
            else:
                print("Error, la edad debe ser mayor a 25 y menor a 90")
                continue

            cantidad_votos = prompt("Votos", "Ingrese la cantidad de votos") 
            while cantidad_votos == None or not cantidad_votos.isdigit():
                cantidad_votos = prompt("Votos", "Error! Ingrese la cantidad de votos")    

            cantidad_votos = int(cantidad_votos)

            if cantidad_votos > 0:
                acumulador_votos += cantidad_votos

                if maximo_votos == 0 and minimo_votos == 0:
                    maximo_votos = cantidad_votos
                    minimo_votos = cantidad_votos   

                if cantidad_votos >= maximo_votos:
                    candidato_con_mas_votos = nombre_ingresado
                    maximo_votos = cantidad_votos 
                elif cantidad_votos <= minimo_votos:
                    candidato_con_menos_votos = nombre_ingresado
                    edad_candidato_con_menos_votos = edad_ingresada 
                    minimo_votos = cantidad_votos
            else: 
                print("Error! Los votos deben ser mayor a 0")
                continue


            contador_candidatos += 1
            respuesta= question("Ingreso", "¿Desea ingresar un nuevo candidato?")


        promedio_edad = acumulador_edades // contador_candidatos

        print(f"El candidato con mas votos es: {candidato_con_mas_votos}")
        print(f"El candidato con menos votos es: {candidato_con_menos_votos} y su edad es {edad_candidato_con_menos_votos}")
        print(f"El promedio de edades es: {promedio_edad}")
        print(f"El total de votos emitidos es: {acumulador_votos}")
        
        
        



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
