from .conexion import  conexionbd
import datetime

# PIBS
def insertar_PIB_ingreso(impuesto_indirectos, ingresos_propietarios,intereses,depreciacion,beneficios_corporativos,renta,renumeraciones,ingreso_neto,tiempo_Creacion,re_ingreso_nacional,re_PIB ,email):
    conexion = conexionbd()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO PIB_ingreso(impuestos_in,ingresos_P,intereses,depreciacion ,beneficios_corp,renta,renumeraciones,ingreso_neto,tiempo_C,re_ingreso_nacional,re_PIB,correo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (impuesto_indirectos, ingresos_propietarios,intereses,depreciacion,beneficios_corporativos,renta,renumeraciones,ingreso_neto,tiempo_Creacion,re_ingreso_nacional,re_PIB,email))
    conexion.commit()
    conexion.close()

def insertar_PIB_gasto(impuestos_indirectos,ingresos_neto,exportaciones,depreciacion,importaciones,gasto_gobierno,consumo_familias,tiempo_Creacion,re_pib,re_pin,re_in ,email):
    conexion = conexionbd()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO PIB_gasto(impuestos_in,ingresos_neto,exportaciones,depreciacion,importaciones ,gasto_gobierno ,consumo_familias,tiempo_C ,r_pib,r_pin,r_ingreso_nacional,correo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (impuestos_indirectos,ingresos_neto,exportaciones,depreciacion,importaciones,gasto_gobierno,consumo_familias,tiempo_Creacion,re_pib,re_pin,re_in,email))
    conexion.commit()
    conexion.close()

def obtener_datos_PIB_ingreso(correo):
    conexion = conexionbd()
    productos = []
    listaProductos2=[]
    with conexion.cursor() as cursor:
        
        cursor.execute("SELECT id,impuestos_in,ingresos_P,intereses,depreciacion ,beneficios_corp,renta,renumeraciones,ingreso_neto,tiempo_C,re_ingreso_nacional,re_PIB FROM PIB_ingreso WHERE correo = %s", (correo,))
        productos = cursor.fetchall()

        for id,im_i,ip,i,d,dc,r,rr,i_n,tc,rin,pib in productos:
            tupla=(id,im_i,ip,i,d,dc,r,rr,i_n,tc,rin,pib)
            listaProductos2.append(tupla)

    conexion.close()
    return listaProductos2

def obtener_datos_PIB_gasto(correo):
    conexion = conexionbd()
    productos = []
    listaProductos2=[]
    with conexion.cursor() as cursor:
        
        cursor.execute("SELECT id,impuestos_in,ingresos_neto,exportaciones,depreciacion,importaciones ,gasto_gobierno ,consumo_familias ,r_pib,r_pin,r_ingreso_nacional FROM PIB_gasto WHERE correo = %s", (correo,))
        productos = cursor.fetchall()

        for id,i_i,i_n,e,d,i,gg,cf,rp,rpin,ri in productos:
            tupla=(id,i_i,i_n,e,d,i,gg,cf,rp,rpin,ri)
            listaProductos2.append(tupla)

    conexion.close()
    return listaProductos2



def eliminar_registro_pib_ingreso(id):
    conexion = conexionbd()
    with conexion.cursor() as cursor:
        cursor.execute(f"DELETE FROM PIB_ingreso WHERE id = {id}")
    conexion.commit()
    conexion.close()

def eliminar_registro_pib_gasto(id):
    conexion = conexionbd()
    with conexion.cursor() as cursor:
        cursor.execute(f"DELETE FROM PIB_gasto WHERE id = {id}")
    conexion.commit()
    conexion.close()

# FIN PIBS
#Utilidad
def insertar_Utilidad(precio_venta,costo_variable,costo_fijo,r_venta,r_costo_variable,r_margen,r_costo_fijos,r_utilidad,correo):
    conexion = conexionbd()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO Utilidad(precio_venta,costo_variable,costo_fijo,r_venta,r_costo_variable,r_margen,r_costo_fijos,r_utilidad,correo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (precio_venta,costo_variable,costo_fijo,r_venta,r_costo_variable,r_margen,r_costo_fijos,r_utilidad,correo))
    conexion.commit()
    conexion.close()


def obtener_datos_Utilidad(correo):
    conexion = conexionbd()
    productos = []
    listaProductos2=[]
    with conexion.cursor() as cursor:
        
        cursor.execute("SELECT id,precio_venta,costo_variable,costo_fijo,r_venta,r_costo_variable,r_margen,r_costo_fijos,r_utilidad FROM Utilidad WHERE correo = %s", (correo,))
        productos = cursor.fetchall()

        for id,p,cv,cf,rv,rc,rm,rcf,ru in productos:
            tupla=(id,p,cv,cf,rv,rc,rm,rcf,ru)
            listaProductos2.append(tupla)

    conexion.close()
    return listaProductos2

def eliminar_registro_utilidad(id):
    conexion = conexionbd()
    with conexion.cursor() as cursor:
        cursor.execute(f"DELETE FROM Utilidad WHERE id = {id}")
    conexion.commit()
    conexion.close()
# Fin Utilidad


def CrearUsuario(correo,contraseña):
    conexion = conexionbd()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO Login(CORREO,CONTRASEÑA) VALUES (%s, %s)",
                       (correo,contraseña))
    conexion.commit()
    conexion.close()


def Validar_Usuario(correo,contra):
    conexion = conexionbd()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM Login WHERE CORREO = %s AND CONTRASEÑA = %s", (correo,contra))
        datos = cursor.fetchall()    
    conexion.close()
    return datos

    




