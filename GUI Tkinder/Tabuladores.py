import tkinter as tk
from tkinter import ttk, messagebox,scrolledtext

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

        #Tabulador con scrolltext
        tabulador2 =ttk.LabelFrame(control_tabulador,text="scroll")
        control_tabulador.add(tabulador2,text="Tabulador 2")

        def crear_componentes_tabulador2(tabulador2):
            text = "Texto del scroll"
            #creacion del tabulador
            scroll = scrolledtext.ScrolledText(tabulador2,width=50,height=10,wrap=tk.WORD)
            scroll.insert(tk.INSERT,text)
            scroll.grid(row=0,column=0)
        crear_componentes_tabulador2(tabulador2)
        #datalist-combobox
        tabulador3 = ttk.LabelFrame(control_tabulador, text="combobox")
        control_tabulador.add(tabulador3, text="Tabulador 3")
        def crear_componentes_tabulador3(tabulador):
            datos = [x+1 for x in range(10)] #list comprenhension
            combobox = ttk.Combobox(tabulador,width=15,values=datos)
            combobox.grid(row=0,column=0,padx=10,pady=10)
            combobox.current(5-1)

        crear_componentes_tabulador3(tabulador3)
if __name__ == '__main__':
    ventana = tabulador()
    ventana.mainloop()