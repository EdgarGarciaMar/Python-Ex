import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Menu GUI')
ventana.iconbitmap('icono.ico')


def enviar():
    mensaje1 = entrada2.get()
    print(mensaje1)
    #Vaciar la entrada
    entrada2.delete(0,tk.END)
    messagebox.showwarning("Alerta", mensaje1+ "Alerta")

def salir():
    messagebox.showinfo("Salida","Saliendo de la app")
    ventana.quit()
    ventana.destroy()
    sys.exit()

def crearMenu():
    #Configurar menu
    menuPrincipal = Menu(ventana)

    #Tearoff = false(0) para que no se separe de la gui
    submenuArchivo = Menu(menuPrincipal,tearoff=0)
    #Agregamos una nueva opc a menu archivo
    submenuArchivo.add_command(label="Nuevo")
    #Agregar un separador
    submenuArchivo.add_separator()
    #Otra opc
    submenuArchivo.add_command(label="Salir", command=salir)#Metodo para la funcionalidad del menu
    #Agregamos el submenu al menu principal
    menuPrincipal.add_cascade(menu=submenuArchivo,label="Archivo")


    #Agregamos un nuevo submenu
    submenuAyuda = Menu(menuPrincipal,tearoff=0)
    #nueva opc de submenu a submenu ayuda
    submenuAyuda.add_command(label="Acerca de")
    #Agregamos al menu principal
    menuPrincipal.add_cascade(menu=submenuAyuda, label="Ayuda")

    #Mostramos el menu en la ventana
    ventana.config(menu=menuPrincipal)


#Etiqueta
etiqueta1 = tk.Label(ventana,text="Instrucciones",justify=tk.CENTER)
etiqueta1.grid(row=0, column=1, columnspan=2)

#Entrada
entrada2 = ttk.Entry(ventana, width=30, justify=tk.LEFT, state=tk.NORMAL)
entrada2.grid(row=1,column=0,padx=0)

#Boton
boton1 = tk.Button(ventana,text="Guardar",command=enviar)
boton1.grid(row=1,column=1,sticky="NSWE",padx=0)

#Menu
crearMenu()
ventana.mainloop()