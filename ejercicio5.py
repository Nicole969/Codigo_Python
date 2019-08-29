
#BOTON MINIMIZAAR
from tkinter import*
import time 

def parpadear():
    ventana.iconify()
    time.sleep(3)
    ventana.deiconify()

ventana =Tk()
boton=Button(ventana,text="MINIMIZAR",command=ventana.iconify)
boton.pack()
ventana.mainloop()

