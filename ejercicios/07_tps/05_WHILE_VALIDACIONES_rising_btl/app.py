import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        bandera = True

        while bandera:
            apellido = prompt("Apellido", "Ingrese su apellido")

            if apellido != "": #Validar que se ingrese por lo menos una cadena
                if not apellido.isdecimal(): 
                    self.txt_apellido.delete(0,100)
                    self.txt_apellido.insert(0, apellido)
                else: 
                    alert("Error", "No debe ingresar numeros")
                    continue
            else:
                alert("Error", "Debe ingresar un apellido")
                continue


            edad = prompt("Edad", "Ingrese su edad")
            if edad.isdecimal():
                edad = int(edad)
                if edad >= 18 and edad <= 90:
                    self.txt_edad.delete(0,100)
                    self.txt_edad.insert(0, edad)
                else:
                    alert("Error", "La edad debe ser entre 18 y 90 años")
                    continue 
            else:
                alert("Error", "Debe ingresar un numero")   
                continue    

            estado_civil = prompt("Estado Civil", "Ingrese su estado civil")
            match estado_civil.lower(): #Pasamos a minuscula estado_civil
                case "soltero" | "soltera":  
                    self.combobox_tipo.set("Soltero/a")
                case "casado" | "casada":
                    self.combobox_tipo.set("Casado/a")
                case "divorciado" | "divorciada":  
                    self.combobox_tipo.set("Divorciado/a")
                case "viudo" | "viuda":
                    self.combobox_tipo.set("Viudo/a")
                case _:
                    alert("Error", "Debe elegir un Estado Civil")
                    continue        
                   

            numero_legajo = prompt("Numero Legajo","Ingrese su numero de legajo")
            
            if numero_legajo.isdecimal():
                if numero_legajo[0] != "0" and numero_legajo.__len__() == 4:
                    numero_legajo = int(numero_legajo)
                    self.txt_legajo.delete(0,100)
                    self.txt_legajo.insert(0,numero_legajo)
                else:
                    alert("Error", "El numero ingresado debe tener cuatro cifras y no puede tener 0(ceros) a la izquierda")
                    continue
            else:
                alert("Error", "Debe ingresar un numero") 
                continue   

            bandera = False       




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
