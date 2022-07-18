import sqlite3
from sqlite3 import Error

class Conexion:
    def __init__(self):
        pass

    def create_connection(self):
        connection = None

        try:
            connection = sqlite3.connect('Escuela.db')
        except Error as e:
            raise Exception(str(e))
        #finally:
            #if (connection):
                #connection.close()

        return connection