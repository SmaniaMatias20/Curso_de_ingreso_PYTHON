import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se debera cargar el peso* de un articulo, el cual podra ser ingresado en gramos o en onzas 

    La unidad de medida es indicada mediante una lista desplegable.

* Flotantes mayores que cero

Si existe error al validar indicarlo mediante un Alert
Si se cargo  correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los pesos en gramos, en onzas y su posicion en la lista (por terminal)

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al precionar el boton Informar 
    0- Valor (en onzas) y posicion del articulo mas pesado
    1- Valor (en gramos) y posicion del articulo mas liviano
    2- Peso promedio (en onzas) 
    3- Peso promedio (en gramos)
    4- Informar los pesos que superan el promedio (en gramos)
    5- Informar los pesos que NO superan el promedio (en onzas)
    6- Informar la cantidad de articulos que superan el peso promedio
    7- Informar la cantidad de articulos que NO superan el peso promedio
    8- Indicar los pesos repetidos (gramos)
    9- Indicar los pesos NO repetidos (gramos)


1 gramo son 0.035274 oz
1 oz son 28.3495 gramos
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("RECUPERATORIO EXAMEN INGRESO")

        self.txt_peso_articulo = customtkinter.CTkEntry(master=self, placeholder_text="PESO")
        self.txt_peso_articulo.grid(row=1, padx=20, pady=20)

        self.combobox_tipo_de_peso = customtkinter.CTkComboBox(master=self, values=["Gramos","Onzas"])
        self.combobox_tipo_de_peso.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_pesos = []


    def btn_agregar_on_click(self):
        validacion = True
        contador_puntos = 0

        peso_ingresado = self.txt_peso_articulo.get()
        unidad_de_medida = self.combobox_tipo_de_peso.get()
        
        if peso_ingresado != "":
            for letra in peso_ingresado:
                if letra == ".":
                    contador_puntos += 1

                if letra.isalpha() or letra == " ":
                    validacion = False            
        else:
            validacion = False
            
        if contador_puntos >= 2:
            validacion = False            
    
        if validacion:
            peso_ingresado = float(peso_ingresado)

            if peso_ingresado <= 0:
                validacion = False

        if validacion:
            alert("Numero", "El peso ingresado es correcto")

            if unidad_de_medida == "Onzas":
                peso_ingresado = peso_ingresado * 28.3495
            
            self.lista_pesos.append(peso_ingresado)
        else:
            alert("Error", "Error! El peso ingresado no es correcto")
            

        self.txt_peso_articulo.delete(0,100)     

    
    def btn_mostrar_on_click(self):
        contador = 0

        for peso in self.lista_pesos:
            print(f"\nPeso: {peso}")
            print(f"Posicion: {contador}" )
            contador += 1

    def btn_informar_on_click(self):
        lista_numeros_repetidos = []
        lista_mayores_promedio = []
        contador = 0
        contador_2 = 0
        acumulador_peso = 0
        bandera = True

        for peso in self.lista_pesos:
            contador += 1
            acumulador_peso += peso 
            for peso_2 in self.lista_pesos:
                contador_2 += 1
                if peso_2 == peso and contador != contador_2:
                        
                    if lista_numeros_repetidos.count(peso) == 0:
                        lista_numeros_repetidos.append(peso)

            contador_2 = 0

            if bandera:
                peso_mas_liviano = peso
                bandera = False
            
            if peso < peso_mas_liviano:
                peso_mas_liviano = peso

        if contador != 0:
            promedio_peso = acumulador_peso // contador    
        else:
            promedio_peso = 0

        for peso in self.lista_pesos:
            if peso > promedio_peso:
                lista_mayores_promedio.append(peso)

        alert("Peso", f"El peso mas liviano es: {peso_mas_liviano}")

        for numero_repetido in lista_numeros_repetidos:
            alert("Numero repetido", f"Numero repetido: {numero_repetido}")  

        alert("Promedio", f"El promedio de peso es: {promedio_peso}")

        for numero in lista_mayores_promedio:
            alert("Numeros", f"Numeros mayores al promedio: {numero}")  
            
        alert("Cantidad", f"La cantidad de articulos que superan el peso promedio es: {len(lista_mayores_promedio)}")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()