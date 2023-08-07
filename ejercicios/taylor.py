import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

# Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de comprar cada entrada:

# * Nombre del comprador
# * Edad (no menor a 16)
# * Género (Masculino, Femenino, Otro)
# * Tipo de entrada (General, Campo delantero, Platea)
# * Medio de pago (Crédito, Efectivo, Débito) 
# * Precio de la entrada (Se debe calcular)

# Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, el medio de pago y su precio correspondiente.

# Lista de precios: 
# General: $16000
# Campo: $25000
# Platea: $30000

# Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 


# Al finalizar la venta de entradas, los organizadores quieren obtener la siguiente información:

# Cantidad total de dinero recaudado por las ventas de entradas.
# Cantidad de entradas vendidas para cada tipo.
# Promedio de edad de las personas que compraron ubicación en Platea.
# Nombre de la persona de mayor edad que compró una entrada de platea.
# Porcentaje de entradas vendidas de tipo "general"
# Nombre de la/s persona/s de mayor edad, de género Masculino que compro una entrada general.
# Tipo de entradas más vendidas

lista_generos = []
lista_nombres = []
lista_edades = []
lista_tipos_entradas = []
lista_precios_entradas = []
precio_entrada = 0
respuesta = True

while respuesta == True:
        
    nombre = prompt("Nombre", "Ingrese el nombre")
    while nombre == None or not nombre.isalpha():
        nombre = prompt("Error", "Error! Ingresar el nombre correctamente!")

    lista_nombres.append(nombre)            
                    
    edad = prompt("Edad", "Ingrese su edad")
    while edad == None or not edad.isdigit() or int(edad) < 16 or int(edad) > 90:
        edad = prompt("Error", "Error! Ingrese la edad correctamente!")   

    edad = int(edad)

    lista_edades.append(edad)

    genero = prompt("Genero", "Ingrese el genero: Masculino/Femenino/Otro")
    while genero == None or not genero.isalpha() or genero != "Masculino" and genero != "Femenino" and genero != "Otro": 
        genero = prompt("Error", "Error! Ingrese el genero correctamente!")      

    lista_generos.append(genero)

    tipo_entrada = prompt("Entrada", "Ingrese el tipo entrada: General/Campo delantero/Platea")
    while tipo_entrada == None or not tipo_entrada.isalpha() or tipo_entrada != "General" and tipo_entrada != "Campo delantero" and tipo_entrada != "Platea": 
        tipo_entrada = prompt("Error", "Error! Ingrese el tipo de entrada correctamente!")        

    lista_tipos_entradas.append(tipo_entrada)

    medio_de_pago = prompt("Pago", "Ingrese el medio de pago: Credito/Efectivo/Debito")
    while medio_de_pago == None or not medio_de_pago.isalpha() or medio_de_pago != "Credito" and medio_de_pago != "Efectivo" and medio_de_pago != "Debito": 
        medio_de_pago = prompt("Error", "Error! Ingrese el medio de pago correctamente!") 
        
    match tipo_entrada:
        case "General":
            precio_entrada = 16000
            match medio_de_pago:
                case "Credito":
                    precio_entrada = precio_entrada * 0.80
                case "Debito":
                    precio_entrada = precio_entrada * 0.85
                case "Efectivo":
                    precio_entrada = 16000

        case "Campo delantero":
            precio_entrada = 25000
            match medio_de_pago:
                case "Credito":
                    precio_entrada = precio_entrada * 0.80
                case "Debito":
                    precio_entrada = precio_entrada * 0.85
                case "Efectivo":
                    precio_entrada = 25000   

        case "Platea":
            precio_entrada = 30000  
            match medio_de_pago:
                case "Credito":
                    precio_entrada = precio_entrada * 0.80
                case "Debito":
                    precio_entrada = precio_entrada * 0.85
                case "Efectivo":
                    precio_entrada = 30000      
    
    lista_precios_entradas.append(precio_entrada)

    respuesta = question("Pregunta", "¿Quiere comprar otra entrada?")
    
# Cantidad total de dinero recaudado por las ventas de entradas.

acumulador_dinero = 0

for precio in lista_precios_entradas:
    acumulador_dinero += precio

print(f"La cantidad total de dinero recaudado es: {acumulador_dinero}")

# Cantidad de entradas vendidas para cada tipo.

contador_platea = 0
contador_general = 0
contador_campo = 0

for tipo in lista_tipos_entradas:

    match tipo:
        case "General":
            contador_general += 1
        case "Campo delantero":
            contador_campo += 1
        case "Platea":
            contador_platea += 1

if contador_general > contador_campo and contador_general > contador_platea:
    mayor_tipo_entradas_vendidas = "General"
elif contador_campo > contador_general and contador_campo > contador_platea:
    mayor_tipo_entradas_vendidas = "Campo delantero"
elif contador_platea > contador_general and contador_platea > contador_campo:
    mayor_tipo_entradas_vendidas = "Platea"
else:
    mayor_tipo_entradas_vendidas = "---No hay un tipo de entrada que se haya vendido mas---"        

print(f"El tipo de entradas mas vendido es: {mayor_tipo_entradas_vendidas}")

# Promedio de edad de las personas que compraron ubicación en Platea.


# Nombre de la persona de mayor edad que compró una entrada de platea.
# Porcentaje de entradas vendidas de tipo "general"
# Nombre de la/s persona/s de mayor edad, de género Masculino que compro una entrada general.
# Tipo de entradas más vendidas