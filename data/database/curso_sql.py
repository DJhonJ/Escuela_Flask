from sqlite3 import connect
from data.database.conexion import Conexion
import datetime

try: 
    def insert_curso(nombre):
        conexion = Conexion().create_connection()
        cursor = conexion.cursor()
        
        valores = [
            (nombre, 1, datetime.datetime.today())
        ]
        
        cursor.executemany('insert into Curso (Nombre, Estado, FechaCreacion) values (?,?,?)', valores)

        conexion.commit() #confirma la transacion
        conexion.close()

        return True
        
    def update_curso():
        pass

    def delete_curso():
        pass

    def select_curso(id = None):
        conexion = Conexion().create_connection()
        cursor = conexion.cursor()

        if id != None:
            cursor.execute(f'select Id, Nombre, Estado, FechaCreacion, FechaModificacion from Curso where Id = {id}')
        else:
            cursor.execute('select Id, Nombre, Estado, FechaCreacion, FechaModificacion from Curso')
        
        cursos = cursor.fetchall()
        
        conexion.close()

        return cursos

except  Exception as e:
     raise e