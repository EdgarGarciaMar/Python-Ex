import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')


def enviar():
    print(entrada2.get())
    #seleccionar el texto
    entrada2.select_range(0,tk.END)
    entrada2.focus()
    #Vaciar la entrada
    entrada2.delete(0,tk.END)


#With es la cantidad de caracteres de la caja, justify es la justificacion del texto
#state=tk.DISABLED BLOQUEAR LA ENTRADA
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL)#show es para paswords show="*"
entrada1.grid(row=0,columnspan=2,pady=20)
#Insert texto de ayuda
entrada1.insert(0,"Introduce una cadena") # primer argumento es la posicion
entrada1.config(state="readonly") #para poner la entrada solo lectura


entrada2 = ttk.Entry(ventana, width=30, justify=tk.LEFT, state=tk.NORMAL)
entrada2.grid(row=1,column=0,padx=0)

boton1 = tk.Button(ventana,text="Guardar",command=enviar)
boton1.grid(row=1,column=1,sticky="NSWE",padx=0)


ventana.mainloop()