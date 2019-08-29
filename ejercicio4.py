#primera parte
from tkinter import*
ventana=Tk()
etiqueta=Label(ventana,text="HOLA A TODOS")
etiqueta.pack()
etiqueta.mainloop()
#segunda parte
ventana=Tk()
ventana.title("Esta es mi primera ventana")
#llamamos denuevo a la ventana y le damos un titulo
boton=Button(ventana,text="MINIMIZAR",command=ventana.iconify)
boton.pack()
