"""
FooDiary 2020
Joel Isaias Solano Ocampo
"""

from os import system       #librerias para limpiar y pausar consola.
import sys
from datetime import date   #libreria para obtener la fecha actual.
import csv                  #libreria para manejar archivos csv.

m = []                      #inicializando matriz.
today = date.today()        #asignando la fecha de hoy a la variable today.

# Funcion principal para desplegar el menu
def main():
    while True:
        system("cls")
        print("Hoy es:", today)
        print("""

╭━━━╮╱╱╱╱╱╭━━━╮
┃╭━━╯╱╱╱╱╱╰╮╭╮┃
┃╰━━┳━━┳━━╮┃┃┃┣┳━━┳━┳╮╱╭╮
┃╭━━┫╭╮┃╭╮┃┃┃┃┣┫╭╮┃╭┫┃╱┃┃
┃┃╱╱┃╰╯┃╰╯┣╯╰╯┃┃╭╮┃┃┃╰━╯┃
╰╯╱╱╰━━┻━━┻━━━┻┻╯╰┻╯╰━╮╭╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
        """)
        apartado(["1) Registrar alimento(s)","2) Ver registro alimenticio","3) Ayuda","4) Acerca de", "5) Salir"])
        opc = input("\nElige una opción: ")
        system("cls")
        if opc == "1":
            print("registrar()")
        elif opc == "2":
            print("ver()")
        elif opc == "3":
            ayuda()
        elif opc == "4":
            acerca()
        elif opc == "5":
            mensaje("Gracias por usar FooDiary. ¡Vuelve pronto!")
            break
        else:
            mensaje("Opción no valida. Vuelve a intentarlo.")
            system("pause")
    sys.exit()

#Funcion mensaje que recibe un string como parametro para darle formato.
def mensaje(t):
    l = ""
    for i in range(len(t)):
        l += "━"
    print("\n╭",l,"╮\n|",t,"|\n╰",l,"╯")

#Funcion apartado que recibe una lista como parametro para darle formato.
def apartado(t):
    max = 0
    for txt in t:
        if len(txt) > max:
            max = len(txt)
    l = ""
    for i in range(max):
        l += "━"
    print("┏",l,"┓\n")
    for txt in t:
        print(txt)
    print("\n┗",l,"┛")

#Funcion ayuda que le brinda informacion suficiente al usuario para que sepa como usar el programa.
def ayuda():
    print("""

╭━━━╮╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱┃┃
┃┃╱┃┣╮╱╭┳╮╭┳━╯┣━━╮
┃╰━╯┃┃╱┃┃┃┃┃╭╮┃╭╮┃
┃╭━╮┃╰━╯┃╰╯┃╰╯┃╭╮┃
╰╯╱╰┻━╮╭┻━━┻━━┻╯╰╯
╱╱╱╱╭━╯┃
╱╱╱╱╰━━╯
    """)
    apartado([
"1. ¿Cómo registrar mis alimentos?",
"R: Puedes registrar tus alimentos en Menú > Registrar alimento(s).",
"Después ingresa el nombre de tu alimento/bebida y presiona Enter.",
"Sigue agregando alimentos según lo qué hayas comido en tú día.",
"Si haz terminado, elige la opción de salir presionando 1.\n\n",

"2. ¿Dondé quedan los datos qué he registrado?",
"R: Tu historial alimenticio queda guardado en un archivo .csv qué",
"podrás encontrar en el directorio principal del programa.",
"Te recomendamos no mover el archivo para el buen funcionamiento 2",
"del programa. En caso de mover el archivo, en Menú > Configuración",
"> Directorio puedes cambiar el directorio predefinido por el nuevo",
"directorio de tú archivo .csv"
    ])
    system("pause")

#Funcion acerca que muestra toda la informacion del dessarrollo del programa.
def acerca():
    print("""

╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
┃┃╱┃┣━━┳━━┳━┳━━┳━━╮╭━╯┣━━╮
┃╰━╯┃╭━┫┃━┫╭┫╭━┫╭╮┃┃╭╮┃┃━┫
┃╭━╮┃╰━┫┃━┫┃┃╰━┫╭╮┃┃╰╯┃┃━┫
╰╯╱╰┻━━┻━━┻╯╰━━┻╯╰╯╰━━┻━━╯
    """)
    apartado(["FooDiary v1.0","Developed by Joel Isaias Solano Ocampo","Github: @JoelSolano59"])
    system("pause")

#Funcion archivo, generara un archivo .csv segun los datos recopilados en la matriz
def archivo(matriz):
    with open("historial_alimentos.csv","w") as inputFile:
        fecha = input("Ingresa la fecha de hoy (dd/mm/yyyy): ")
        hora = input("Ingresa la hora (hh/mm): ")
        header = "Fecha,Hora"
        for i in range(len(matriz)):
            header += ","+"Alimento "+str(i+1)
        header += "\n"
        fila = ""
        inputFile.write(header)
        fila += str(fecha)+","+str(hora)
        for alimento in matriz:
            fila += ","+str(alimento)
        inputFile.write(fila)
    main()

main()