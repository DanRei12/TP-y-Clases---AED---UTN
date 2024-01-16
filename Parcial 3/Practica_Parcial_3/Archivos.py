import os.path
import pickle
import io

'''
__author__ = 'Cátedra de AED'
def test():
    print('Procediendo a grabar números en el archivo')
    m = open('prueba.num', 'wb')
    x, y = 2.345, 19
    pickle.dump(x, m)
    pickle.dump(y, m)
    m.close()
    m = open('prueba.num', 'rb')
    a = pickle.load(m)
    b = pickle.load(m)
    m.close()
    print('Datos recuperados desde el archivo:', a, ' - ', b)
    print('Hecho...')
if __name__ == '__main__':
    test()
'''

__author__ = 'Catedra de AED'
#Se define la clase/registro
class Libro:
    def __init__(self, cod, tit, aut):
        self.isbn = cod
        self.titulo = tit
        self.autor = aut

#Se realiza la lectura de una linea
def display(libro):
    print('ISBN:', libro.isbn, end='')
    print(' - Título:', libro.titulo, end='')
    print(' - Autor:', libro.autor)

#Programa Principal
def test():
    print('Prueba de grabación de varios registros...')
    #Asignacion de libros
    lib1 = Libro(2134, 'Fundación', 'Isaac Asimov')
    lib2 = Libro(5587, 'Fundación e Imperio', 'Isaac Asimov')
    lib3 = Libro(3471, 'Segunda Fundación', 'Isaac Asimov')
    lib4 = Libro(1122, 'Los Límites de la Fundación', 'Isaac Asimov')
    lib5 = Libro(2286, 'Fundación y Tierra', 'Isaac Asimov')
    fd = 'libros.dat'
    m = open(fd, 'wb')
    #Se aumentan los libros al archivo
    pickle.dump(lib1, m)
    pickle.dump(lib2, m)
    pickle.dump(lib3, m)
    pickle.dump(lib4, m)
    pickle.dump(lib5, m)
    m.close()
    print('Se grabaron varios registros en el archivo', fd)
    m = open(fd, 'rb')
    #Se consigue la cantidad de bytes del archivo
    t = os.path.getsize(fd)
    print('Se recuperaron estos registros desde el archivo', fd, ':')
    #Ciclo para leer el archivo sin que se vea interrumpido por pasar el limite de bytes
    while m.tell() < t:
        lib = pickle.load(m)
        display(lib)
    # t = m.seek(-10, io.SEEK_END)
    m.close()

    print('Tamaño del archivo al terminar:', t, 'bytes')
if __name__ == '__main__':
    test()
