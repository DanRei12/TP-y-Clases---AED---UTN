"""Una editorial encargada de la publicación de una revista científica ha
solicitado que se desarrolle un programa para gestionar su operatoria. Se deben almacenar
en un arreglo unidimensional (un vector) los datos relacionados con los artículos disponibles
para su publicación (cargar por teclado la cantidad n de artículos).
Cada artículo tiene los
siguientes datos: código (int), título (cadena), cantidad de páginas, tipo de artículo (puede
ser un valor entre 0 y 9 identificando el campo de aplicación) y el idioma en que está escrito
(un valor entre 0 y 5). Se pide un programa controlado por menú de opciones que permita:

1. Cargar por teclado el arreglo de artículos, que debe quedar ordenado
alfabéticamente de acuerdo al título de los artículos. Alternativamente, la carga
puede hacerse en forma automática, generando en forma aleatoria los valores a
contener en cada registro. Además, verificar que ningún artículo aparezca repetido en
el arreglo (no permita dos artículos con el mismo título).

2. Mostrar el arreglo completo.

3. Cargar por teclado el título de un artículo y determinar si existe alguno con ese título.
Mostrar sus datos si existe, o informar que no existe.

4. Cargar por teclado el código de un artículo y determinar si existe alguno con ese
código. Mostrar sus datos si existe, o informar que no existe.

5. Determinar la cantidad de artículos por tipo e idioma que hay en el arreglo (es decir,
cuántos artículos tipo 0 está escritos en el idioma 0, cuántos tipo 0 están en el idioma
1, y así sucesivamente… con un total de 10*6 = 60 contadores).

6. Generar un archivo que contenga todos los datos de los artículos cuya cantidad de
páginas sea superior a 10.

7. Mostrar el archivo completo. """

import pickle
import os.path

__author__ = 'Catedra de AED'


class Articulo:
    def __init__(self, cod, tit, pg, tp, id):
        self.codigo = cod
        self.titulo = tit
        self.paginas = pg
        self.tipo = tp
        self.idioma = id


def to_string(art):
    r = ''
    r += '{:<30}'.format('Titulo: ' + art.titulo)
    r += '{:<20}'.format('Codigo: ' + str(art.codigo))
    r += '{:<20}'.format('Paginas: ' + str(art.paginas))
    r += '{:<20}'.format('Tipo: ' + str(art.tipo))
    r += '{:<20}'.format('Idioma: ' + str(art.idioma))
    return r


def validar_mayor(lim):
    n = lim - 1
    while n <= lim:
        n = int(input('Valor mayor a ' + str(lim) + ' por favor: '))
        if n <= lim:
            print('\t\tError... se pidio mayor a', lim, '... cargue de nuevo...')
    return n


def validar_intervalo(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Valor entre ' + str(inf) + ' y ' + str(sup)+ ' por favor: '))
        if n < inf or n > sup:
            print('\t\tError... se pidió entre', inf, 'y', sup, '... cargue de nuevo...')
    return n


def validar_titulo(p):
    tit = ''
    while tit == '' or busqueda_binaria(p, tit) != -1:
        tit = input('Título: ')
        if tit == '' or busqueda_binaria(p, tit) != -1:
            print('Nombre repetido o vacío... cargue de nuevo...')

    return tit


def busqueda_binaria(p, tit):
    # busca por título: algoritmo de búsqueda binaria...
    # ...el arreglo está ordenado por título...
    n = len(p)
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2

        if p[c].titulo == tit:
            return c

        if tit < p[c].titulo:
            der = c - 1
        else:
            izq = c + 1

    return -1


def busqueda_secuencial(p, cod):
    # busca por código: algoritmo de búsqueda secuencial...
    # ...el arreglo no está ordenado por código...
    n = len(p)
    for i in range(n):
        if p[i].codigo == cod:
            return i

    return -1


def add_in_order(p, articulo):
    # inserta un registro en el arreglo, en forma ordenada...
    # ...pero aplicando búsqueda binaria para encontrar
    # el punto de inserción...
    n = len(p)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2

        if p[c].titulo == articulo.titulo:
            pos = c
            break

        if articulo.titulo < p[c].titulo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    p[pos:pos] = [articulo]


def cargar_arreglo_ordenado():
    p = []
    print('Cantidad de articulos...')
    n = validar_mayor(0)

    print()
    print('Ingrese los datos de los articulos...')
    for i in range(n):
        tit = validar_titulo(p)

        print('Código...')
        cod = validar_mayor(0)

        print('Cantidad de páginas...')
        pg = validar_mayor(0)

        print('Tipo...')
        tp = validar_intervalo(0, 9)

        print('Idioma...')
        id = validar_intervalo(0, 5)

        articulo = Articulo(cod, tit, pg, tp, id)
        add_in_order(p, articulo)
        print()

    return p


def mostrar_arreglo(p):
    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return

    print('Listado de artículos disponibles')
    for articulo in p:
        print(to_string(articulo))

    print()


def buscar_titulo(p):
    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return

    x = input('Título a buscar: ')
    pos = busqueda_binaria(p, x)

    if pos != -1:
        print('Articulo encontrado...')
        print(to_string(p[pos]))
    else:
        print('No hay un articulo con ese título')

    print()


def buscar_codigo(p):
    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return

    x = int(input('Código a buscar: '))
    pos = busqueda_secuencial(p, x)

    if pos != -1:
        print('Articulo encontrado...')
        print(to_string(p[pos]))
    else:
        print('No hay un articulo con ese código')

    print()


def conteo(p):
    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return

    cf, cc = 10, 6
    cant = [cc*[0] for f in range(cf)]

    for art in p:
        f = art.tipo
        c = art.idioma
        cant[f][c] += 1

    print('Cantidad de artículos por tipo e idioma...')
    for f in range(cf):
        for c in range(cc):
            if cant[f][c] != 0:
                print('Tipo', f, 'Idioma', c, 'Cantidad:', cant[f][c])


def crear_archivo(p):
    global FD

    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return

    print('Cantidad de páginas a controlar...')
    cp = validar_mayor(0)

    print('Grabando artículos con más de', cp, 'en el archivo', FD, '...')
    m = open(FD, 'wb')
    for art in p:
        if art.paginas > cp:
            pickle.dump(art, m)

    m.close()
    print('... hecho')
    print()


def mostrar_archivo():
    global FD

    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe...')
        print()
        return

    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')

    print('Contenido del archivo', FD, '...')
    while m.tell() < tbm:
        art = pickle.load(m)
        print(to_string(art))

    m.close()
    print()


def main():
    global FD
    FD = 'articulos.edi'

    p = []
    op = 0
    while op != 8:
        print('Editorial UTN')
        print('   1. Registrar articulos ordenados por título')
        print('   2. Listado completo de articulos')
        print('   3. Buscar un articulo por título')
        print('   4. Buscar un articulo por código')
        print('   5. Conteo por tipo e idioma')
        print('   6. Crear archivo desde el arreglo (por cantidad de páginas)')
        print('   7. Mostrar el archivo')
        print('   8. Salir')
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()

        if op == 1:
            p = cargar_arreglo_ordenado()

        elif op == 2:
            mostrar_arreglo(p)

        elif op == 3:
            buscar_titulo(p)

        elif op == 4:
            buscar_codigo(p)

        elif op == 5:
            conteo(p)

        elif op == 6:
            crear_archivo(p)

        elif op == 7:
            mostrar_archivo()

        elif op == 8:
            pass


# script principal...
if __name__ == '__main__':
    main()
