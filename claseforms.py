from flask_wtf import FlaskForm
from wtforms import StringField,TextField,PasswordField,SubmitField,IntegerField,DateTimeField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired,length
from wtforms import validators

#FORMS
#CLASE DEL LOGIN (INGRESAR CON EL USUARIO YA EXISTENTE)
class Login(FlaskForm):
    email = EmailField(
        'Correo electronico',
        [
            validators.InputRequired(message="El campo es requerido."),
            validators.Length(min=15, max=50, message='Ingrese un email válido.'),
            validators.DataRequired(message="El campo es requerido."),
            validators.Email(message="Ingrese un email válido.")
            #validators.regexp(regex=r'[a-z]+.[a-z]+@'+'uanl.edu.mx', message='El correo debe ser universitario.')
        ]
    )
    password = PasswordField(
        'Contraseña',
        [
            validators.InputRequired(message="La contraseña es requerida."),
            validators.Length(min=5, max=15, message='Ingrese un password de mínimo 8 caracteres maximo 15.'),
            validators.DataRequired(message="La contraseña es requerida."),
        ]
    )
    botonLog=SubmitField("INGRESAR")


#CLASE DEL LOGIN (CREAR USUARIO )
class Crear_Usuario(FlaskForm):
    email = EmailField(
        'Correo electronico',
        [
            validators.InputRequired(message="El campo es requerido."),
            validators.Length(min=15, max=50, message='Ingrese un email válido.'),
            validators.DataRequired(message="El campo es requerido."),
            validators.Email(message="Ingrese un email válido.")
            #validators.regexp(regex=r'[a-z]+.[a-z]+@'+'uanl.edu.mx', message='El correo debe ser universitario.')
        ]
    )
    password = PasswordField(
        'Contraseña',
        [
            validators.InputRequired(message="La contraseña es requerida."),
            validators.Length(min=5, max=15, message='Ingrese un password de mínimo 8 caracteres maximo 15.'),
            validators.DataRequired(message="La contraseña es requerida."),
        ]
    )
    botoncrearU=SubmitField("CREAR")
    botonatras=SubmitField("ATRAS")

# CLASE DEL PIB INGRESO
class PIB_ingreso(FlaskForm):
    id=IntegerField("ID")
    im_in=IntegerField("Impuestos Indirectos",validators=[DataRequired()])
    ig_p=IntegerField("Ingresos de los Propietarios",validators=[DataRequired()])
    intereses=IntegerField("Intereses",validators=[DataRequired()])
    dep=IntegerField("Depreciacion",validators=[DataRequired()])
    b_corp=IntegerField("Beneficios Corporativos",validators=[DataRequired()])
    renta=IntegerField("Renta",validators=[DataRequired()])
    r_trab=IntegerField("Renumeraciones de los Trabajadores",validators=[DataRequired()])
    in_fe=IntegerField("Ingreso Neto de los Factores Extranjeros",validators=[DataRequired()])

    botoncalcular=SubmitField("CALCULAR")

#CLASE DEL PIB GASTO
class PIB_gasto(FlaskForm):
    id=IntegerField("ID")
    II=IntegerField("Impuestos Indirectos",validators=[DataRequired()])
    INFEE=IntegerField("Ingreso neto de los factores extranjeros",validators=[DataRequired()])
    E=IntegerField("Exportaciones",validators=[DataRequired()])
    D=IntegerField("Depreciacion",validators=[DataRequired()])
    IM=IntegerField("Importaciones",validators=[DataRequired()])
    GG=IntegerField("Gasto de Gobierno",validators=[DataRequired()])
    GCF=IntegerField("Gasto de Consumo de Familias",validators=[DataRequired()])

    botoncalcular=SubmitField("CALCULAR")

class Utilidad(FlaskForm):
    P=IntegerField("Precio de Venta Unitario",validators=[DataRequired()])
    CV=IntegerField("Costo Variable por unidad",validators=[DataRequired()])
    CF=IntegerField("Costos Fijos Totales",validators=[DataRequired()])

    botoncalcular=SubmitField("CALCULAR")

