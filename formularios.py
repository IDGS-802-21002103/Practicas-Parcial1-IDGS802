from wtforms import Form, SelectField
from wtforms import StringField
from wtforms import IntegerField
from wtforms import RadioField
from wtforms import validators

MESSAGE_REQUIRED = "El campo es requerido"
MESSAGE_LENGTH = "Ingrese una palabra valida"

class DistanciaForm(Form):
    x1 = IntegerField("X1")
    x2 = IntegerField("X2")
    y1 = IntegerField("Y1")
    y2 = IntegerField("Y2")


class ZodiacoForm(Form):
    nombre = StringField("NOMBRE")
    apellido_paterno = StringField("APELLIDO PATERNO")
    apellido_materno = StringField("APELLIDO MATERNO")
    dia = IntegerField("Dia")
    mes = SelectField(
        "Mes",
        choices=[
            ("1", "ENERO"),
            ("2", "FEBRERO"),
            ("3", "MARZO"),
            ("4", "ABRIL"),
            ("5", "MAYO"),
            ("6", "JUNIO"),
            ("7", "JULIO"),
            ("8", "AGOSTO"),
            ("9", "SEPTIEMBRE"),
            ("10", "OCTUBRE"),
            ("11", "NOVIEMBRE"),
            ("12", "DICIEMBRE"),
        ],
    )
    anio = IntegerField("Año")
    sexo = RadioField("Sexo", choices=[("M", "MASCULINO"), ("F", "FEMENINO")])

class DiccionarioForm(Form):
    ingles = StringField("INGLES", [validators.DataRequired(message=MESSAGE_REQUIRED), validators.length(min=1, message=MESSAGE_LENGTH)])
    espanol = StringField("ESPAÑOL", [validators.DataRequired(message=MESSAGE_REQUIRED), validators.length(min=1, message=MESSAGE_LENGTH)])

class BusquedaPalabraForm(Form):
    seleccion = RadioField("Seleccion", choices=[("1", "INGLES"), ("2", "ESPAÑOL")], default="1")
    palabra = StringField("PALABRA", [validators.DataRequired(message=MESSAGE_REQUIRED), validators.length(min=1, message=MESSAGE_LENGTH)])
