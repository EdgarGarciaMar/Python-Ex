import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Mensajes')
ventana.iconbitmap('icono.ico')



def enviar():
    mensaje1 = entrada2.get()
    print(mensaje1)
    #Vaciar la entrada
    entrada2.delete(0,tk.END)
    #cajas de mensajes// se ve mejor en windows
    #messagebox.showinfo("Mensaje Info",mensaje1+" mensaje info")
    #messagebox.showerror("Mensaje de Error", mensaje1+ "Error")
    messagebox.showwarning("Alerta", mensaje1+ "Alerta")
#Etiqueta
etiqueta1 = tk.Label(ventana,text="Instrucciones",justify=tk.CENTER)
etiqueta1.grid(row=0, column=1, columnspan=2)

entrada2 = ttk.Entry(ventana, width=30, justify=tk.LEFT, state=tk.NORMAL)
entrada2.grid(row=1,column=0,padx=0)

boton1 = tk.Button(ventana,text="Guardar",command=enviar)
boton1.grid(row=1,column=1,sticky="NSWE",padx=0)


ventana.mainloop()