class Libro:

    def __init__(self, titulo, isbn, autor):

        self.titulo = titulo
        self.isbn = isbn
        self.autor = autor

    def MostrarLibro(self):

        print('****** Libro ******')
        print('Titulo: ' + self.titulo.capitalize())
        print('ISBN: ' + self.isbn)
        print('Autor: ' + self.autor.nombre.capitalize() + ' ' + self.autor.apellido.capitalize())
        print('*******************\n')
    
    def ObtenerTitulo(self):
        return self.titulo
    
    
    