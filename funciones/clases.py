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
