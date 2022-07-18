import imp
from flask import Flask, render_template, request, redirect, url_for
from controller import curso_controller

app = Flask(__name__)

#rutas html
@app.route('/')
@app.route('/login')
def index_template():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard_template():
    return render_template('dashboard.html')

@app.route('/curso')
def curso_template():
    cursos = curso_controller.consultar_curso()

    return render_template('curso.html', cursos=cursos)

@app.route('/curso/add/<id>')
@app.route('/curso/add')
def nuevo_curso_template(id=None):
    curso = None
    if id != None:
        cursos = curso_controller.consultar_curso(id)

        if len(cursos) > 0:
            curso = cursos[0]
        else:
            return redirect(url_for('curso_template'))

    return render_template('curso.html', accion='create', curso=curso)

@app.route('/estudiante')
def estudiante_template():
    return render_template('estudiante.html')


#rutas validaciones
@app.route('/iniciarSession', methods=['POST'])
def iniciar_session():
    usuario = request.form.get('usuario')

    if usuario == 'jhondoe':
        return redirect(url_for('dashboard_template'))
    
    return redirect(url_for('index_template', error='error'))

@app.route('/crearCurso', methods=['POST'])
def crear_curso():
    nombre = request.form.get('txtNombreCurso')

    curso_controller.crear_curso(nombre)

    return redirect(url_for('curso_template'))

@app.route('/curso/delete/<id>')
def eliminar_curso(id):
    curso_controller.eliminar_curso(id)
    return redirect(url_for('curso_template'))

# 0 = no existe. 1 = credenciales malas, NO SE ESTA USANDO
def mensaje_error(error):
    if (error != None and error != ''):
            mensajes = ['El usuario ingresado no existe.', 'Credenciales ingresada incorrectas.']
            error = int(error)

            return mensajes[error]

    return ''

#para identificar que el archivo principal es el main.py
if __name__ == '__main__':
    #debug=True, cuando haya un cambio el servidor se recarga y ejecuta automaticamente
    app.run(debug=True, port=5000)