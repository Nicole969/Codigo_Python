#boton de salida y impresion 

from tkinter import*
import time 

def imprime():
    print("Acabas de presionar el boton imprimir ")

ventana =Tk()
ventana.title("SEGUNDA VENTANA EN TKINTER")
boton=Button(ventana,text="Salir",command=ventana.quit)
boton.pack()
boton=Button(ventana,text="Imprimir",command=imprime)
boton.pack()
ventana.mainloop()