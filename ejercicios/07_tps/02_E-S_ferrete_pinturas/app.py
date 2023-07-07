import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

2.	Para el departamento de Pinturas:
	A.	Al ingresar una temperatura en Fahrenheit debemos mostrar la temperatura en Centígrados con un mensaje concatenado 
        (0 °F − 32) × 5/9 = -17,78 °C

    B.	Al ingresar una temperatura en Centígrados debemos mostrar la temperatura en Fahrenheit 
        (0 °C × 9/5) + 32 = 32 °F

    
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Temperatura °C")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_temperatura_c = customtkinter.CTkEntry(master=self)
        self.txt_temperatura_c.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Temperatura °F")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_temperatura_f = customtkinter.CTkEntry(master=self)
        self.txt_temperatura_f.grid(row=1, column=1)
       
        self.btn_convertir_c_f = customtkinter.CTkButton(master=self, text="Convertir °C a °F", command=self.btn_convertir_c_f_on_click)
        self.btn_convertir_c_f.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_convertir_f_c = customtkinter.CTkButton(master=self, text="Convertir °F a °C", command=self.btn_convertir_f_c_on_click)
        self.btn_convertir_f_c.grid(row=4, pady=10, columnspan=2, sticky="nsew")
    
    def btn_convertir_c_f_on_click(self):
        #Harcodeamos los datos
        #self.txt_temperatura_c.insert(0,"40")
        
        #Obtenemos el contenido de la caja de texto y lo almacenamos en la variable
        grados_centigrados = self.txt_temperatura_c.get()
        
        #Casteamos el contenido de la variable
        grados_centigrados = float(grados_centigrados)

        #Realizamos la operacion
        grados_fahrenheit = (grados_centigrados*1.8) + 32

        #Formateamos el mensaje y lo asignamos a la variable
        mensaje = f"{grados_centigrados}°C equivalen a: {grados_fahrenheit}°F".format()

        #Mostramos el mensaje
        alert(title="Conversion",message=mensaje)

        #Vaciamos las cajas de texto
        self.txt_temperatura_c.delete(0,100)
        self.txt_temperatura_f.delete(0,100)
        




    def btn_convertir_f_c_on_click(self):
        #Harcodeamos el dato
        #self.txt_temperatura_f.insert(0,"50")

        #Obtenemos el contenido de la caja de texto y lo almacenamos en la variable
        grados_fahrenheit = self.txt_temperatura_f.get()

        #Casteamos el contenido de la variable
        grados_fahrenheit = float(grados_fahrenheit)

        #Realizamos la operacion
        grados_centigrados = (grados_fahrenheit - 32) / 1.8

        #Formateamos el mensaje y lo asignamos a la variable
        mensaje = f"{grados_fahrenheit}°F equivalen a: {grados_centigrados}°C".format()

        #Mostramos el mensaje
        alert(title="Conversion",message=mensaje)

        #Vaciamos las cajas de texto
        self.txt_temperatura_c.delete(0,100)
        self.txt_temperatura_f.delete(0,100)





    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()