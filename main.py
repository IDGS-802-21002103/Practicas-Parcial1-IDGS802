'''Archivo principal de la aplicacion'''
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def operacion():
    '''Funcion para realizar operaciones'''
    if request.method == 'GET':
        return render_template('formulario.html')
    if request.method == 'POST':
        numero1 = int(request.form.get('numero1'))
        numero2 = int(request.form.get('numero2'))
        tipo = request.form.get('tipo')
        if tipo == 'multiplicar':
            resultado = numero1 * numero2
        elif tipo == 'dividir':
            resultado = numero1 / numero2
        elif tipo == 'sumar':
            resultado = numero1 + numero2
        elif tipo == 'restar':
            resultado = numero1 - numero2
        else:
            resultado = 'Operación no válida'
        return render_template("formulario.html", resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
