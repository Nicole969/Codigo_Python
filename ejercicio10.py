
#pintando las tetras de los botones 
from tkinter import*
import time 

def imprime():
    print("Acabas de presionar el boton imprimir ")

ventana =Tk()
ventana.title("SEGUNDA VENTANA EN TKINTER")
boton=Button(ventana,text="Salir",fg="red",command=ventana.quit)
boton.pack()
boton=Button(ventana,text="Imprimir",fg="Blue",command=imprime)
boton.pack()
ventana.mainloop()