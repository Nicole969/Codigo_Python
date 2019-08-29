#AGREGANDO UN TITULO

from tkinter import*
import time 

def parpadear():
    ventana.iconify()
    time.sleep(3)
    ventana.deiconify()

ventana =Tk()
ventana.title("PRIMERA VENTANA EN TKINTER")
boton=Button(ventana,text="EVENTO",command=parpadear)
boton.pack()
ventana.mainloop()