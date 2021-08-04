from flask import Flask,request,render_template,flash,session
from flask import url_for,redirect
from flask_wtf import CSRFProtect
from flask import Response
from config import Config

#PIBS
# IMPORTACION DE FORMS (usuario)
from claseforms import Login,Crear_Usuario

# IMPORTACION DE FORMS DE PIBS
from claseforms import PIB_ingreso,PIB_gasto

# IMPORTACIONES DE LA CONEXION CON LA BASE DE DATOS

        # IMPORTACION DE FUNCIONES DE USUARIO
from funciones.op_bd import CrearUsuario,Validar_Usuario

        # IMPORTACION DE FUNCIONES DE PIBS 
from funciones.op_bd import insertar_PIB_ingreso,obtener_datos_PIB_ingreso
from funciones.op_bd import insertar_PIB_gasto,obtener_datos_PIB_gasto
from funciones.op_bd import eliminar_registro_pib_ingreso,eliminar_registro_pib_gasto

    # IMPORTACION DE CLASES DE PIBS PARA CALCULAR EL PIB DE LOS DOS METODOS
from funciones.clases import MetodoDelIngreso,MetodoDelGasto

#UTILIDAD
#IMPORTACION DE FORM Utilidad
from claseforms import Utilidad
#IMPORTACION DE FUNCIONES DE UTILIDAD
from funciones.op_bd import obtener_datos_Utilidad,insertar_Utilidad,eliminar_registro_utilidad
#IMPORTACION DE CLASE DE UTILIDAD PARA CALCULAR LA UTILIDAD 
from funciones.clases import Equilibrio

import datetime

# decodigo.com
import os


# variables globales 
correo=""
po=""
lista=[]
lista2=[]
valores=""
grafica=""
app=Flask(__name__,template_folder="Templates")

app.config.from_object(Config)

csrf=CSRFProtect()

@app.route("/",methods=["GET", "POST"]) 
def login():
    form=Login(request.form)
    if request.method=="POST" and form.validate_on_submit():
        email=session["email"]=form.email.data
        contraseña=session["password"]=form.password.data

        global correo
        correo=""
        global po
        po=""
        contador=0
        
        valido=Validar_Usuario(email,contraseña)

        for elemento in valido:
            for x in elemento:
                contador+=1

        if contador==2:
            correo=email
            return redirect(url_for('MENU'))
        else:
            po="NO"
            message=("NO COINCIDE EL CORREO CON ESA CONTRASEÑA")
            flash(message)


    return render_template("usuario/login.html",form=form,status=po)

# CREAR USUARIO 
@app.route("/Crear_Cuenta",methods=["GET","POST"])
def create():
    form=Crear_Usuario(request.form) 
    if request.method=="POST" and form.validate_on_submit():
        email=session["email"]=form.email.data
        contraseña=session["password"]=form.password.data
        global po
        po=""

        try:
            message=('USUARIO DADO DE ALTA')
            CrearUsuario(email,contraseña)
            po="SI"
        except:
            po="NO"
            message=("Ya fue dado de alta el Correo")

        finally:
            flash(message)
    return render_template("usuario/Crear_cuenta.html",form=form,status=po) 

# MENU PRINCIPAL
@app.route("/Menu_Principal")
def MENU():
    global correo
    global lista
    lista=[]
    # Se define el nombre de la carpeta o directorio a crear
    directorio = "static/graficas/"+correo
    try:
        os.mkdir(directorio)
    except OSError:
        pass
    
    return render_template("index.html")

# PIB POR EL METODO DEL INGRESO
@app.route("/PIB_INGRESO", methods=["GET", "POST"])
def PIB_INGRESO():
    global correo
    global valores
    email=correo
    form=PIB_ingreso(request.form)
    valores=obtener_datos_PIB_ingreso(email)
    if request.method=="POST" and form.validate_on_submit():
       
        impuestos_indirectos=session["im_in"]=form.im_in.data
        ingresos_propietarios=session["ig_p"]=form.ig_p.data
        intereses=session["intereses"]=form.intereses.data
        depreciacion=session["depreciacion"]=form.dep.data
        beneficios_corporativos=session["b_corp"]=form.b_corp.data
        renta=session["renta"]=form.renta.data
        renumeraciones=session["r_trab"]=form.r_trab.data
        ingreso_neto=session["in_fe"]=form.in_fe.data
        tiempo_C=datetime.datetime.now()
        email=correo
        global lista
        lista=[]
        
        try:
            calculo=MetodoDelIngreso(impuestos_indirectos,ingresos_propietarios,intereses,depreciacion,beneficios_corporativos,renta,renumeraciones,ingreso_neto).PIB()
            lista=[calculo]
            ingreso_nacional=calculo[0]
            pib=calculo[1]
            
            insertar_PIB_ingreso(impuestos_indirectos,ingresos_propietarios,intereses,depreciacion,beneficios_corporativos,renta,renumeraciones,ingreso_neto,tiempo_C,ingreso_nacional,pib,email)
            valores=obtener_datos_PIB_ingreso(email)
        except:
            pass
    return render_template("procesos/PIB_ingreso.html",form=form ,calculo=lista , lista=valores)


