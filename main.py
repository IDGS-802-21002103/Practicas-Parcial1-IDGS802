'''Archivo principal de la aplicacion'''
from flask import Flask, render_template, request

import formula
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

@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    '''Funcion para calcular la distancia'''
    distancia_form = formula.DistanciaForm(request.form)
    x1 = ''
    x2 = ''
    y1 = ''
    y2 = ''

    if request.method == 'GET':
        return render_template("formula.html", form=distancia_form)
    if request.method == 'POST':
        x1 = distancia_form.x1.data
        x2 = distancia_form.x2.data
        y1 = distancia_form.y1.data
        y2 = distancia_form.y2.data
        distancia = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
        return render_template("formula.html", form=distancia_form, distancia=distancia)

if __name__ == '__main__':
    app.run(debug=True)
