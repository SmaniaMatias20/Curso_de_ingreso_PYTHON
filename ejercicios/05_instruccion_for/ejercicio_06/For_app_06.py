import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Smania

Al presionar el botón Mostrar pedir un número. mostrar los números pares desde 
el 1 al número ingresado, y mostrar la cantidad de números pares encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # numero = prompt("Numero", "Ingrese un numero")
        # numero = int(numero)
        # contador_pares = 0
        # lista_numeros = range(2,numero+1,2)
        # for numero in lista_numeros:
        #     alert("Numeros pares", numero)
        #     contador_pares += 1
        
        # alert("Cantidad de pares", f"La cantidad de numeros pares encontrados es: {contador_pares}")

        numero_ingresado = prompt("Numero", "Ingrese un numero")

        while numero_ingresado == None or not numero_ingresado.isdigit():
            numero_ingresado = prompt("Numero", "Ingrese un numero")

        numero_ingresado = int(numero_ingresado)
        contador_pares = 0
        lista_numeros = range(1,numero_ingresado+1)
        for numero in lista_numeros:
            if numero % 2 == 0:
                alert("Numero par", numero)
                contador_pares += 1

        alert("Cantidad de pares", f"La cantidad de numeros pares encontrados es: {contador_pares}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()