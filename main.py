"""Archivo principal de la aplicacion"""

from ast import parse
from logging import Logger
from math import log
import re
from flask import Flask, redirect, render_template, request, url_for

import formularios

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def operacion():
    """Funcion para realizar operaciones"""
    if request.method == "GET":
        return render_template("formulario.html")
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
        return render_template("formulario.html", resultado=resultado)


@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    """Funcion para calcular la distancia"""
    distancia_form = formularios.DistanciaForm(request.form)
    x1 = ""
    x2 = ""
    y1 = ""
    y2 = ""

    if request.method == "GET":
        return render_template("formula.html", form=distancia_form)
    if request.method == "POST":
        x1 = distancia_form.x1.data
        x2 = distancia_form.x2.data
        y1 = distancia_form.y1.data
        y2 = distancia_form.y2.data
        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
        return render_template("formula.html", form=distancia_form, distancia=distancia)


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
        return render_template("zodiaco.html", form=zodiaco_form)
    if request.method == "POST":

        # HOROSCOPO CHINO
        app.logger.debug("Año: %s", anio)
        
        if anio % 12 == 0:
            horoscopo_chino = "Mono"#
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
            horoscopo_chino = "Rata"#
            ruta = "rata.png"
        elif anio % 12 == 5:
            horoscopo_chino = "Buey"#
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
            horoscopo_chino = "Serpiente"#
            ruta = "serpiente.png"
        elif anio % 12 == 10:
            horoscopo_chino = "Caballo"#
            ruta = "caballo.png"
        elif anio % 12 == 11:
            horoscopo_chino = "Cabra"#
            ruta = "cabra.png"

        app.logger.debug("Horoscopo chino: %s", horoscopo_chino)
        app.logger.debug("Ruta: %s", ruta)
        return render_template(
            "respuesta_zodiaco.html",
            nombre=nombre,
            edad=edad,
            horoscopo_chino=horoscopo_chino,
            ruta=ruta
        )


if __name__ == "__main__":
    app.run(debug=True)
