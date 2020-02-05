#crear ventana
from tkinter import*
import random
import operator
import os
#instalar libreria pygame e importarla
#importar random
#importar operator

#crear listas
i = 0
opcion = 0
lista_canciones = []
lista_imagenes = []
lista_videos = []
listas_canciones = []
albumes_imagenes = []
albumes_videos = []
#crear ventana
from tkinter import*

def ventanaMusica():
    root = Tk()
    root.geometry('626x417')
    root.title("RePOO")
    def clickedMusic():
        root.destroy()
        menuPrincipal = ventana()
    
    btnMusic = Button(root, text="musica", command=clickedMusic)
    btnMusic.place(x=50, y=200,height=50, width=100)
    root.mainloop()

def ventana():
    root = Tk()
    root.geometry('626x417')
    root.title("RePOO")
    def clickedMusica():
        
        root.destroy()
        musicaMM = ventanaMusica()
    def clickedImagen():
        otra_ventana = Tkinter.Toplevel(root)
        root.iconify()
    def clickedVideo():
        otra_ventana = Tkinter.Toplevel(root)
        root.iconify()
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

class multimedia:
    def __init__ (self,nombre,album, interprete, año):
        self.nombre = nombre
        self.album = album
        self.interprete = interprete
        self.año = año

    def get_nombre(self):
        return self.nombre

    def get_album(self):
        return self.album

    def get_interprete(self):
        return self.interprete

    def get_año(self):
        return self.año

class cancion(multimedia):
    def __init__ (self,nombre, interprete, album,  año, genero):
        self.nombre = nombre
        self.album = album
        self.interprete = interprete
        self.año = año
        self.genero = genero

    def get_genero(self):
        return self.genero

class imagen(multimedia):
    pass

class video(multimedia):
    pass

#verificar que el numero igresado desde menu sea una funcion valida
class numero:
    def clr(self):
        os.system('cls')
    def __init__(self,numero):
        self.i = numero

    def numopc(self):
        correcto = False
        num = 0
        while (not correcto):
            try:
                num = int(input("\n"))
                correcto = True
            except ValueError:
                print("Porfavor ingrese un numero valido")
        if num <= self.i:
            return num
        else:
            print("Porfavor ingrese un numero valido")
            return self.numopc()





