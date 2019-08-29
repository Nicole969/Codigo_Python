
import datetime

def entrada(mensaje):
    print(mensaje)
    opcion()


def opcion() :
    print("Menu de asistencia")
    print("1.marca ingreas :")
    print("2.marca salida :")
    n=input("INGRESE UNA OPCION :")
    if n=="1":
        ingreso()
    

def ingreso():
    usuario=input("Marque su entrada con DNI :")
    if str(usuario)=="75405161":
        print("Marcaste tu entrada Nicole")
        a=datetime.datetime.now()
        print("fecha y hora de ingreso :",a)
        cont()
    else:
        print("USUARIO NO REGISTRADO")
    
def cont():
    m=input("Ingrese una opcion :")
    if m=="2" :
        usuario=input("marque su salida con DNI :")
        if str(usuario)=="75405161":
            print("Marcaste tu salida Nicole")
            a=datetime.datetime.now()
            b=datetime.datetime.now()
            print("fecha y hora de salid :",b)  
            delta=b-a
            print("ud.se quedo",delta,"s")  
        else:
            print("USUARIO NO REGISTRADO") 
        

entrada("BIENVENIDA")
    

