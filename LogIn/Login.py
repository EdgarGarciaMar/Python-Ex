import tkinter as tk
from tkinter import ttk, messagebox

from PIL import ImageTk, Image

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.iconbitmap('login.ico')


image = Image.open("login.png")
image = image.resize((50, 50))
img = ImageTk.PhotoImage(image)
imagen = tk.Label(ventana,image=img)
imagen.grid(row=0,column=0,columnspan=2)

#función para login
def login():
    usuario = usuarioText.get()
    password = passwordText.get()

    if usuario == "Ed" and password == "1234":
        messagebox.showwarning("Bienvenido","Hola "+ usuario)
    else:
        messagebox.showwarning("Error", "Acceso denegado")

#Etiqueta nombre usuario
etiquetaUsuario = tk.Label(ventana,text="Usuario",justify=tk.CENTER)
etiquetaUsuario.grid(row=1, column=0)

#Entrada del nombre usuario
usuarioText= tk.StringVar(value="")
entradaUsuario = ttk.Entry(ventana, width=25, justify=tk.LEFT, state=tk.NORMAL, textvariable=usuarioText)
entradaUsuario.grid(row=1,column=1)

#Etiqueta password
etiquetaPassword = tk.Label(ventana,text="Password",justify=tk.CENTER)
etiquetaPassword.grid(row=2, column=0,)

#Entrada password
passwordText = tk.StringVar(value="")
entradaPassword = ttk.Entry(ventana, width=25, justify=tk.LEFT, state=tk.NORMAL, textvariable=passwordText, show="*")
entradaPassword.grid(row=2,column=1)

#Boton
enviar = tk.Button(ventana,text="Ingresar",command=login)
enviar.grid(row=3,column=1,sticky="NSWE",columnspan=2)

ventana.mainloop()