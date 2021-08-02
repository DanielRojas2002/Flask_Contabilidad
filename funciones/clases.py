import matplotlib.pyplot as plt 
import sys
import datetime

class MetodoDelIngreso:
    def __init__ (self,II,IP,IN,D,BC,R,RT,INFE):
        self.__II=II
        self.__IP=IP
        self.__IN=IN
        self.__D=D
        self.__BC=BC
        self.__R=R
        self.__RT=RT
        self.__INFE=INFE

    def formulas(self):
        print("-"*40)
        print("IN=(Rt+R+In+Ip+Bc)")
        print("PIB=(IN+IIE+dep+INFE)")
        print("-"*40)
        
          
    
    def PIB(self):
        IN=(self.__RT+self.__R+self.__IN+self.__IP+self.__BC)
        pib=(IN+self.__II+self.__D+self.__INFE)
        lista=[IN,pib]

        return lista


class MetodoDelGasto():
    def __init__(self,ID,INFEE,E,D,IM,GG,GCF):
        self.__ID=ID
        self.__INFEE=INFEE
        self.__E=E
        self.__D=D
        self.__IM=IM
        self.__GG=GG
        self.__GCF=GCF
        
    
    def formulas(self):
        print("-"*40)
        print("Estas son las Formulas ")
        print("Xn=(E-I)")
        print("PIB=(C+I+G+Xn)")
        print("IN=(PIN-ingreso neto de los factores-impuestos indirectos)")
        print("-"*40)
    
    
    def PIB(self):
        XN=(self.__E-self.__IM)
        pib=(self.__GCF+self.__INFEE+self.__GG+XN)
        PIN=(pib-self.__D)
        IN=(PIN-self.__INFEE-self.__ID)
        lista=[pib,PIN,IN]
        return lista




class Equilibrio():
    def __init__(self,p,cv,cf):
        self.__p=p
        self.__cv=cv
        self.__cf=cf
        
    
    def proceso(self):
        lista=[]
        equilibrio=(self.__cf/(self.__p-self.__cv))
        #print(f"Estas son las unidades que tienes que vender para tener un Equilibrio (Ni ganancia , Ni perdida): {equilibrio} ")
        #print(separador)
        It=(equilibrio*self.__p)
        costoV=(equilibrio*self.__cv)
        margenC=(It-costoV)
        utilidad=(margenC-self.__cf)
        lista=[equilibrio,It,costoV,margenC,utilidad]
        # print(f"Ventas: {It}")
        #print(f"(-)Costo Variable : {costoV}")
        #print(f"(=)Margen de Contribucion : {margenC}")
        #print(f"(-)Costos Fijos : {self.__cf}")
        #print(f"Utilidad,Perdida o punto de equilibrio : {utilidad}")
        return lista

        
    def graficar(self,lista):
        equilibrio=lista[0]
        It=lista[1]
        costoV=lista[2]
        margenC=lista[3]
        utilidad=lista[4]
        '''
            x=[0,equilibrio]
            y=[0,It]
            plt.plot(x,y,"r")
            plt.plot(It,label=r"$IT$",color="r")
            x1=[0,equilibrio]
            y2=[self.__cf,It]
            plt.plot(x1,y2,"g")
            plt.plot(costoV,label=r"$CT$",color="g")
            plt.grid(True)

            plt.plot(self.__cf,label=r"$Costo Fijo$",color="k")
            plt.axhline(self.__cf,color="k",lw=2)
            
            plt.legend(loc=4)
            plt.xlabel("Unidades")
            plt.ylabel("$ DINERO")
            plt.title("Grafica de Punto de Equilibrio")
        
            
            plt.text(equilibrio,It,". Equilibrio",rotation=45)
            plt.show()
        '''




