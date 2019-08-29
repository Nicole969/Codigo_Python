#SEÑALA VALORES 
from tkinter import*
def obtener():
    print(valor.get())

ventana=Tk()
valor=StringVar()
ventana.title("Uso de Spinbox con Tkinter")
ventana.geometry("400x300")
etiqueta=Label(ventana,text="Ejemplo 1 de Spinbox").place(x=20,y=20)
combo=Spinbox(ventana,values=("Uno","Dos","Tres","Cuatro","Cinco")).place(x=20,y=50)
etiqueta2=Label(ventana,text="Ejemplo 2 de Spinbox").place(x=20,y=80)
combo2=Spinbox(ventana,from_=1,to=10,textvariable=valor).place(x=20,y=140)
boton=Button(ventana,text="Obtener valor Spinbox",command=obtener).place(x=80,y=140)
mainloop()