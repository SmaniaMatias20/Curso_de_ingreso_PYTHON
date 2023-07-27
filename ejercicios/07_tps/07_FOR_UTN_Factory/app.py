'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
    ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
    necesarias para tomar decisiones a la hora de la selección:

    Nombre
    Edad (mayor de edad)
    Género (F-M-NB)
    Tecnología (PYTHON - JS - ASP.NET)
    Puesto (Jr - Ssr - Sr)

    Informar por pantalla:
    a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
    cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
    b. Nombre del postulante Jr con menor edad. 
    c. Promedio de edades por género.
    d. Tecnologia con mas postulantes (solo hay una).
    e. Porcentaje de postulantes de cada genero.

    Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

    '''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        postulantes_no_binarios_aspnet_js = 0
        menor_edad_jr = 0
        acumulador_edad_f = 0
        acumulador_edad_m = 0
        acumulador_edad_nb = 0
        contador_edad_f = 0
        contador_edad_m = 0
        contador_edad_nb = 0
        contador_tecnologia_python = 0
        contador_tecnologia_js = 0
        contador_tecnologia_net = 0
        contador_genero_m = 0
        contador_genero_f = 0
        contador_genero_nb = 0
        nombre_jr_menor_edad = "No hay postulantes JR"
        

        for _ in range(10):
            nombre = prompt("Nombre", "Ingrese su nombre")
            while nombre == None or not nombre.isalpha():
                nombre = prompt("Nombre", "Error! Ingrese su nombre correctamente")

            edad = prompt("Edad", "Ingrese su edad")

            while edad == None or not edad.isdigit():
                edad = prompt("Edad", "Error! Ingrese su edad")

            edad = int(edad)

            while edad < 18 or edad > 90:
                edad = prompt("Edad", "Error! Ingrese su edad correctamente")
                if edad == None or edad == "":
                    edad = 0
                else:
                    edad = int(edad)

               
            genero = prompt("Genero", "Ingrese su genero F/M/NB")
            while genero == None or not genero.isalpha() or genero.upper() != "M" and genero.upper() != "F" and genero.upper() != "NB":
                genero = prompt("Genero", "Error! Ingrese el genero correctamente F/M/NB")

            tecnologia = prompt("Tecnologia", "Ingrese la tecnologia PYTHON/JS/ASP.NET")
            while tecnologia == None or tecnologia.isdigit() or tecnologia.upper() != "PYTHON" and tecnologia.upper() != "JS" and tecnologia.upper() != "ASP.NET" : 
                tecnologia = prompt("Tecnologia", "Error! Ingrese la tecnologia PYTHON/JS/ASP.NET")

            puesto = prompt("Puesto", "Ingrese su puesto JR/SSR/SR")   
            while puesto == None or not puesto.isalpha() or puesto.upper() != "JR" and puesto.upper() != "SSR" and puesto.upper() != "SR" :
                puesto = prompt("Puesto", "Error! Ingrese el puesto JR/SSR/SR") 

            
            if genero.upper() == "NB" and (tecnologia.upper() == "ASP.NET" or tecnologia.upper() == "JS"):
                if edad >= 25 and edad <= 40:
                    if puesto.upper() == "SR":
                        postulantes_no_binarios_aspnet_js += 1


            if puesto.upper() == "JR":
                if menor_edad_jr == 0:
                    menor_edad_jr = edad
                    nombre_jr_menor_edad = nombre

                if edad < menor_edad_jr:
                    nombre_jr_menor_edad = nombre
                    menor_edad_jr = edad

            match genero.upper():
                case "M":
                    acumulador_edad_m += edad
                    contador_edad_m += 1
                    contador_genero_m += 1
                case "F":
                    acumulador_edad_f += edad
                    contador_edad_f += 1
                    contador_genero_f += 1
                case "NB":
                    acumulador_edad_nb += edad
                    contador_edad_nb += 1
                    contador_genero_nb += 1

            if tecnologia.upper() == "PYTHON":
                contador_tecnologia_python += 1
            elif tecnologia.upper() == "JS":
                contador_tecnologia_js += 1  
            else:
                contador_tecnologia_net += 1       

        if contador_edad_m != 0:       
            promedio_edad_m = acumulador_edad_m // contador_edad_m
        else:
            promedio_edad_m = 0

        if contador_edad_f != 0:
            promedio_edad_f = acumulador_edad_f // contador_edad_f
        else:
            promedio_edad_f = 0    
        
        if contador_edad_nb != 0:
            promedio_edad_nb = acumulador_edad_nb // contador_edad_nb
        else:
            promedio_edad_nb = 0    
        

        #PUNTO D
        if contador_tecnologia_python > contador_tecnologia_js and contador_tecnologia_python > contador_edad_nb:
            tecnologia_con_mas_postulantes = "PYTHON"
        elif contador_tecnologia_js > contador_tecnologia_python and contador_tecnologia_js > contador_edad_nb:
            tecnologia_con_mas_postulantes = "JS"
        else:
            tecnologia_con_mas_postulantes = "ASP.NET"  

        #PUNTO E

        porcentaje_genero_m = (contador_genero_m * 100) / 10
        porcentaje_genero_f = (contador_genero_f * 100) / 10
        porcentaje_genero_nb = (contador_genero_nb * 100) / 10      

        print(f"""La cantidad de postulantes no binarios que programan en ASP.NET o JS,
        tienen edad entre 25 y 40 años y son SR es: {postulantes_no_binarios_aspnet_js}""")

        print(f"\nEl nombre del postulante JR con menor edad es: {nombre_jr_menor_edad}")

        print(f"""\nEl promedio de edades por genero es ---> 
        \nMasculino: {promedio_edad_m}
        \nFemenino: {promedio_edad_f} 
        \nNo Binario: {promedio_edad_nb}
        """)

        print(f"\nLa tecnologia con mas postulantes es: {tecnologia_con_mas_postulantes}")

        print(f"""\nEl porcentaje por genero de los postulantes es: 
        \nMasculino: {porcentaje_genero_m}%
        \nFemenino: {porcentaje_genero_f}% 
        \nNo Binario: {porcentaje_genero_nb}%
        """)





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
