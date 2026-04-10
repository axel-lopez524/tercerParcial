'''
import tkinter as tk
from tkinter import messagebox

def carga_diccionario():
    diccionario = {}
    try:
        with open("diccionario.txt", "r") as f:
            for linea in f:
                esp, ing =linea.strip().split(",")
                diccionario[esp.lower()] = ing.lower()
                
    except:
        pass
    return diccionario

def guardar_palabras(esp, ing):
    with open("diccionario.txt", "a") as f:
        f.write(f"{esp},{ing}\n")
        
def traducir():
    palabra = entrada.get().lower()
    diccionario = carga_diccionario
    
    if.pcion.get() == 1:
        resultado= diccionario.get(palabra, "No encontrada")
    else:
        inv_diccionario = {v: k for k, v in diccionario.items()}
        resultado = inv_diccionario.get(palabra,"No encontrada")
        
        
    b_resultado_config
    
    
    
def agregar():
    español =entrada_esp.get().lower()
    ingles =entrada_ing.get().lower() 
    
    if español= "" or ingles == "":
        messagebox.showerror("Error", "Campos vacios")
        return
    
    guardar_palabra(español,ingles)
    messagebox.showinfo("Exito", "palabra agregada")
    
    
root = tk.Tk()
root.title("Traductor")
root.geometry("350x350")

entrada = tk.Entry(root)

entrada.pack(pady=10)    
        
opcion = tk.InVar()
opcion.set(1)     


tk.Radiobutton(root, text= "Español -> Ingles", variable=opcion, value=1).pack()
tk.Radiobutton(root, text= "Ingles -> Español", variable=opcion, value=2).pack()

tk.button(root, text = "Traducir", command=traducir).pack(padt=10)

b_resultado = tk.Label(root, text="")
b_resultado.pack(pady=10)

tk.Label(root, text= "Agregar nueva palabra").pack()
entrada_esp = tk.Entry(root)
entrada_esp.pack()
entrada_esp.insert(0,"español")

tk.Label(root, text= "Agregar nueva palabra").pack()
entrada_ing = tk.Entry(root)
entrada_ing.pack()
entrada_ing.insert(0,"ingles")

tk.button(root, text="Agregar", command=agregar).pack(pady=10)

root.mainloop()
'''
import tkinter as tk
from tkinter import messagebox

# Cargar palabras desde archivo
def cargar_diccionario():
    dic = {}
    try:
        # Se corrigió "withopen" por "with open"
        with open("Diccionario.txt", "r") as f:
            for linea in f:
                # Se limpia la línea y se separa por la coma
                partes = linea.strip().split(",")
                if len(partes) == 2:
                    esp, ing = partes
                    dic[esp.lower()] = ing.lower()
    except:
        pass  # Si el archivo no existe, retorna el diccionario vacío
    return dic

# Guardar nueva palabra 
def guardar_palabra(esp, ing):
    # Se corrigió "withopen" por "with open"
    with open("Diccionario.txt", "a") as f:
        f.write(f"{esp.lower()},{ing.lower()}\n")
        
# Traduccion
def traducir():
    palabra = entrada.get().lower()
    dic = cargar_diccionario()
    
    if opcion.get() == 1:
        resultado = dic.get(palabra, "No encontrada")
    else:
        inv_dic = {v: k for k, v in dic.items()}
        resultado = inv_dic.get(palabra, "No encontrada")
        
    lbl_resultado.config(text=resultado)
    
# Agregar nueva palabra
def agregar():
    esp = entrada_esp.get().lower()
    ing = entrada_ing.get().lower()
    
    if esp == "" or ing == "":
        messagebox.showerror("Error", "Campos Vacios")
        return
    
    guardar_palabra(esp, ing)
    messagebox.showinfo("Exito", "Palabra Agregada")
    
#=======================================================================
# INTERFAZ
root = tk.Tk()
root.title("Traductor")
root.geometry("350x400")

# Entrada
entrada = tk.Entry(root)
entrada.pack(pady=10)

# Se corrigió tk.IntVar a tk.IntVar()
opcion = tk.IntVar()
opcion.set(1)

tk.Radiobutton(root, text="Espanol -> Ingles", variable=opcion, value=1).pack()
tk.Radiobutton(root, text="Ingles -> Espanol", variable=opcion, value=2).pack()

# Boton traducir
tk.Button(root, text="Traducir", command=traducir).pack(pady=10)

# Resultado
lbl_resultado = tk.Label(root, text="")
lbl_resultado.pack(pady=10)

# Seccion Agregar
tk.Label(root, text="Agregar nueva palabra").pack()

entrada_esp = tk.Entry(root)
entrada_esp.pack()
entrada_esp.insert(0, "espanol")

entrada_ing = tk.Entry(root)
entrada_ing.pack()
entrada_ing.insert(0, "ingles")

tk.Button(root, text="Agregar", command=agregar).pack(pady=10)

root.mainloop()

