from Libro import Libro
from Autor import Autor


class Biblioteca:

    def __init__(self):
        self.listaLibros = listaLibros = []

    def NumeroLibros(self):
        print('En la biblioteca, hay ' + str(len(self.listaLibros)) + ' libros.')

    def AnadirLibro(self, libro):
        self.listaLibros.append(libro)

    def MostrarBiblioteca(self):
        print('\n--------- BIBLIOTECA ----------------\n')
        for libro in self.listaLibros:
            Libro.MostrarLibro(libro)
        print('---------------------------------------\n')

    def BorrarLibro(self, isbn):

        libroEncontrado = False

        for libro in self.listaLibros:
            
            if libro.isbn == isbn:
                self.listaLibros.remove(libro)
                print('El libro se ha borrado correctamente')
                libroEncontrado = True

        if libroEncontrado == False:
            print('¡¡¡¡¡ El libro introducido no esta en la biblioteca !!!!!')
