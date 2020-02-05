#crear ventana
from tkinter import*

def clickedMusica():
    root.destroy()
    musica = Tk()
    musica.geometry('626x417')
    musica.title("RePOO")
    btnMusic = Button(root, text="musica", command=clickedMusic)
    btnMusic.place(x=50, y=200,height=50, width=100)
def clickedImagen():
    otra_ventana = Tkinter.Toplevel(root)
    root.iconify()
def clickedVideo():
    otra_ventana = Tkinter.Toplevel(root)
    root.iconify()

def ventana():
    root = Tk()
    root.geometry('626x417')
    root.title("RePOO")

    #añadir imagen
    #imagen1 = PhotoImage(file='fondoV2.gif')
    #label1 = Label(root, image=imagen1)
    #label1.pack(side='top', fill='both', expand='yes')
    #añadir texto
    text = Label(root,text = 'bienvenido a RePOO')
    text.place(x=100, y=100)
    text.config(font = ("Verdana", 30))
    #añadir botones
    btnMusica = Button(root, text="musica", command=clickedMusica)
    btnMusica.place(x=50, y=200,height=50, width=100)
    btnImagen = Button(root, text="Imagen", command=clickedImagen)
    btnImagen.place(x=250, y=200,height=50, width=100)
    btnVideo = Button(root, text="Videos", command=clickedVideo)
    btnVideo.place(x=450, y=200,height=50, width=100)
    root.mainloop()
