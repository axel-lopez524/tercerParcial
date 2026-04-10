'''
import tkinter as tk
from tkinter import messagebox

def calcular_todo():
    try:
        
        nombre_completo = f"{entry_nom.get()} {entry_pat.get()} {entry_mat.get()}"
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        año = int(entry_anio.get())
        
        
        
        # 1. Calcular Edad
        
        edad =(2026-año)
        
        # 2. Calcular Signo Zodiacal Chino (Basado en el año)
        # El ciclo se repite cada 12 años
        
        signos = ["Rata": "",
    "Buey": "",
    "Tigre": "",
    "Conejo": "",
    "Dragón": "",
    "Serpiente": "serpiente.png",
    "Caballo": "caballo.png",
    "Cabra": "cabra.jpeg",
    "Mono": "mono.jpeg",
    "Gallo": "gallo.png",
    "Perro": "perro.jpeg",
    "Cerdo": "cerdo.jpeg"

            "Mono", "Gallo", "Perro", "Cerdo", "Rata",  
            "Tigre", "Conejo", "Dragón", "Serpiente", "Caballo", "Cabra","00"
        ]
        signo_resultado = signos[año % 12]
        
        # 3. Actualizar etiquetas de resultado
        lbl_res_nombre.config(text=f"Hola {nombre_completo}")
        lbl_res_edad.config(text=f"Tienes {edad} años")
        lbl_res_signo.config(text=f"tu signo zodiacal es {signo_resultado}")
        
        # Nota: Para la imagen, necesitarías un archivo .png o .gif 
        # Ejemplo: img = tk.PhotoImage(file="caballo.png")
        # lbl_imagen.config(image=img)
        
        
        img_path = signo_resultado[signos]
        try:
            img = Image.open(img_path)
            img = img.resize((120, 120))
            img_tk = ImageTk.PhotoImage(img)
            lbl_img.config(image=img_tk)
            lbl_img.image = img_tk
        except:
            lbl_img.config(text="Imagen no encontrada")


            
            
            
            
    except ValueError:
        messagebox.showerror("Error", "Por favor introduce números válidos en la fecha.")
        
    
        

# Configuración de la Ventana Principal
root = tk.Tk()
root.title("Cálculo de Datos Personales")
root.geometry("600x400")

# --- PANEL IZQUIERDO (FORMULARIO) ---
frame_izq = tk.Frame(root, padx=20, pady=20)
frame_izq.pack(side="left", fill="both")

tk.Label(frame_izq, text="Datos Personales", font=("Arial", 12, "bold")).grid(row=0, columnspan=2)

tk.Label(frame_izq, text="Nombre:").grid(row=1, column=0, sticky="e")
entry_nom = tk.Entry(frame_izq)
entry_nom.grid(row=1, column=1)

tk.Label(frame_izq, text="Apellido_paterno:").grid(row=2, column=0, sticky="e")
entry_pat = tk.Entry(frame_izq)
entry_pat.grid(row=2, column=1)

tk.Label(frame_izq, text="apellido_materno:").grid(row=3, column=0, sticky="e")
entry_mat = tk.Entry(frame_izq)
entry_mat.grid(row=3, column=1)

# Fecha de Nacimiento
tk.Label(frame_izq, text="Fecha de nacimiento", pady=10).grid(row=4, columnspan=2)
f_fecha = tk.Frame(frame_izq)
f_fecha.grid(row=5, columnspan=2)

tk.Label(f_fecha, text="Día").pack(side="left")
entry_dia = tk.Entry(f_fecha, width=3)
entry_dia.pack(side="left", padx=5)

tk.Label(f_fecha, text="Mes").pack(side="left")
entry_mes = tk.Entry(f_fecha, width=3)
entry_mes.pack(side="left", padx=5)

tk.Label(f_fecha, text="Año").pack(side="left")
entry_anio = tk.Entry(f_fecha, width=5)
entry_anio.pack(side="left", padx=5)

# Sexo (Radio Buttons)
tk.Label(frame_izq, text="sexo").grid(row=6, column=0, pady=10)
var_sexo = tk.IntVar()
tk.Radiobutton(frame_izq, text="Masculino", variable=var_sexo, value=1).grid(row=7, column=1, sticky="w")
tk.Radiobutton(frame_izq, text="Femenino", variable=var_sexo, value=2).grid(row=8, column=1, sticky="w")

btn_imprimir = tk.Button(frame_izq, text="imprimir", command=calcular_todo, bg="white", relief="solid")
btn_imprimir.grid(row=9, columnspan=2, pady=20)

# --- PANEL DERECHO (RESULTADOS) ---
frame_der = tk.Frame(root, padx=20, pady=20)
frame_der.pack(side="right", fill="both", expand=True)

lbl_res_nombre = tk.Label(frame_der, text="", font=("Arial", 12, "italic bold"))
lbl_res_nombre.pack(pady=5)

lbl_res_edad = tk.Label(frame_der, text="", font=("Arial", 11))
lbl_res_edad.pack(pady=5)

lbl_res_signo = tk.Label(frame_der, text="", font=("Arial", 11))
lbl_res_signo.pack(pady=5)

lbl_imagen = tk.Label(frame_der) # Aquí iría la imagen del signo
lbl_imagen.pack(pady=10)

root.mainloop()
'''
import tkinter as tk
from tkinter import messagebox
# Importamos PIL para manejar imágenes JPG/PNG (requiere: pip install Pillow)
from PIL import Image, ImageTk 

