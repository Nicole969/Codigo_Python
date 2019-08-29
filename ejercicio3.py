import datetime
i=0
while i<=2 :
    print("           ASISTENCIA")
    print("::::::::::::::::::::::::::::::::")
    print("1.Ingreso")
    print("2.Salida")
    print("3.Reporte")
    opcion=input("Elija opcion :")
    if opcion=="1" :
        hi=input("Ingrese su DNI :")
        if hi=="75405161" :
            a=datetime.datetime.now()
            print("Su ingreso se registro")
        else :
            print("No tiene acceso")
    elif opcion=="2" :
        hi=input("Ingrese su DNI :")
        if hi=="75405161" :
            b=datetime.datetime.now()
            print=("Su salida se registro")
        else :
            print("Usuarior incorrecto")

    elif opcion=="3" :
        delta=b-a
        print("Usted a ingresado",delta.secons)            

        RESUELTO EN EL WHATSAPP