"""Archivo principal de la aplicacion"""

from flask import Flask, render_template, request
import formularios
from io import open

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/calculadora", methods=["GET", "POST"])
def operacion():
    """Funcion para realizar operaciones"""
    if request.method == "GET":
        return render_template("calculadora_form.html")
    if request.method == "POST":
        numero1 = int(request.form.get("numero1"))
        numero2 = int(request.form.get("numero2"))
        tipo = request.form.get("tipo")
        if tipo == "multiplicar":
            resultado = numero1 * numero2
        elif tipo == "dividir":
            resultado = numero1 / numero2
        elif tipo == "sumar":
            resultado = numero1 + numero2
        elif tipo == "restar":
            resultado = numero1 - numero2
        else:
            resultado = "Operación no válida"
        return render_template("calculadora_form.html", resultado=resultado)

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    """Funcion para calcular la distancia"""
    distancia_form = formularios.DistanciaForm(request.form)
    x1 = ""
    x2 = ""
    y1 = ""
    y2 = ""

    if request.method == "GET":
        return render_template("distancia_form.html", form=distancia_form)
    if request.method == "POST":
        x1 = distancia_form.x1.data
        x2 = distancia_form.x2.data
        y1 = distancia_form.y1.data
        y2 = distancia_form.y2.data
        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
        return render_template(
            "distancia_form.html", form=distancia_form, distancia=distancia
        )

@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    """Funcion para calcular el signo zodiacal"""
    zodiaco_form = formularios.ZodiacoForm(request.form)

    nombre = zodiaco_form.nombre.data
    anio = zodiaco_form.anio.data
    horoscopo_chino = ""
    ruta = ""

    if anio is not None:
        edad = 2024 - int(anio)
    else:
        edad = 0

    if request.method == "GET":
        return render_template("zodiaco_form.html", form=zodiaco_form)
    if request.method == "POST":

        horoscopo_chino, ruta = obtener_horoscopo(anio)
        return render_template(
            "zodiaco_resp.html",
            nombre=nombre,
            edad=edad,
            horoscopo_chino=horoscopo_chino,
            ruta=ruta,
        )

def obtener_horoscopo(anio):
    # HOROSCOPO CHINO
    app.logger.debug("Año: %s", anio)

    if anio % 12 == 0:
        horoscopo_chino = "Mono"
        ruta = "mono.png"
    elif anio % 12 == 1:
        horoscopo_chino = "Gallo"
        ruta = "gallo.png"
    elif anio % 12 == 2:
        horoscopo_chino = "Perro"
        ruta = "perro.png"
    elif anio % 12 == 3:
        horoscopo_chino = "Cerdo"
        ruta = "cerdo.png"
    elif anio % 12 == 4:
        horoscopo_chino = "Rata"  #
        ruta = "rata.png"
    elif anio % 12 == 5:
        horoscopo_chino = "Buey"  #
        ruta = "buey.png"
    elif anio % 12 == 6:
        horoscopo_chino = "Tigre"
        ruta = "tigre.png"
    elif anio % 12 == 7:
        horoscopo_chino = "Conejo"
        ruta = "conejo.jpg"
    elif anio % 12 == 8:
        horoscopo_chino = "Dragon"
        ruta = "dragon.png"
    elif anio % 12 == 9:
        horoscopo_chino = "Serpiente"  #
        ruta = "serpiente.png"
    elif anio % 12 == 10:
        horoscopo_chino = "Caballo"  #
        ruta = "caballo.png"
    elif anio % 12 == 11:
        horoscopo_chino = "Cabra"  #
        ruta = "cabra.png"

    app.logger.debug("Horoscopo chino: %s", horoscopo_chino)
    app.logger.debug("Ruta: %s", ruta)

    return horoscopo_chino, ruta

@app.route("/diccionario", methods=["GET", "POST"])
def diccionario():
    """Funcion para buscar palabras en un diccionario"""
    diccionario_form = formularios.DiccionarioForm(request.form)
    busqueda_palabra_form = formularios.BusquedaPalabraForm(request.form)
    ingles = diccionario_form.ingles.data 
    espanol = diccionario_form.espanol.data
    seleccion = busqueda_palabra_form.seleccion.data
    palabra = busqueda_palabra_form.palabra.data

    if diccionario_form.validate() and request.method == "POST":
        print("INGLES: ", ingles,"ESPAÑOL: ", espanol)
        guardar_traduccion(ingles, espanol)

        return render_template(
            "diccionario.html",
            diccionario_form=diccionario_form,
            busqueda_palabra_form=busqueda_palabra_form,
            ingles="",
            espanol="",
        )

    if busqueda_palabra_form.validate() and request.method == "POST":

        print("PALABRA: ", palabra)    
        if palabra != "" and palabra is not None:
            palabra = buscar_palabra(palabra, seleccion)

        return render_template(
            "diccionario.html",
            busqueda_palabra_form=busqueda_palabra_form,
            diccionario_form=diccionario_form,
            seleccion=seleccion,
            palabra=palabra,
        )

    return render_template('diccionario.html', diccionario_form=diccionario_form, busqueda_palabra_form=busqueda_palabra_form)

def guardar_traduccion(ingles, espanol):
    with open("diccionario.txt", "a") as archivo:
        archivo.write(ingles.upper() + ":" + espanol.upper() + "\n")

def buscar_palabra(palabra, seleccion):
    with open("diccionario.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            print("LINEA: ", linea)
            if seleccion == "1":
                print("SELECCION: ", seleccion)
                if palabra.upper() in linea.split(":")[1]:
                    return linea.split(":")[0].strip()
            else:
                print("SELECCION: ", seleccion)
                if palabra.upper() in linea.split(":")[0]:
                    return linea.split(":")[1].strip()
    return "Palabra no encontrada".upper()

if __name__ == "__main__":
    app.run(debug=True)
