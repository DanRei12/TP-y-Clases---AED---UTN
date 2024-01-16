"""Un estudio cinematográfico solicita un programa para procesar los datos de las películas que tiene producidas.
Por cada película, se tienen los siguientes datos: número de identificación (un entero), título (una cadena),
el tipo de película (un entero entre 1 y 20 para indicar, por ejemplo: 1: infantil, 2: acción, etc.), la calificación
(otro entero, entre 0 y 5 para indicar por ejemplo: 0: apta para todo público, 1: apta para mayores de 13, etc.) y el
costo de producción (un flotante).  Se pide definir en un módulo separado el tipo de registro Pelicula con los campos
pedidos, y desarrollar en un segundo módulo un programa en Python controlado por menú de opciones que permita gestionar
las siguientes tareas:

1) Cargar un arreglo de registros con los datos de n películas de manera que en todo momento se mantenga ordenado por
título, de menor a mayor. Para esto debe utilizar el algoritmo de inserción ordenada con búsqueda binaria (se
considerará directamente incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar
el algoritmo de inserción ordenada, pero con búsqueda secuencial). Puede hacer la carga en forma manual (en cuyo caso
realice las validaciones que sean necesarias), o puede generar los datos en forma automática (con valores aleatorios
generados en el rango correcto). Pero si hace carga manual, TODA la carga debe ser manual, y si la hace automática
entonces TODA debe ser automática.

2) Mostrar los datos de las películas (a razón de una por por línea de pantalla) cuyo costo sea mayor a un valor c que
se carga por teclado y cuyo tipo sea igual al valor t que también se carga por teclado.

3) Usando el arreglo creado en el punto 1, determine la cantidad de películas por cada combinación posible de tipo y
calificación (o sea, 120 contadores: cantidad de películas tipo 1 con calificación 0,  tipo 1 con calificación 2, etc.).
 Genere TODOS los contadores, pero muestre sólo los resultados que correspondan a los tipos de películas que sean mayores
 al valor t que se carga por teclado.

4) Usando el arreglo creado en el punto 1, generar un archivo con todas las películas cuyo costo sea menor al costo
promedio de todas las películas del vector. Si el archivo ya existía, eliminar su contenido y comenzar desde cero.

5) Mostrar por pantalla el contenido del archivo creado en el punto anterior. Pero al final del listado, muestre una
línea adicional indicando la cantidad de registros que se mostraron que eran del tipo x, cargando x por teclado."""

import pickle
import os.path
import random
from Pelicula import Pelicula

__author__ = 'Candela Cardoso'

titulos =['Justice League', 'Akira', 'It', 'Ghost in the Shell', 'The Godfather', 'Princess Mononoke', 'Perfect Blue',
          'Kill Bill', 'V for Vendetta', 'Ratatouille', 'Sicko', 'Inception', 'Season of the Witch', 'War Horse',
          'The Place Beyond the Pines', 'Ted', 'Big Bad Wolves', 'Her', 'Prisoners', 'Dragon Quest Your Story',
          'Marriage Story', 'The Irishman', 'Texas Chainsaw', 'Le Voyage dans la Lune', 'The Killing', '2001 A Space Odyssey',
          'A Clockwork Orange', 'Jaws', 'Tommy', 'Carrie', 'The Shining', 'The Thing', 'Scarface', 'Black Rain', 'Goodfellas',
          'Ghostbusters', 'Misery', 'Fight Club', 'A Quiet Place']
archive = 'Pelis.pel'


def añadir(v, peliculas):
    n = len(v)
    pos = n

    izq, der = 0, n-1
    while izq <= der:
        b = (izq + der) // 2
        if v[b].titulo == peliculas.titulo:
            pos = b
            break
        if peliculas.titulo < v[b].titulo:
            der = b - 1
        else:
            izq = b + 1
    if izq > der:
        pos = izq
    v[pos:pos] = [peliculas]

