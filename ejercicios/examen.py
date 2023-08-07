import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se deberan cargar tantos vehiculos como el usuario desee. 
    Los datos a cargar de cada vehiculo son: tipo de vehiculo (auto, camioneta, moto) y kilometros*.

* Todos los autos son usados.

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar todos los vehiculos ingresados con su correspondiente kilometraje y su posicion en la lista.
Ejemplo: 1 - Auto - 1000 km
         2 - Camioneta - 2000 km
         etc..

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al presionar el boton Informar 
    0- El mayor kilometraje y su tipo de vehiculo.
    1- El menor kilometraje y su tipo de vehiculo.
    2- Kilometraje promedio de los autos.
    3- Precio promedios de todos los servicios.
    4- Informar los kilometrajes que superan el promedio (total).
    5- Informar los kilometrajes que NO superan el promedio (total).
    6- Informar la cantidad de vehiculos de cada tipo.
    7- Informar el precio promedio de los servicios cuyo kilometraje es mayor a 10000 kms.
    8- Indicar el mayor de los promedios de kilometros por tipo de vehiculo.
    9- Informar el monto promedio de cada servicio realizado.


Los montos de los servicios son:
    - Auto: $15000
    - Camioneta: $25000
    - Moto: $10000
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")
        
        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_tipo_vehiculo = ["auto","moto","camioneta","auto","moto","camioneta",]
        self.lista_marca_vehiculo = [400,200,1000,500,600,800]

    def btn_agregar_on_click(self):

        respuesta = True

        while respuesta == True:   

            tipo_de_vehiculo = prompt("Tipo", "Ingrese el tipo")
            while tipo_de_vehiculo == None or not tipo_de_vehiculo.isalpha() or tipo_de_vehiculo != "auto" and tipo_de_vehiculo != "camioneta" and tipo_de_vehiculo != "moto": 
                tipo_de_vehiculo = prompt("Error", "Error! Ingrese el tipo correctamente!")
                    
            self.lista_tipo_vehiculo.append(tipo_de_vehiculo)        
            
            kilometros = prompt("KM", "Ingrese los kilometros")    
            while kilometros == None or not kilometros.isdigit() or int(kilometros) < 0:
                kilometros = prompt("Error", "Error! Ingrese los kilometros correctamente!")

            kilometros = int(kilometros)

            self.lista_marca_vehiculo.append(kilometros)

            respuesta = question("Pregunta", "¿Desea agregar otro vehiculo?")   

    
    def btn_mostrar_on_click(self):
        for i, vehiculo in enumerate(self.lista_tipo_vehiculo):
            print(f"{i} - {vehiculo} - {self.lista_marca_vehiculo[i]}")


    def btn_informar_on_click(self):
       #1- El menor kilometraje y su tipo de vehiculo.
       
        menor_kilometraje = None

        for i, kilometraje in enumerate(self.lista_marca_vehiculo):
            if menor_kilometraje == None or kilometraje < menor_kilometraje:
                menor_kilometraje = kilometraje
                tipo_vehiculo_menor_kilometraje = self.lista_tipo_vehiculo[i]

        print(f"El vehiculo con menos kilometraje es: {tipo_vehiculo_menor_kilometraje} con {menor_kilometraje} KM")

        #8- Indicar el mayor de los promedios de kilometros por tipo de vehiculo.

        # lista_indices_autos = []
        # lista_indices_motos = []
        # lista_indices_camionetas = []

        # for i, tipo in self.lista_tipo_vehiculo:
        #     match tipo:
        #         case "auto":
        #             lista_indices_autos.append(i)      
        #         case "moto":
        #             lista_indices_motos.append(i)
        #         case "camioneta":
        #             lista_indices_camionetas.append(i)

       
if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()