import tkinter as tk
import relleno_img as relleno

def generar_planilla():
    nombre = entry_nombre.get()
    direccion = entry_direccion.get()
    relleno.generar_imagen(nombre, direccion)

root = tk.Tk()
label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_direccion = tk.Label(root, text="Dirección:")
label_direccion.pack()
entry_direccion = tk.Entry(root)
entry_direccion.pack()

button_generar = tk.Button(root, text="Generar Planilla", command=generar_planilla)
button_generar.pack()

root.mainloop()
