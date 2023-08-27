from Autor import Autor
from Libro import Libro
from Biblioteca import Biblioteca

biblioteca1 = Biblioteca()


def MostrarMenu():

    print('\n********* MENU *********')
    print('1. Añadir libro a la biblioteca')
    print('2. Mostrar Biblioteca')
    print('3. Borrar libro')
    print('4. ¿Numero de libros?')
    print('5. SALIR')
    print('************************\n')


def AnadirLibroBiblioteca():
    titulo = input('Introduzca el titulo del libro: ').lower()
    isbn = input('Itroduzca el ISBN: ')
    nombreAutor = input('Introduzca el nombre del autor: ').lower()
    apellidoAutor = input('Introduzca el apellido del autor: ').lower()

    autor = Autor(nombreAutor, apellidoAutor.lower())
    libro = Libro(titulo, isbn, autor)

    Biblioteca.AnadirLibro(biblioteca1, libro)


fin = False

while not fin:

    MostrarMenu()
    try:
        opcion = int(input('Seleccione una opcion: '))
        if opcion < 1 or opcion > 5:
            print('OPCION NO VALIDA OPCIONES DEL 1 AL 5')
            MostrarMenu()
    except:
        print('INTRODUZCA UN NUMERO DEL 1 AL 5 PORFAVOR!!!')
        MostrarMenu()

    if opcion == 1:
        AnadirLibroBiblioteca()

    elif opcion == 2:
        Biblioteca.MostrarBiblioteca(biblioteca1)

    elif opcion == 3:
        print('**** BORRAR LIBRO ****')
        isbn = input('Introdce el ISBN del libro que deseas borrar: ')
        Biblioteca.BorrarLibro(biblioteca1,isbn)

    elif opcion == 4:
        Biblioteca.NumeroLibros(biblioteca1)
    
    elif opcion == 5:
        fin = True