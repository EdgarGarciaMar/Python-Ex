import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x400")
ventana.iconbitmap("icono.ico")

#definimos los metodos de los botones
def evento1():
    boton1.config(text="Boton 1 presionado")

def evento2():
    boton2.config(text="Boton 2 presionado")

#metodo grid en lugar de pack para acomodar los botones

boton1 = ttk.Button(ventana,text="Boton 1", command=evento1)
#metodo grid para pocicionarlo dentro de la matriz de posiciones
boton1.grid(row=0,column=0,sticky= "W")


boton2 = ttk.Button(ventana,text="Boton 2",command=evento2)
#Propiedad Sticki N norte,S sur,W izquierda E derecha
boton2.grid(row=1,column=0,sticky= "E")
ventana.mainloop()