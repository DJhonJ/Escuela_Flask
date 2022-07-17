from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

#rutas html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/curso')
def curso():
    return render_template('curso.html')

@app.route('/curso/add')
def nuevoCurso():
    return render_template('curso.html', accion='create')

@app.route('/estudiante')
def estudiante():
    return render_template('estudiante.html')


#rutas validaciones
@app.route('/iniciarSession', methods=['POST'])
def iniciarSession():
    usuario = request.form.get('usuario')

    if usuario == 'jhondoe':
        return redirect(url_for('dashboard'))
    
    return redirect(url_for('index', error='error'))

@app.route('/crearCurso', methods=['POST'])
def crearCurso():
    pass

# 0 = no existe. 1 = credenciales malas
def mensajeError(error):
    if (error != None and error != ''):
            mensajes = ['El usuario ingresado no existe.', 'Credenciales ingresada incorrectas.']
            error = int(error)

            return mensajes[error]

    return ''

#para identificar que el archivo principal es el main.py
if __name__ == '__main__':
    #debug=True, cuando haya un cambio el servidor se recarga y ejecuta automaticamente
    app.run(debug=True, port=5000)