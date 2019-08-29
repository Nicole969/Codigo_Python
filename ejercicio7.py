
#BOTON EVENTO QUE LO MINIMIZA DURANTE 3S Y LUEGO SE RESTABLECE
from tkinter import*
import time 

def parpadear():
    ventana.iconify()
    time.sleep(3)
    ventana.deiconify()

ventana =Tk()
boton=Button(ventana,text="EVENTO",command=parpadear)
boton.pack()
ventana.mainloop()