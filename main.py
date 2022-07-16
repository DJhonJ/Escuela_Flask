from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#ruta
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form.get('usuario')

    if usuario == 'jhondoe':
        return f"Hola {usuario}"
    
    return redirect(url_for('index', error='error'))

    

#para identificar que el archivo principal es el main.py
if __name__ == '__main__':
    #debug=True, cuando haya un cambio el servidor se recarga y ejecuta automaticamente
    app.run(debug=True, port=5000)