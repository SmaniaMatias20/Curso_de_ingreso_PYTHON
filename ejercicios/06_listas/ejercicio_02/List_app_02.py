import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Smania

Al presionar el botón 'CARGAR' se le solicitarán tres números al usuario mediante el Dialog Prompt, los mismos deberán ser almacenados en un vector lista_datos. 
Al presionar el botón 'MOSTRAR', se deberán mostrar los números almacenados en el vector utilizando Dialog Alert para informar cada elemento.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = []


    def btn_cargar_on_click(self):

        for _ in range(3):
            numero = prompt("Numero", "Ingrese un numero")
            while numero == None or not numero.isdigit():
               numero = prompt("Numero", "Ingrese un numero") 
            
            self.lista_datos.append(numero)
            

            

        
    def btn_mostrar_on_click(self):

        for elemento in self.lista_datos:
            alert("Mostrar", elemento)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()