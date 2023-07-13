import random
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Matias
Apellido: Smania

Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        #Primera forma
        """ 
        cantidad_lamparas = self.combobox_cantidad.get()
        marca_lampara = self.combobox_marca.get()
        cantidad_lamparas = int(cantidad_lamparas)
        precio_base_lampara = 800
        
        if cantidad_lamparas >= 6:
            precio_final = (precio_base_lampara * cantidad_lamparas) * 0.50       
        else: 
            if cantidad_lamparas == 5: 
                if marca_lampara == "ArgentinaLuz":
                    precio_final = (precio_base_lampara * cantidad_lamparas) * 0.60
                else: 
                    precio_final = (precio_base_lampara * cantidad_lamparas) * 0.70        
            else:
                if cantidad_lamparas == 4: 
                    if marca_lampara == "ArgentinaLuz" or marca_lampara == "FelipeLamparas":  
                        precio_final = (precio_base_lampara * cantidad_lamparas) * 0.75 
                    else: 
                        precio_final = (precio_base_lampara * cantidad_lamparas) * 0.80 
                else:          
                    if cantidad_lamparas == 3:
                        if marca_lampara == "ArgentinaLuz":    
                            precio_final = (precio_base_lampara * cantidad_lamparas) * 0.85
                        else:    
                            if marca_lampara == "FelipeLamparas":
                                precio_final = (precio_base_lampara * cantidad_lamparas) * 0.90    
                            else:        
                                precio_final = (precio_base_lampara * cantidad_lamparas) * 0.95 
                    else: 
                        precio_final = precio_base_lampara * cantidad_lamparas            

        if precio_final > 4000:
            precio_final = precio_final * 0.95
            mensaje = f"La cantidad de lamparas compradas es de {cantidad_lamparas}, la marca es {marca_lampara} y el precio final es de {precio_final}"
        else:
            mensaje = f"La cantidad de lamparas compradas es de {cantidad_lamparas}, la marca es {marca_lampara} y el precio final es de {precio_final}"    
                
        alert(title = "Ejercicio 4", message = mensaje) 
        
        """

        #Segunda forma

        cantidad_lamparas = self.combobox_cantidad.get()
        marca_lampara = self.combobox_marca.get()
        cantidad_lamparas = int(cantidad_lamparas)
        precio_base_lampara = 800

        if cantidad_lamparas >= 6:
            precio_final = (precio_base_lampara * cantidad_lamparas) * 0.50
        elif cantidad_lamparas == 5:
            if marca_lampara == "ArgentinaLuz":
                precio_final = (precio_base_lampara * cantidad_lamparas) * 0.60
            else: 
                precio_final = (precio_base_lampara * cantidad_lamparas) * 0.70
        elif cantidad_lamparas == 4:
            if marca_lampara == "ArgentinaLuz" or marca_lampara == "FelipeLamparas":  
                precio_final = (precio_base_lampara * cantidad_lamparas) * 0.75 
            else: 
                precio_final = (precio_base_lampara * cantidad_lamparas) * 0.80 
        elif cantidad_lamparas == 3:
            if marca_lampara == "ArgentinaLuz":    
                precio_final = (precio_base_lampara * cantidad_lamparas) * 0.85
            else:    
                if marca_lampara == "FelipeLamparas":
                    precio_final = (precio_base_lampara * cantidad_lamparas) * 0.90    
                else:        
                    precio_final = (precio_base_lampara * cantidad_lamparas) * 0.95
        else: 
            precio_final = precio_base_lampara * cantidad_lamparas 

        if precio_final > 4000:
            precio_final = precio_final * 0.95
            mensaje = f"La cantidad de lamparas compradas es de {cantidad_lamparas}, la marca es {marca_lampara} y el precio final es de {precio_final}"
        else:
            mensaje = f"La cantidad de lamparas compradas es de {cantidad_lamparas}, la marca es {marca_lampara} y el precio final es de {precio_final}"    
                
        alert(title = "Ejercicio 4", message = mensaje)               


          
            






        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()