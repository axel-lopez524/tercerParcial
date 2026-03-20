

'''def crear_archivo():
    nombre = input("Nombre del archivo: ")
    with open(nombre, "w") as archivo:
        print("Archivo creado correctamente")
        
crear_archivo()'''

'''def escribir_archivo():
    nombre = input("Nombre del archivo: ")
    texto = input("Escribe el texto a guardar: ")
    
    with open(nombre, "a") as archivo:
        archivo.write("\n" + texto)
        
    print("Texto agregado correctamente")'''
        
        
def escribir_archivo():
    nombre=input("nombre del archivo: ")
    
    try:
        
        with open(nombre, "r") as archivo:
            contenido = archivo.read()
            print("\ncontenido del archivo: ")
            print(contenido)
    except FileNotFoundError:
        print("El archivo no exite")
        
escribir_archivo() 

import os
def leer_archivo():
    nombre= input(" Nombre del archivo: ")
    try:
        with open(nombre,"r") as archivo:
            contenido= archivo.read()
            os.system("cls")
            print("\nContenido del archivo: ")
            print(contenido)
            print("|---------------------------|")
            archivo.seek(0)
            contenido= archivo.read()
            print("\nContenido del archivo: ")
            print(contenido)
    except FileNotFoundError:
        print("El archivo no existe")        

def buscar_palabra():
    nombre= input("Nombre del archivo: ")
    palabra= input("Palabra a buscar: ")

    try:
        with open(nombre, "r") as archivo:
            contenido= archivo.read()

            if palabra in contenido:
                print("La palabra fue encontrada")
            else:
                print("La palabra no fue encontrada en el archivo")
    except FileNotFoundError:
        print ("El archivo no existe")


def menu():
    while True:
        print("\n---Gestor de archivos---")
        print("1. Crear Archivo")
        print("2. Escribir en Archivo")
        print("3. Agregar Texto")
        print("4. Leer Archivo")
        print("5. Buscar Palabra")
        print("6. Salir")

        opcion = input("Seleccione una ocpion: ")

        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            escribir_archivo()
        elif opcion == "3":
            agregar_texto()
        elif opcion == "4":
            leer_archivo()
        elif opcion == "5":
            buscar_palabra()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")
menu()      
