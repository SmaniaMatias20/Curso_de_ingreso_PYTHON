import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Smania

Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = prompt("Numero", "Ingrese un numero")

        while numero_ingresado == None or not numero_ingresado.isdigit():
            numero_ingresado = prompt("Numero", "Ingrese un numero")

        contador_divisores = 0
        numero_ingresado = int(numero_ingresado)
        lista_numeros = range(1,numero_ingresado+1)

        for numero in lista_numeros:
            if numero_ingresado % numero == 0:
                alert("Numeros divisores", numero)
                contador_divisores += 1

        alert("Cantidad divisores", f"La cantidad de numeros divisores es: {contador_divisores}")        




        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()