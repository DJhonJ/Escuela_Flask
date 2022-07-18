import imp
import data.database.curso_sql
from data.model import curso

def crear_curso(nombre):
    data.database.curso_sql.insert_curso(nombre)

#retona array de cursos
def consultar_curso(id = None):
    cursos_tupla = data.database.curso_sql.select_curso(id)
    cursos = []

    for item in cursos_tupla:
        cursos.append(curso.Curso(item[0], item[1], item[2], item[3], item[4]))

    return cursos