import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Smania

Al presionar el botón 'MÁXIMO' se analizará el vector lista_datos a efectos de determinar cuál es el número 
más grande allí contenido el cual deberá ser informado utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="MÁXIMO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        bandera = True

        for numero in self.lista_datos:
            if bandera:
                numero_maximo = numero
                bandera = False

            if numero >= numero_maximo:
                numero_maximo = numero

        alert("Numero maximo", f"El numero maximo de la lista es: {numero_maximo}")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()