# ELIMINACION  POR ID DEL METODO DEL INGRESO
@app.route("/obtener_valor_id_b/<int:id>", methods=["GET","POST"])
def obtenervalorborrarI(id):
    eliminar_registro_pib_ingreso(id) 
    
    return redirect(url_for('PIB_INGRESO'))

# PIB POR EL METODO DEL GASTO 
@app.route("/PIB_GASTO",methods=["GET","POST"])
def PIB_GASTO():
    global correo
    global valores
    email=correo
    form=PIB_gasto(request.form)
    valores=obtener_datos_PIB_gasto(email)
    if request.method=="POST" and form.validate_on_submit():
       
        impuestos_indirectos=session["II"]=form.II.data
        ingresos_neto=session["INFEE"]=form.INFEE.data
        exportaciones=session["E"]=form.E.data
        depreciacion=session["D"]=form.D.data
        importaciones=session["IM"]=form.IM.data
        gasto_gobierno=session["GG"]=form.GG.data
        consumo_familias=session["GCF"]=form.GCF.data
        tiempo_C=datetime.datetime.now()
        email=correo
        global lista
        lista=[]
        
        try:
            calculo=MetodoDelGasto(impuestos_indirectos,ingresos_neto,exportaciones,depreciacion,importaciones,gasto_gobierno,consumo_familias).PIB()
            lista=[calculo]
            pib=calculo[0]
            pin=calculo[1]
            INE=calculo[2]
            
            insertar_PIB_gasto(impuestos_indirectos,ingresos_neto,exportaciones,depreciacion,importaciones,gasto_gobierno,consumo_familias,tiempo_C,pib,pin,INE,email)
            valores=obtener_datos_PIB_gasto(email)
            
        except:
            pass
        
    return render_template("procesos/PIB_gasto.html",form=form ,calculo=lista , lista=valores)


# ELIMINACION POR ID DEL METODO DEL GASTO 
@app.route("/obtener_valor_id_bo/<int:id>", methods=["GET","POST"])
def obtenervalorborrarG(id):
    eliminar_registro_pib_gasto(id) 
    
    return redirect(url_for('PIB_GASTO'))


@app.route("/Utilidad", methods=["GET","POST"])
def UTILIDAD():
    global correo
    global valores
    email=correo
    global lista
    global lista2
    lista2=[]
    global grafica
    grafica=""
    lista=[]
    form=Utilidad(request.form)
    valores=obtener_datos_Utilidad(email)
    if request.method=="POST" and form.validate_on_submit():
        precio_venta =session["P"]=form.P.data
        costo_variable=session["CV"]=form.CV.data
        costo_fijo=session["CF"]=form.CF.data
        tiempo_C=datetime.datetime.now()

        
        calculo=Equilibrio(precio_venta,costo_variable,costo_fijo).proceso()
        
        lista=calculo
        lista2=[calculo]
        r_equilibrio =calculo[0]
        r_venta=calculo[1]
        r_costo_variable=calculo[2]
        r_margen=calculo[3]
        r_utilidad=calculo[4]

        insertar_Utilidad(precio_venta,costo_variable,costo_fijo,r_equilibrio,r_venta,r_costo_variable,r_margen,r_utilidad,tiempo_C,email)
        valores=obtener_datos_Utilidad(email)

    return render_template("procesos/Utilidad.html",form=form ,calculo=lista2 , lista=valores )


@app.route("/ver_grafica/<lista>", methods=["GET","POST"])
def graficas(lista):
    print(lista)
    global correo
    email=correo


    grafica=Equilibrio().graficar(lista,email)
    

    return redirect(url_for('UTILIDAD')) 



@app.route("/obtener_valor_id_bor/<int:id>", methods=["GET","POST"])
def obtenervalorborrarU(id):
    eliminar_registro_utilidad(id) 
    
    return redirect(url_for('UTILIDAD'))    



#INICIALIZACION DE LA APLICACION
if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=5000)