import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


# Un jugador de League of Legends tiene un fin de semana libre y va a jugar partidas hasta que se canse.
# Para mejorar su jugabilidad, por cada partida jugada va a registrar:
# Modo de juego ("Normal", "Clasificatoria", "ARAM")
# Nombre del personaje que usó
# La cantidad de asesinatos (No puede ser negativo)
# Muertes (No puede ser negativo)
# Asistencias. (No puede ser negativo, hasta 40)

# De lo registrado, al jugador le interesa lo siguiente:

# a) El modo de juego más jugado.
# b) El personaje con el cual murió más.
# c) El promedio de asistencias.
# d) De la partida con mas asesinatos, el nombre del personaje y el modo de juego.

# lista_nombres_personajes = []
# lista_modos_de_juegos = []
# lista_cantidad_asesinatos = []
# lista_cantidad_muertes = []
# lista_cantidad_asistencias = []

# respuesta = True

# while respuesta:

#     modo_de_juego = prompt("Mod de juego", "Ingrese el modo de juego")
#     while modo_de_juego == None or not modo_de_juego.isalpha() or modo_de_juego != "Normal" and modo_de_juego != "Clasificatoria" and modo_de_juego != "ARAM": 
#         modo_de_juego = prompt("Error", "Error! Ingrese el modo de juego correctamente!")

#     lista_modos_de_juegos.append(modo_de_juego)

#     nombre_personaje = prompt("Nombre", "Ingrese el nombre")
#     while nombre_personaje == None or not nombre_personaje.isalpha():
#         nombre_personaje = prompt("Error", "Error! Ingresar el nombre correctamente!")
    
#     lista_nombres_personajes.append(nombre_personaje)

#     asesinatos = prompt("Asesinatos", "Ingrese la cantidad de asesinatos")
#     while asesinatos == None or not asesinatos.isdigit() or int(asesinatos) < 0:
#         asesinatos = prompt("Error", "Error! Ingrese la cantidad de asesinatos correctamente!") 

#     asesinatos = int(asesinatos)

#     lista_cantidad_asesinatos.append(asesinatos)                    

    # muertes = prompt("Muertes", "Ingrese la cantidad de muertes")
    # while muertes == None or not muertes.isdigit() or int(muertes) < 0:
    #     muertes = prompt("Error", "Error! Ingrese la cantidad de muertes correctamente!")    

    # muertes = int(muertes)

    # lista_cantidad_muertes.append(muertes)

    # asistencias = prompt("Asistencias", "Ingrese la cantidad de asistencias")
    # while asistencias == None or not asistencias.isdigit() or int(asistencias) < 0 or int(asistencias) > 40:
    #     asistencias = prompt("Error", "Error! Ingrese la cantidad de asistencias correctamente!")  

    # asistencias = int(asistencias)

    # lista_cantidad_asistencias.append(asistencias)

    # respuesta = question("Pregunta", "¿Quiere continuar?")

#-----------------------------------------------------------------------------------------------------------

#a) El modo de juego más jugado.

# contador_normal = 0
# contador_clasificatoria = 0
# contador_aram = 0

# for modo in lista_modos_de_juegos:

#     match modo:
#         case "Normal":
#             contador_normal += 1
#         case "Clasificatoria":
#             contador_clasificatoria += 1
#         case "ARAM":
#             contador_aram += 1        

# if contador_normal > contador_clasificatoria and contador_normal > contador_aram:
#     modo_de_juego_mas_jugado = "Normal"
# elif contador_clasificatoria > contador_normal and contador_clasificatoria > contador_aram:
#     modo_de_juego_mas_jugado = "Clasificatoria"
# elif contador_aram > contador_clasificatoria and contador_aram > contador_normal:
#     modo_de_juego_mas_jugado = "ARAM"
# else:
#     modo_de_juego_mas_jugado = "---No hay modo de juego mas jugado---"
    
# print(f"El modo de juego mas jugado es: {modo_de_juego_mas_jugado}")    

#-----------------------------------------------------------------------------------------------------------

# b) El personaje con el cual murió más.

# mayor_cantidad_muertes = None

# for i, muertes in enumerate(lista_cantidad_muertes):
    
#     if mayor_cantidad_muertes == None or muertes > mayor_cantidad_muertes:
#         mayor_cantidad_muertes = muertes
#         personaje_con_mas_muertes = lista_nombres_personajes[i]

       
# print(f"El personaje con mas muertes es: {personaje_con_mas_muertes} con {mayor_cantidad_muertes} muertes")

#-----------------------------------------------------------------------------------------------------------

#c) El promedio de asistencias.

# contador_asistencias = 0
# acumulador_asistencias = 0

# for asistencias in lista_cantidad_asistencias:
#     acumulador_asistencias += asistencias
#     contador_asistencias += 1

# if contador_asistencias != 0:
#     promedio_asistencias = acumulador_asistencias / contador_asistencias
# else:
#     promedio_asistencias = 0

# print(f"El promedio de asistencias es: {promedio_asistencias}")

#-----------------------------------------------------------------------------------------------------------

# d) De la partida con mas asesinatos, el nombre del personaje y el modo de juego.

# mayor_cantidad_asesinatos = None

# for i, asesinatos in enumerate(lista_cantidad_asesinatos):

#     if mayor_cantidad_asesinatos == None or asesinatos > mayor_cantidad_asesinatos:
#         mayor_cantidad_asesinatos = asesinatos
#         nombre_personaje_mas_asesinatos = lista_nombres_personajes[i]
#         modo_de_juego_con_mas_asesinatos = lista_modos_de_juegos[i]

# print(f"El modo de juego con mas asesinatos es {modo_de_juego_con_mas_asesinatos} y el personaje es {nombre_personaje_mas_asesinatos} con {mayor_cantidad_asesinatos} asesinatos")
