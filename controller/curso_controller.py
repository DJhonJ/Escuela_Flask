import data.database.curso_sql
from data.model import curso
import re

#retorna True si el id es un numero y es mayor a cero
def validateId(id):
    if id != None and len(re.findall("\d", id)) > 0 and int(id) > 0:
        return True

    return False

def crear_curso(nombre):
    data.database.curso_sql.insert_curso(nombre)

#retona array de cursos
def consultar_curso(id = None):
    cursos = []
    
    if id != None and not validateId(id):
        return cursos

    cursos_tupla = data.database.curso_sql.select_curso(id)

    for item in cursos_tupla:
        cursos.append(curso.Curso(item[0], item[1], item[2], item[3], item[4]))

    return cursos

def eliminar_curso(id):
    if validateId(id):
        return data.database.curso_sql.delete_curso(id)

    return False
    