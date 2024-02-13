from wtforms import Form, SelectField
from wtforms import StringField
from wtforms import IntegerField
from wtforms import RadioField


class DistanciaForm(Form):
    x1 = IntegerField("x1")
    x2 = IntegerField("x2")
    y1 = IntegerField("y1")
    y2 = IntegerField("y2")

class ZodiacoForm(Form):
    nombre = StringField("NOMBRE")
    apellido_paterno = StringField("APELLIDO PATERNO")
    apellido_materno = StringField("APELLIDO MATERNO")
    dia = IntegerField("Dia")
    mes = SelectField("Mes", choices=[('1', 'ENERO'), ('2', 'FEBRERO'), ('3', 'MARZO'), ('4', 'ABRIL'), ('5', 'MAYO'), ('6', 'JUNIO'), ('7', 'JULIO'), ('8', 'AGOSTO'), ('9', 'SEPTIEMBRE'), ('10', 'OCTUBRE'), ('11', 'NOVIEMBRE'), ('12', 'DICIEMBRE')])
    anio = IntegerField("Año")
    sexo = RadioField("Sexo", choices=[('M', 'MASCULINO'), ('F', 'FEMENINO')])
    
    

