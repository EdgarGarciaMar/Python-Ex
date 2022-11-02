import tkinter as tk
from tkinter import ttk, messagebox

class tabulador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("TABULADOR")
        self.crearTabs()

    def crearTabs(self):
        #Crear un tab control // clase notbook
        control_tabulador = ttk.Notebook(self)

        #agregamos un marco o frame para agregar detro del tab
        tabulador1 = ttk.Frame(control_tabulador)

        #Agregamos el tabulador
        control_tabulador.add(tabulador1,text="Tabulador1")
        #mostrar tab
        control_tabulador.pack(fill="both")
        #etiqueta
        etiqueta1 = ttk.Label(tabulador1,text="Nombre:")
        etiqueta1.grid(row=0,column=0,sticky=tk.E)
        #agregar elementos
        entrada1 = ttk.Entry(tabulador1, width=30)
        entrada1.grid(row=0,column=1,padx=5,pady=5)
        #boton
        def enviar():
            messagebox.showinfo("Mensaje",f'Nombre: {entrada1.get()}')

        boton1 = ttk.Button(tabulador1,text="Enviar",command=enviar)
        boton1.grid(row=1,column=0,columnspan=2)

        tabulador2 =ttk.LabelFrame(control_tabulador,text="Contenido")
        control_tabulador.add(tabulador2,text="Tabulador 2")


if __name__ == '__main__':
    ventana = tabulador()
    ventana.mainloop()