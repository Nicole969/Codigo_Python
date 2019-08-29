
#EJERCICIO 1 
from tkinter import*
def imprimE() :
    print("HOLA A TODOS")

ventana=Tk()
ventana.title("Ejercicio numero 1")
ventana.geometry("400x200")
etiqueta=Label(ventana,text="Desde aqui saludamos").place(x=10, y=10)
boton=Button(ventana,text="Dame clic para saludar",command=imprimE).place(x=200, y=10)
etiqueta2=Label(ventana,text="Desde aqui minimizamos").place(x=10, y=30)
boton=Button(ventana,text="Dame clic para minimizar",command=ventana.quit).place(x=200, y=30)
ventana.mainloop()

#en la hoja esta resuelto 