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