def carg_vec():
    v = []
    n = int(input('Marque la cantidad de peliculas a registrar: '))
    for i in range(n):
        num_id = int(random.randint(1000, 100000))
        nom = str(random.choice(titulos))
        tipo = int(random.randint(1, 20))
        clas = int(random.randrange(0, 5))
        cost = float(random.randint(1000000, 100000000))

        peliculas = Pelicula(num_id, nom, tipo, clas, cost)
        añadir(v, peliculas)
    print('Carga registrada con sumo exito.')
    input()
    return v, n

def to_string(pelicula):
    r = ''
    r += '{:<20}'.format('Numero de Identificacion: ' + str(pelicula.identificacion))
    r += '{:<30}'.format(' - Nombre: ' + pelicula.titulo)
    r += '{:<20}'.format(' - Tipo de Pelicula: ' + str(pelicula.tipo))
    r += '{:<20}'.format(' - Clasificación: ' + str(pelicula.calificacion))
    r += '{:<20}'.format(' - Costo de producción: ' + str(pelicula.costo))
    return r

def mostrar_peli(v):
    m = int(input('Ingrese el costo minimo para las peliculas a mostrar: '))
    n = int(input('Ingrese el tipo de peliculas a mostrar (de 1 a 20): '))
    for peli in v:
        if peli.costo >= m and peli.tipo == n:
            print(to_string(peli))

def gen_matriz(vec):
    if len(vec) == 0:
        print('No hay datos cargados aún, por favor ejecutar opción 1 primero')
        print()
        return []

    t = int(input('Ingrese el valor de tipo minimo para los contadores a mostrar (de 1 a 20): '))
    cant_f, cant_c = 21, 6
    matriz = [cant_c*[0] for f in range(cant_f)]

    for tema in vec:
        f = tema.tipo
        c = tema.calificacion
        matriz[f][c] += 1

    print('Cantidad de peliculas para el tipo', t, ':')
    for f in range(cant_f):
        for c in range(cant_c):
            if (f+1) > t:
                print('Tipo: ' + str(f+1) + ' - Calificación: ' + str(c) + ' - Cantidad de peliculas: ', matriz[f][c])
    return matriz

#Generar archivo binario para idioma especifico.
def gen_bin_arch(vec, n, archive):
    if len(vec) == 0:
        print('No hay datos cargados aún, por favor ejecutar opción 1 primero')
        print()
        return

    cont = 0
    for peli in vec:
        cont += peli.costo
    prom = cont / n

    m = open(archive, 'w+b')
    for peli in vec:
        if peli.costo < prom:
            pickle.dump(peli, m)

    m.close()
    print('Archivo generado correctamente.')

#Mostrar contenido del archivo binario.
def show_archive(archive):
    vec = []
    cont = 0
    x = int(input('Ingrese el tipo del que contar cantidad de registros(del 1 al 20): '))
    if not os.path.exists(archive):
        print('Este archivo', archive, 'aun no existe.\n')
        return

    tbm = os.path.getsize(archive)
    m = open(archive, 'rb')

    print('Contenido de el archivo', archive, '\n')
    while m.tell() < tbm:
        pelicula= pickle.load(m)
        print(to_string(pelicula))
        if pelicula.tipo == x:
            cont += 1

    m.close()

    print('La cantidad de peliculas del tipo', x, 'es de: ', cont)

#Función principal.
def main():
    op = 0
    vec = []
    matriz = []
    while op != 6:
        op = int(input('\nEstudio Cinematografico\n'
                       'Elija entre las siguientes opciones:\n'
                       '1- Cargar datos ordenando por titulo.\n'
                       '2- Mostrar tipo y costo.\n'
                       '3- Cantidad de pelis por tipo y calificación.\n'
                       '4- Generar archivo con pelis menor a costo promedio.\n'
                       '5- Mostrar con cantidad de tal tipo.\n'
                       '6- Salir del programa\n'
                       'Ingrese su opción: '))
        if op == 1:
            vec, n = carg_vec()
        elif op == 2:
            mostrar_peli(vec)
        elif op == 3:
            gen_matriz(vec)
        elif op == 4:
            gen_bin_arch(vec, n, archive)
        elif op == 5:
            show_archive(archive)
        elif op == 6:
            pass

    input('Programa finalizado. Enter para cerrar')

if __name__ == '__main__':
    main()
