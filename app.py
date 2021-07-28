from flask import Flask,request,render_template,flash,session
from flask import url_for,redirect
from flask_wtf import CSRFProtect
from config import Config
from claseforms import Login,Crear_Usuario,PIB_ingreso,PIB_gasto

from funciones.op_bd import CrearUsuario,Validar_Usuario,insertar_PIB_ingreso,obtener_datos_PIB_ingreso,insertar_PIB_gasto
from funciones.op_bd import obtener_datos_PIB_gasto,obtener_datos_por_id_ingreso,eliminar_registro_pib_ingreso

from funciones.clases import MetodoDelIngreso,MetodoDelGasto
import datetime


correo=""
po=""
lista=[]
valores=""
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


    return render_template("login.html",form=form,status=po)


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
    return render_template("Crear_cuenta.html",form=form,status=po) 


@app.route("/Menu_Principal")
def MENU():
    global lista
    lista=[]
    return render_template("menu.html")


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
    return render_template("PIB_ingreso.html",form=form ,calculo=lista , lista=valores)

@app.route("/obtener_valor_id_b/<int:id>", methods=["GET","POST"])
def obtenervalorborrar(id):
    form=PIB_ingreso(request.form) 
    if request.method=="POST":
        id=session["id"]=form.id.data
        print(id)
    datoaborrar=obtener_datos_por_id_ingreso(id)
    print(datoaborrar)
    eliminar_registro_pib_ingreso(datoaborrar[0]) # Aqui me quede 
    

    return redirect(url_for('PIB_INGRESO'))
   




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
            print(valores)
        except:
            pass
        
    return render_template("PIB_gasto.html",form=form ,calculo=lista , lista=valores)






if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=5000)