class Autor:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def MostrarAutor(self):
        print('Autor '+ self.nombre + ' ' + self.apellido)