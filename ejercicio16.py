#VENTANA DONDE INGRESAS TUS NOMBRES Y ASI LOS UTILIZA PARA PERSONALIZAR TU SALUDO 
from tkinter import*
def saludar() :
    print("Hola :"+nombre.get()+" "+apellidoP.get()+" "+apellidoM.get())

ventana=Tk()
nombre=StringVar()
apellidoP=StringVar()
apellidoM=StringVar()
nombre.set("Escribe tu nombre")
ventana.title("Entradas en tkinter")
ventana.geometry("400x400")
etiqueta1=Label(ventana,text="Escribe tu nombre : ").place(x=10, y=10)
nombreCaja=Entry(ventana,textvariable=nombre).place(x=170, y=10)
etiqueta2=Label(ventana,text="Escribe tu apellido Paterno : ").place(x=10, y=40)
apellidoPCaja=Entry(ventana,textvariable=apellidoP).place(x=170 ,y=40)
etiqueta3=Label(ventana,text="Escribe tu apellido Materno : ").place(x=10, y=70)
apellidoMCaja=Entry(ventana,textvariable=apellidoM).place(x=170 ,y=70)
boton=Button(ventana,text="Saludo personalizado",command=saludar).place( x=10, y=100)
ventana.mainloop()
