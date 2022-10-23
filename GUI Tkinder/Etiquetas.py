import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Etiquetas')
ventana.iconbitmap('icono.ico')


def enviar2():
    #recuperar la info
    print(var.get())
    etiqueta1.config(text=var.get())#poner texto en la etiqueta
    #modificar con set
    var.set("")




#Etiqueta
etiqueta1 = tk.Label(ventana,text="Instrucciones",justify=tk.CENTER)
etiqueta1.grid(row=0, column=1, columnspan=2)

var = tk.StringVar(value="valor por defecto") #variable modificalbe get y set
#variable de entrada modificable get y set
entrada3 = ttk.Entry(ventana, width=25, justify=tk.LEFT, state=tk.NORMAL, textvariable=var)
entrada3.grid(row=1, column=0)

boton2 = tk.Button(ventana,text="Guardar2",command=enviar2)
boton2.grid(row=1,column=1,sticky="NSWE",padx=0)

ventana.mainloop()