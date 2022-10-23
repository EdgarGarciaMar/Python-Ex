import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# Configurar el grid
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.rowconfigure(2, weight=5)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)


# Métodos de los eventos
def evento1():
    boton1.config(text='Botón 1 presionado')

def evento2():
    boton2.config(text='Botón 2 presionado')

def evento4():#fg cambiar color, relief cambiar el contorno,bg background color
    boton4.config(text="Botón 4 presionado", fg="blue", relief=tk.GROOVE, bg="red")

# Definimos los botones
boton1 = tk.Button(ventana, text='Botón 1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSWE',padx=40, pady=30, ipadx=20, ipady=50)#pading x en los lados, y arriba abajo cuando tiene ipad es porque es interno

# N(arriba), E(derecha), S(abajo), W(izquierda)
boton2 = tk.Button(ventana, text='Botón 2', command=evento2)
boton2.grid(row=1,column=0, sticky='NSWE')

# Boton3
boton3 = tk.Button(ventana, text='Botón 3')
boton3.grid(row=0, column=1, sticky='NSWE')

# Boton4 al suasr ttk hay estilos, pero no se redimenciona
#tk se redimensiona sin estilos
boton4= tk.Button(ventana,text='Botón 4',command=evento4)
boton4.grid(row=1, column=1, sticky='NSWE')

#boton 5 con col y row span
boton5 = tk.Button(ventana,text="Botón 5")
boton5.grid(row=2,column=0,sticky="NSWE", columnspan=2, rowspan=2) #span se expanden y toman las columnas y filas es como un juntar celdas

ventana.mainloop()
