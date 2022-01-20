from tkinter import ttk 
from tkinter import *


import sqlite3

class Patient:

    db_name = 'database.db'

    def __init__(self, window):
        self.wind = window
        self.wind.title('Registro de Pacientes')

        frame = LabelFrame(self.wind, text="Registre nuevo Paciente")
        frame.grid(row = 0, column = 0, columnspan = 5, pady = 20)

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
        self.area = Entry(frame)
        self.area.grid(row = 3, column = 1)

        # Price Input
        Label(frame, text='Precio: ').grid(row = 4, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 4, column = 1)
        
        # Button
        ttk.Button(frame, text='Guardar Paciente', command = self.add_patients).grid(row = 5, columnspan = 2, sticky = W + E)
        
        # Output Messages 
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 5, sticky = W + E)

        
        #table
        self.tree = ttk.Treeview(height = 10, columns=[f"#{n}" for n in range(0, 3)])
        self.tree.grid(row = 6, column = 0, columnspan = 4)
        self.tree.heading('#0', text = 'Nombre', anchor = CENTER)
        self.tree.heading('#1', text = 'Apellido', anchor = CENTER)
        self.tree.heading('#2', text = 'Area', anchor = CENTER)
        self.tree.heading('#3', text = 'Precio' , anchor= CENTER)

        ttk.Button(text = 'Eliminar', command = self.delete_patients).grid(row = 7, column= 0, sticky = W + E)
        ttk.Button(text = 'Editar', command= self.edit_patients).grid(row = 7,  column = 1, sticky = W + E)


        self.get_patients()


    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_name) as conn:
             cursor = conn.cursor()
             result = cursor.execute(query, parameters)
             conn.commit()
        return result

    def get_patients(self):

       records = self.tree.get_children()
       for element in records:
         self.tree.delete(element)

       query =  'SELECT * FROM patient ORDER BY name DESC'
       db_rows = self.run_query(query)
       for row in db_rows:
            self.tree.insert('', 0, text=row[1], values = (row[2], row[3], row[4]))
            
    def validation(self):
        return len(self.name.get())!=0 and len(self.lastname.get())!=0 and len(self.area.get())!=0 and len(self.price.get())!=0


    def add_patients(self):
        if self.validation():
            query = 'INSERT INTO patient VALUES(NULL, ?, ?, ?, ?)'
            parameters =  (self.name.get(), self.lastname.get(), self.area.get(), self.price.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Paciente Agregado Sastifactoriamente'
            self.name.delete(0, END)
            self.lastname.delete(0, END)
            self.area.delete(0, END)
            self.price.delete(0, END)
        else:
          self.message['text'] = 'Todos los datos son requeridos'
        self.get_patients()


    def delete_patients(self):
        self.message['text'] = ''
        try:
             self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Por favor selecciona un registro'
            return
        self.message['text'] = ''
        name = self.tree.item(self.tree.selection())['text']
        query = 'DELETE FROM patient WHERE name = ?'
        self.run_query(query, (name, ))
        self.message['text'] = 'Paciente Eliminado Sastifactoriamente'
        self.get_patients()


    def edit_patients(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Please, select Record'
            return
        name = self.tree.item(self.tree.selection())['text']
        old_lastname = self.tree.item(self.tree.selection())['values'][0]
        old_area = self.tree.item(self.tree.selection())['values'][1]
        old_price = self.tree.item(self.tree.selection())['values'][2]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Editar Paciente'

        Label(self.edit_wind, text = 'Antiguo Nombre:').grid(row = 0, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = name), state = 'readonly').grid(row = 0, column = 2)

        Label(self.edit_wind, text = 'Nuevo Nombre:').grid(row = 1, column = 1)
        new_name = Entry(self.edit_wind)
        new_name.grid(row = 1, column = 2)
        
        Label(self.edit_wind, text = 'Antiguo Apellido:').grid(row = 2, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_lastname), state = 'readonly').grid(row = 2, column = 2)

        Label(self.edit_wind, text = 'Nuevo Apellido:').grid(row = 3, column = 1)
        new_lastaname= Entry(self.edit_wind)
        new_lastaname.grid(row = 3, column = 2)

        Label(self.edit_wind, text = 'Antigua Area:').grid(row = 4, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_area), state = 'readonly').grid(row = 4, column = 2)

        Label(self.edit_wind, text = 'Nueva Area:').grid(row = 5, column = 1)
        new_area= Entry(self.edit_wind)
        new_area.grid(row = 5, column = 2)

        Label(self.edit_wind, text = 'Antiguo Precio:').grid(row = 6, column = 1)
        Entry(self.edit_wind, textvariable = StringVar(self.edit_wind, value = old_price), state = 'readonly').grid(row = 6, column = 2)

        Label(self.edit_wind, text = 'Nuevo Precio:').grid(row = 7, column = 1)
        new_price= Entry(self.edit_wind)
        new_price.grid(row = 7, column = 2)

        Button(self.edit_wind, text = 'Actualizar', command = lambda: self.edit_records(new_name.get(), name, new_lastaname.get(), old_lastname, new_area.get(), old_area, new_price.get(), old_price)).grid(row = 8, column = 2, pady=10, sticky = W)
        self.edit_wind.mainloop()


    def edit_records(self, new_name, name, new_lastaname, old_lastname, new_area, old_area, new_price, old_price):
        query = 'UPDATE patient SET name = ?, lastname = ?, area = ?, price = ? WHERE name = ? AND lastname = ? AND area = ? AND price = ?'
        parameters = (new_name, new_lastaname, new_area, new_price, name, old_lastname, old_area, old_price)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.message['text'] = 'Paciente Actualizado Sastifactoriamente'
        self.get_patients()





if __name__ == '__main__':
    window = Tk()
    application = Patient(window)
    window.mainloop()