from tkinter import*
ventana = Tk()
ventana.geometry("500x500")
ventana.title("Uso de imagenes")
#PNG y GIF
imagen = PhotoImage(file="d:\homero.png")
imgbtn = PhotoImage(file="d:\goku.png")
fondo = Label(ventana, image=imagen).place(x=0,y=0)
boton = Button(ventana, image=imgbtn).place(x=250,y=20)
ventana.mainloop()