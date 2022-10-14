import tkinter as tk


class Calculadora(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid()
        self.crearElementos()

    @staticmethod
    def botonClic():
        print("Presionado")


    def crearElementos(self):
        contador = 0
        B = []  # Declaramos la matriz [Lista]
        for i in range(6):
            B.append([])  # Agregamos la columna
            for j in range(6):
                self.etiqueta1 = tk.Label(self,text="Hola").grid(column=0,row=0,sticky="NSWE")
                self.boton1 = tk.Button(self, text=f'Boton {contador}', command=self.botonClic)
                self.boton1.grid(row=i+1, column=j, sticky="NWSE")
                B[i].append(self.boton1)
                contador+=1



        #self.boton1 = tk.Button(self,text="Boton 1",command= self.botonClic)
        #self.boton1.grid(row=2, column=0, sticky="W")
        #self.boton2 = tk.Button(self, text="Boton 2", command=self.botonClic)
        #self.boton2.grid(row=3, column=0, sticky="W")



Calculator = tk.Tk()
Calculator.title("Calculadora")
Calculator.geometry("600x400")
Calculator.config(cursor="pencil")
Calculator.rowconfigure(0,weight=1)
Calculator.rowconfigure(1,weight=2)
app = Calculadora(Calculator)
app.grid()

app.mainloop()
