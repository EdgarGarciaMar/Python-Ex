#Importamos el modulo para la gui
import tkinter as tk
#importamos botones
from tkinter import ttk

#Creamos la ventana
ventana = tk.Tk()
#modificar el tamaño de la ventana
ventana.geometry("600x400")
#cambio de nombre de la ventana
ventana.title("Hola mundo")
#Configuramos el icono de la app
ventana.iconbitmap('icono.ico')
#Agregamos un boton
def eventoClic():
    boton1.config(text="Boton presionado")#cambiar texto al presionar boton
    print("Clic")
    #crear nuevo boton
    boton2 = ttk.Button(ventana,text="Nuevo boton")
    boton2.pack()


boton1 = ttk.Button(ventana, text="Dar clic",command=eventoClic)
#pack layout manager para desplegar componentes
boton1.pack()
#Iniciamos la ventana (esta linea la ejecutamos al final)
#si se ejecuta antes del final no se actualizan las cosas
ventana.mainloop()
