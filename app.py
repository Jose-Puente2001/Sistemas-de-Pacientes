from tkinter import ttk 
from tkinter import *


import sqlite3

class Patient:

    def __init__(self, window):
        self.wind = window
        self.wind.title('Registro de Pacientes')

        frame = LabelFrame(self.wind, text="Registre nuevo Paciente")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Name Input
        Label(frame, text='Nombre: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        #lastname Input
        Label(frame, text='Apellido: ').grid(row = 2, column= 0)
        self.lastname = Entry(frame)
        self.lastname.grid(row = 2, column = 1)

        #area Input
        Label(frame, text='Area donde se dirige: ').grid(row = 3, column= 0)
        self.lastname = Entry(frame)
        self.lastname.grid(row = 3, column = 1)

        # Price Input
        Label(frame, text='Precio: ').grid(row = 4, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 4, column = 1)
        
        # Button
        ttk.Button(frame, text='Guardar Paciente').grid(row = 5, columnspan = 2, sticky = W + E)
        
        #table
        self.tree = ttk.Treeview(height = 15, columns=[f"#{n}" for n in range(0, 3)])
        self.tree.grid(row = 6, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#1', text = 'Apellido', anchor = CENTER)
        self.tree.heading('#2', text = 'Area', anchor = CENTER)
        self.tree.heading('#3', text = 'Precio' , anchor= CENTER)

if __name__ == '__main__':
    window = Tk()
    application = Patient(window)
    window.mainloop()