class menus:

    def __init__(self):
        pass

    # menu para ver y agregar musica
    def menumusic(self):
        print("1. Agregar musica")
        print("2. Crear listas de musica ")
        print("3. Ver listas de musica")
        print("4. Ver toda la musica")
        print("5. Volver al menu")
        numeroV = numero(5)
        opcion = numeroV.numopc()

        if opcion == 1:
            ingreso = ingresar()
            ingreso.ingresar_cancion()
        elif opcion == 2:
            crearLista = crear_listas("cancion", lista_canciones)
            crearLista.crear_lista()
        elif opcion == 3:
            lista = ver_listas("cancion", listas_canciones)
            lista.ver_lista()
        elif opcion == 4:
            self.menumusicb()
        elif opcion == 5:
            salir = True

    # menu toda la musica organizada por atributos
    def menumusicb(self):
        print("1. Ver por autor")
        print("2. Ver alfabeticamente")
        print("3. Ver por album")
        print("4. Ver por año")
        print("5. Ver por genero")
        print("6. Volver al menu")
        print("7. Volver a Musica")
        numeroV = numero(7)
        opcion = numeroV.numopc()

        if opcion == 1:
            vista = ver_por_autor(lista_canciones)
            vista.ver_por_autor()
        elif opcion == 2:
            vista = ver_alfabeticamente(lista_canciones)
            vista.ver_alfabeticamente()
        elif opcion == 3:
            vista = ver_por_album(lista_canciones)
            vista.ver_por_album()
        elif opcion == 4:
            vista = ver_por_año(lista_canciones)
            vista.ver_por_año()
        elif opcion == 5:
            vista = ver_por_genero(lista_canciones)
            vista.ver_por_genero()
        elif opcion == 6:
            salir = True
        elif opcion == 7:
            self.menumusic()

    #menu para ver y agregar videos
    def menuvid(self):
        print("1. Agregar videos")
        print("2. Crear album de videos")
        print("3. Ver album de videos")
        print("4. Ver todos los videos")
        print("5. Volver al menu")
        numeroV = numero(5)
        opcion = numeroV.numopc()

        if opcion == 1:
            ingreso = ingresar()
            ingreso.ingresar_video()
        elif opcion == 2:
            crearLista = crear_listas("video", lista_videos)
            crearLista.crear_lista()
        elif opcion == 3:
            lista = ver_listas("video", albumes_videos)
            lista.ver_lista()
        elif opcion == 4:
            self.menuvideob()
        elif opcion == 5:
            salir = True

    #menu todos los videos organizado por atributos
    def menuvideob(self):
        print("1. Ver por autor")
        print("2. Ver alfabeticamente")
        print("3. Ver por album")
        print("4. Ver por año")
        print("5. Volver al menu")
        print("6. Volver a video")
        numeroV = numero(6)
        opcion = numeroV.numopc()

        if opcion == 1:
            vista = ver_por_autor(lista_videos)
            vista.ver_por_autor()
        elif opcion == 2:
            vista = ver_alfabeticamente(lista_videos)
            vista.ver_alfabeticamente()
        elif opcion == 3:
            vista = ver_por_album(lista_videos)
            vista.ver_por_album()
        elif opcion == 4:
            vista = ver_por_año(lista_videos)
            vista.ver_por_año()
        elif opcion == 5:
            salir = True
        elif opcion == 6:
            self.menuvid()

    #menu para ver y agregar imagenes
    def menuimag(self):
        print("1. Agregar imagenes")
        print("2. Crear album de imagenes ")
        print("3. Ver album de imagenes")
        print("4. Ver todas las imagenes")
        print("5. Volver al menu")
        numeroV = numero(5)
        opcion = numeroV.numopc()

        if opcion == 1:
            ingreso = ingresar()
            ingreso.ingresar_imagen()
        elif opcion == 2:
            crearLista = crear_listas("imagen", lista_imagenes)
            crearLista.crear_lista()
        elif opcion == 3:
            lista = ver_listas("imagen", albumes_imagenes)
            lista.ver_lista()
        elif opcion == 4:
            self.menuimagenb()
        elif opcion == 5:
            salir = True

    #menu todas las imagenes organizadas por atributos
    def menuimagenb(self):

        print("1. Ver por autor")
        print("2. Ver alfabeticamente")
        print("3. Ver por album")
        print("4. Ver por año")
        print("5. Volver al menu")
        print("6. Volver a imagen")
        numeroV = numero(6)
        opcion = numeroV.numopc()

        if opcion == 1:
            vista = ver_por_autor(lista_imagenes)
            vista.ver_por_autor()
        elif opcion == 2:
            vista = ver_alfabeticamente(lista_imagenes)
            vista.ver_alfabeticamente()
        elif opcion == 3:
            vista = ver_por_album(lista_imagenes),ñ
            vista.ver_por_album()
        elif opcion == 4:
            vista = ver_por_año(lista_imagenes)
            vista.ver_por_año()
        elif opcion == 5:
            salir = True
        elif opcion == 6:
            self.menuimag()
    def clr(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    #menu principal
    def menu(self):
        print("$$     $$   $$$$$$   $$   $$   $$     $$         ")
        print("$$$   $$$   $$       $$$  $$   $$     $$       ")
        print("$$  $  $$   $$$$$    $$ $ $$   $$     $$         ")
        print("$$     $$   $$       $$  $$$   $$     $$     ")
        print("$$     $$   $$$$$$   $$   $$   $$$$$$$$$  \n    ")
        print("Introduzca la opcion que desee:\n")
        print("1. Musica")
        print("2. Videos ")
        print("3. Imagenes")
        print("4. Salir")
        self.clr()


    #agregar y guardar cancion en el archivo
class ingresar:
    def __init__(self):
        pass

    def ingresar_cancion(self):
        archivo = open("Archivo.txt", "a")
        IngCant = int(input("ingrese cantidad de canciones a subir:"))
        for i in range(IngCant):
            nombre = input("ingrese el nombre de la canción:")
            inter = input("ingrese un interprete:")
            album = input("ingrese un album:")
            año = input("ingrese el año de creación de la canción:")
            genero = input("ingrese el genero de la canción:")

            lista_canciones.append(cancion(nombre,inter, album, año, genero))
            archivo.write("\n" +
                "cancion" + "#" + nombre + "#" + inter + "#" + album + "#" + str(año) + "#" + genero + "#" )
            print("cancion guardada")


            #agregar y guardar imagen en el archivo
    def ingresar_imagen(self):
        archivo = open("Archivo.txt", "a")
        IngCant = int(input("ingrese cantidad de imagenes a subir:"))
        for i in range(IngCant):
            Nombre = input("ingrese el nombre de la imagen:")
            Inter = input("ingrese un interprete:")
            Album = input("ingrese un album:")
            Año = input("ingrese el año de creación de la imagen:")
            lista_imagenes.append(imagen(Nombre, Inter, Album, Año))
            archivo.write("\n"
                          + "imagen" + "#" + Nombre + "#" + Inter + "#" + Album + "#" + str(Año) + "#")
            print ("imagen guardada")


            #agregar y guardar video en el archivo
    def ingresar_video(self):
        archivo = open("Archivo.txt", "a")
        IngCant = int(input("ingrese cantidad de videos a subir:"))
        for i in range(IngCant):
            NOMBRE = input("ingrese el nombre del video:")
            INTER = input("ingrese un interprete:")
            ALBUM = input("ingrese un album:")
            AÑO = input("ingrese el año de creación del video:")
            lista_imagenes.append(video(NOMBRE, INTER, ALBUM, AÑO))
            archivo.write("\n"
                          + "video" + "#" + NOMBRE + "#" + INTER + "#" + ALBUM + "#" + str(AÑO) + "#")
            print("video guardada")




class Order:
    def __init__(self, lista, resultado, tipo):
        self.lista = lista
        self.resultado = resultado
        self.tipo = tipo


    def mostrar_ordenado(self):
        if self.tipo == "nombre":
            for i in range(len(self.resultado)):
                for j in range(len(self.lista)):
                    if self.resultado[i] == self.lista[j].nombre:
                        print(self.lista[j].nombre, self.lista[j].interprete, self.lista[j].album, self.lista[j].año)
        elif self.tipo == "autor":
            for i in range(len(self.resultado)):
                for j in range(len(self.lista)):
                    if self.resultado[i] == self.lista[j].interprete:
                        print(self.lista[j].interprete, self.lista[j].nombre, self.lista[j].album, self.lista[j].año)
        elif self.tipo == "album":
            for i in range(len(self.resultado)):
                for j in range(len(self.lista)):
                    if self.resultado[i] == self.lista[j].album:
                        print(self.lista[j].album, self.lista[j].nombre, self.lista[j].interprete, self.lista[j].año)
        elif self.tipo == "año":
            for i in range(len(self.resultado)):
                for j in range(len(self.lista)):
                    if self.resultado[i] == self.lista[j].año:
                        print( self.lista[j].año, self.lista[j].nombre, self.lista[j].interprete, self.lista[j].album)
        elif self.tipo == "genero":
            for i in range(len(self.resultado)):
                for j in range(len(self.lista)):
                    if self.resultado[i] == self.lista[j].genero:
                        print(self.lista[j].genero, self.lista[j].nombre, self.lista[j].interprete, self.lista[j].album, self.lista[j].año)


class Ver:
    def __init__(self, lista):
        self.lista = lista
        self.sublista = []

class ver_alfabeticamente(Ver):
    def ver_alfabeticamente(self):
        for i in range(len(self.lista)):
            self.sublista.append(self.lista[i].nombre)

        resultado = sorted(self.sublista, key=operator.itemgetter(0))
        resultado1 = []
        for i in resultado:
            if i not in resultado1:
                resultado1.append(i)
        ordenado = Order(self.lista, resultado1, "nombre")
        ordenado.mostrar_ordenado()

class ver_por_autor(Ver):
# ordenar los datos guardados por autor
    def ver_por_autor(self):
        for i in range(len(self.lista)):
            self.sublista.append(self.lista[i].interprete)

        resultado = sorted(self.sublista, key=operator.itemgetter(0))
        resultado1 = []
        for i in resultado:
            if i not in resultado1:
                resultado1.append(i)
        ordenado = Order(self.lista, resultado1, "autor")
        ordenado.mostrar_ordenado()

class ver_por_album(Ver):
# ordenar los datos guaardados por album
    def ver_por_album(self):
        for i in range(len(self.lista)):
            self.sublista.append(self.lista[i].album)

        resultado = sorted(self.sublista, key=operator.itemgetter(0))
        resultado1 = []
        for i in resultado:
            if i not in resultado1:
                resultado1.append(i)
        ordenado = Order(self.lista, resultado1, "album")
        ordenado.mostrar_ordenado()

class ver_por_año(Ver):
# ordenar los datos guardados por año
    def ver_por_año(self):
        for i in range(len(self.lista)):
            self.sublista.append(self.lista[i].año)

        resultado = sorted(self.sublista, key=operator.itemgetter(0))
        resultado1 = []
        for i in resultado:
            if i not in resultado1:
                resultado1.append(i)
        ordenado = Order(self.lista, resultado1, "año")
        ordenado.mostrar_ordenado()

class ver_por_genero(Ver):
# ordenar los datos guardados por genero
    def ver_por_genero(self):
        for i in range(len(self.lista)):
            self.sublista.append(self.lista[i].genero)

        resultado = sorted(self.sublista, key=operator.itemgetter(0))
        resultado1 = []
        for i in resultado:
            if i not in resultado1:
                resultado1.append(i)
        ordenado = Order(self.lista, resultado1, "genero")
        ordenado.mostrar_ordenado()


#crear listas y albumes hechos por el usuario
class crear_listas:

    def __init__(self,tipo, listaPrincipal):
        self.tipo = tipo
        self.listaPrincipal = listaPrincipal
        self.n = None

    def crear_lista(self):
        archivo = open("Archivo.txt", "a")
        nombres = []
        for i in range(len(self.listaPrincipal)):
            print (self.listaPrincipal[i].nombre)
            nombres.append(self.listaPrincipal[i].nombre)
        lista = []
        if self.tipo=="cancion":
            n = input("ingrese numero de canciones a guardar en la lista ")
            archivo.write("\n"+"listaCanciones"+"#")
        elif self.tipo=="imagen":
            n = input("ingrese numero de imagenes a guardar en el album ")
            archivo.write("\n" + "listaImagenes"+"#")
        elif self.tipo=="video":
            n = input("ingrese numero de videos a guardar en el album ")
            archivo.write("\n" + "listaVideos"+"#")
        i=1
        n = int(n)


        while i <= n:
            nombre_verificado = self.verificar_nombre(nombres)
            i+=1
            lista.append(nombre_verificado)
            archivo.write(nombre_verificado+"#")

        if self.tipo == "cancion":
            listas_canciones.append(lista)
        elif self.tipo == "imagen":
            albumes_imagenes.append(lista)
        elif self.tipo == "video":
            albumes_videos.append(lista)

    #verificar el nombre ingresado existe
    def verificar_nombre(self, nombres):
        nombre = input("ingrese el nombre de " + self.tipo)
        if nombre in nombres:
            return nombre
        else:
            return self.verificar_nombre(nombres)

#ver listas y albumes creados por el usuario
class ver_listas:

    def __init__(self, tipo, lista):
        self.tipo = tipo
        self.lista = lista

    def ver_lista(self):
        tamaño = len(self.lista)
        i=0

        if tamaño == 0:
            print ("No hay listas")

        else:
            if self.tipo == "cancion":
                print("la musica tiene las siguientes listas de canciones")
            else:
                print("los siguientes son los albumes de:",self.tipo)
            while i<tamaño:
                print("lista", i+1, ":")
                j = 0
                while j < len(self.lista[i]):
                    listaAux = self.lista[i]
                    print (listaAux[j])
                    j += 1
                i += 1


            #main ejecutable del programa
class Reproductor_multimedia:

    def __init__ (self):
        pass

    def main(self):
        with open("Archivo.txt") as archivo:
            lineas = archivo.readlines()
            i=0
            
            for item in lineas:
                caracteres = lineas[i].split("#")
                if caracteres[0] == "cancion":
                    lista_canciones.append(cancion(caracteres[1], caracteres[2],caracteres[3],caracteres[4],caracteres[5]))
                    i += 1
                elif caracteres[0] == "imagen":
                    lista_imagenes.append(imagen(caracteres[1], caracteres[2],caracteres[3],caracteres[4],))
                    i += 1
                elif caracteres[0] == "video":
                    lista_videos.append(imagen(caracteres[1], caracteres[2],caracteres[3],caracteres[4],))
                    i += 1
                elif caracteres[0] == "listaCanciones":
                    lista = []
                    nombres = len(caracteres)
                    j = 1
                    while j < nombres:
                        lista.append(caracteres[j])
                        j += 1
                    listas_canciones.append(lista)
                    i += 1
                elif caracteres[0] == "listaImagenes":
                    lista = []
                    nombres = len(caracteres)
                    j = 1
                    while j < nombres:
                        lista.append(caracteres[j])
                        j += 1
                    albumes_imagenes.append(lista)
                    i += 1
                elif caracteres[0] == "listaVideos":
                    lista = []
                    nombres = len(caracteres)
                    j = 1
                    while j < nombres:
                        lista.append(caracteres[j])
                        j += 1
                    albumes_videos.append(lista)
                    i += 1
                elif caracteres[0] == "\n":
                    i += 1
                else:
                    print ("error en el archivo, por favor reviselo")
                    exit()


        Reproductor = ventana()
            

reproducir = Reproductor_multimedia()
reproducir.main()