def calcular_todo():
    try:
        # Obtener datos de la interfaz
        nombre = entry_nom.get()
        paterno = entry_pat.get()
        materno = entry_mat.get()
        nombre_completo = f"{nombre} {paterno} {materno}"
        
        año = int(entry_anio.get())
        
        # 1. Calcular Edad (Asumiendo que estamos en 2026)
        edad = 2026 - año
        
        # 2. Diccionario de Signos (Año % 12)
        # 0: Mono, 1: Gallo, 2: Perro, 3: Cerdo, 4: Rata, 5: Buey, 
        # 6: Tigre, 7: Conejo, 8: Dragón, 9: Serpiente, 10: Caballo, 11: Cabra
        dict_signos = {
            0: ("Mono", "mono.png"),
            1: ("Gallo", "gallo.png"),
            2: ("Perro", "perro.png"),
            3: ("Cerdo", "cerdo.jpg"),
            4: ("Rata", "rata.png"),
            5: ("Buey", "toro.jpg"),
            6: ("tiger", "tiger.png"),
            7: ("Conejo", "conejo.png"),
            8: ("Dragón", "dragon.png"),
            9: ("Serpiente", "serpiente.png"),
            10: ("Caballo", "caballo.png"),
            11: ("Cabra", "cabra.png")
        }
        
        indice = año % 12
        nombre_signo, img_path = dict_signos[indice]
        
        # 3. Actualizar etiquetas de texto
        lbl_res_nombre.config(text=f"Hola {nombre_completo}")
        lbl_res_edad.config(text=f"Tienes {edad} años")
        lbl_res_signo.config(text=f"Tu signo zodiacal es {nombre_signo}")
        
        # 4. Manejo de la Imagen
        try:
            imagen = Image.open(img_path)
            imagen = imagen.resize((120, 120), Image.Resampling.LANCZOS)
            img_tk = ImageTk.PhotoImage(imagen)
            lbl_imagen.config(image=img_tk, text="") # Quitamos el texto si hay imagen
            lbl_imagen.image = img_tk # Referencia para que no desaparezca
        except Exception:
            lbl_imagen.config(image="", text="(Imagen no encontrada)")

    except ValueError:
        messagebox.showerror("Error", "Por favor introduce un año válido (números).")

# --- Configuración de la Ventana ---
root = tk.Tk()
root.title("Cálculo de Datos Personales")
root.geometry("650x450")

# --- PANEL IZQUIERDO (FORMULARIO) ---
frame_izq = tk.Frame(root, padx=20, pady=20)
frame_izq.pack(side="left", fill="both")

tk.Label(frame_izq, text="Datos Personales", font=("Arial", 12, "bold")).grid(row=0, columnspan=2, pady=10)

tk.Label(frame_izq, text="Nombre:").grid(row=1, column=0, sticky="e")
entry_nom = tk.Entry(frame_izq)
entry_nom.grid(row=1, column=1)

tk.Label(frame_izq, text="Ap. Paterno:").grid(row=2, column=0, sticky="e")
entry_pat = tk.Entry(frame_izq)
entry_pat.grid(row=2, column=1)

tk.Label(frame_izq, text="Ap. Materno:").grid(row=3, column=0, sticky="e")
entry_mat = tk.Entry(frame_izq)
entry_mat.grid(row=3, column=1)

# Fecha de Nacimiento
tk.Label(frame_izq, text="Fecha de nacimiento", pady=10).grid(row=4, columnspan=2)
f_fecha = tk.Frame(frame_izq)
f_fecha.grid(row=5, columnspan=2)

tk.Label(f_fecha, text="Día").pack(side="left")
entry_dia = tk.Entry(f_fecha, width=4)
entry_dia.pack(side="left", padx=2)

tk.Label(f_fecha, text="Mes").pack(side="left")
entry_mes = tk.Entry(f_fecha, width=4)
entry_mes.pack(side="left", padx=2)

tk.Label(f_fecha, text="Año").pack(side="left")
entry_anio = tk.Entry(f_fecha, width=6)
entry_anio.pack(side="left", padx=2)

# Sexo
tk.Label(frame_izq, text="Sexo:").grid(row=6, column=0, pady=10)
var_sexo = tk.IntVar()
tk.Radiobutton(frame_izq, text="Masculino", variable=var_sexo, value=1).grid(row=7, column=1, sticky="w")
tk.Radiobutton(frame_izq, text="Femenino", variable=var_sexo, value=2).grid(row=8, column=1, sticky="w")

btn_imprimir = tk.Button(frame_izq, text="CALCULAR", command=calcular_todo, bg="#e1e1e1", width=15)
btn_imprimir.grid(row=9, columnspan=2, pady=20)

# --- PANEL DERECHO (RESULTADOS) ---
frame_der = tk.Frame(root, padx=20, pady=20, bg="#f0f0f0")
frame_der.pack(side="right", fill="both", expand=True)

lbl_res_nombre = tk.Label(frame_der, text="", font=("Arial", 11, "bold"), bg="#f0f0f0")
lbl_res_nombre.pack(pady=5)

lbl_res_edad = tk.Label(frame_der, text="", font=("Arial", 10), bg="#f0f0f0")
lbl_res_edad.pack(pady=5)

lbl_res_signo = tk.Label(frame_der, text="", font=("Arial", 10), bg="#f0f0f0")
lbl_res_signo.pack(pady=5)

lbl_imagen = tk.Label(frame_der, bg="#f0f0f0") 
lbl_imagen.pack(pady=10)

root.mainloop()