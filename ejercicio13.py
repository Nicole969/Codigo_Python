
#posicion de los botones 
from tkinter import*

ventana=Tk()
ventana.title("Posicionamiento")
boton=Button(ventana,text="Posicionamiento diferente").place(x=10,y=10)
etiqueta=Label(ventana,text="Posicionamiento diferente").place(x=200,y=10)
etiqueta2=Label(ventana,text="Posicionamiento diferente 2").place(x=10,y=30)
etiqueta3=Label(ventana,text="Posicionamiento diferente 3").place(x=200,y=30)
ventana.mainloop()