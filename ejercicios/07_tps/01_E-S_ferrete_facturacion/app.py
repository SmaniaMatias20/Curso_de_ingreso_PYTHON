import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Smania

Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
       
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        #Harcodeamos los tres importes
        #self.txt_importe_1.insert(0,"25")
        #self.txt_importe_2.insert(0,"25")
        #self.txt_importe_3.insert(0,"50")

        #Obtenemos el contenido de las cajas de texto y lo almacenamos en las variables
        precio_primer_producto = self.txt_importe_1.get()
        precio_segundo_producto = self.txt_importe_2.get()
        precio_tercer_producto = self.txt_importe_3.get()

        #Casteamos el contenido de las variables
        precio_primer_producto = float(precio_primer_producto) 
        precio_segundo_producto = float(precio_segundo_producto)
        precio_tercer_producto = float(precio_tercer_producto)

        #Realizamos la operacion
        total = precio_primer_producto + precio_segundo_producto + precio_tercer_producto

        #Formateamos y mostramos el mensaje 
        mensaje = f"La suma de los tres productos es: ${total}".format()
        alert(title="Suma", message=mensaje)

        #Vaciamos las cajas de texto
        self.txt_importe_1.delete(0,100)
        self.txt_importe_2.delete(0,100)
        self.txt_importe_3.delete(0,100)
        


    def btn_promedio_on_click(self):
        #Harcodeamos los tres importes
        #self.txt_importe_1.insert(0,"25")
        #self.txt_importe_2.insert(0,"25")
        #self.txt_importe_3.insert(0,"50")

        #Obtenemos el contenido de las cajas de texto y lo almacenamos en las variables
        precio_primer_producto = self.txt_importe_1.get()
        precio_segundo_producto = self.txt_importe_2.get()
        precio_tercer_producto = self.txt_importe_3.get()

        #Casteamos el contenido de las variables
        precio_primer_producto = float(precio_primer_producto) 
        precio_segundo_producto = float(precio_segundo_producto)
        precio_tercer_producto = float(precio_tercer_producto)

        #Realizamos la operacion
        promedio = (precio_primer_producto + precio_segundo_producto + precio_tercer_producto)/3

        #Formateamos y mostramos el contenido del mensaje
        mensaje = f"El promedio de los tres productos es: ${promedio}".format() 
        alert(title="Promedio", message=mensaje) 

        #Vaciamos las cajas de texto
        self.txt_importe_1.delete(0,100)
        self.txt_importe_2.delete(0,100)
        self.txt_importe_3.delete(0,100)

    def btn_total_iva_on_click(self):
        #Harcodeamos los tres importes
        #self.txt_importe_1.insert(0,"25")
        #self.txt_importe_2.insert(0,"25")
        #self.txt_importe_3.insert(0,"50")

        #Obtenemos el contenido de las cajas de texto y lo almacenamos en las variables
        precio_primer_producto = self.txt_importe_1.get()
        precio_segundo_producto = self.txt_importe_2.get()
        precio_tercer_producto = self.txt_importe_3.get()

        #Casteamos el contenido de las variables
        precio_primer_producto = float(precio_primer_producto) 
        precio_segundo_producto = float(precio_segundo_producto)
        precio_tercer_producto = float(precio_tercer_producto)

        #Realizamos la operacion
        precio_final = (precio_primer_producto + precio_segundo_producto + precio_tercer_producto) * 1.21   

        #Formateamos y mostramos el contenido del mensaje
        mensaje = f"El precio final de los productos es: ${precio_final}".format() 
        alert(title="Precio con IVA", message=mensaje) 

        #Vaciamos las cajas de texto
        self.txt_importe_1.delete(0,100)
        self.txt_importe_2.delete(0,100)
        self.txt_importe_3.delete(0,100)
        
         
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()