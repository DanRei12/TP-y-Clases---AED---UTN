"""
Una empresa de venta de equipamiento médico mantiene información sobre los distintos aparatos que tiene
a la venta. Por cada equipo se registran los datos siguientes: número de identificación (un entero),
nombre (una cadena), precio, tipo de aparato (un número entero entre 0 y 39 incluidos, para indicar
(por ejemplo): 0: aparato de rayos X, 1: tomógafo, etc.) y código de pais de origen (un valor entre 0 y 19,
para indicar (por ejemplo): 0: Argentina, 1: USA, 2: Italia, etc.) Se pide definir un tipo registro Equipo con
los campos que se indicaron, y un programa completo con menú de opciones para hacer lo siguiente:

1- Cargar los datos de n registros de tipo Equipo en un arreglo de registros (cargue n por teclado).
Valide que el tipo y el pais de origen estén dentro de los valores descriptos. Puede cargar los datos
manualmente, o puede generarlos aleatoriamente (pero si hace carga manual, TODA la carga debe ser manual, y si
la hace automática entonces TODA debe ser automática). El arreglo debe crearse de forma que siempre quede
ordenado de menor a mayor, según el precio, y para hacer esto debe aplicar el algoritmo de inserción ordenada
con búsqueda binaria. Se considerará directamente incorrecta la solución basada en cargar el arreglo completo y
ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con búsqueda secuencial.

2- Mostrar el arreglo creado en el punto 1, a razón de  un registro por línea, pero muestre solo los registros
cuyo precio sea mayor a un valor p cargado por teclado, y que no vengan del país número 8.

3- Buscar en el arreglo creado en el punto 1 un registro en el cual el número de identificación sea igual a
num (cargar num por teclado).  Si existe, mostrar por pantalla todos los datos de ese registro. Si no existe,
informar con un mensaje. La búsqueda debe detenerse al encontrar el primer registro que coincida con el patrón
pedido.

4- A partir del arreglo, crear un archivo de registros en el cual se copien los datos de todos los registros
cuyo precio sea menor al precio promedio de todos los artículos del arreglo.

5- Mostrar el archivo creado en el punto anterior, a razón de un registro por línea en la pantalla. Al final
del listado, mostrar una línea adicional que indique la cantidad de registros que se mostraron.


"""

import random
import Equipo
import generator

__author__ = "Daniel_Reinoso_1k03"

def add_in_order(e, equipo):
    n = len(e)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if e[c].precio == equipo.precio :
            pos = c
            break
        if equipo.precio < e[c].precio:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    e[pos:pos] = [equipo]

def carg_arreglo_in_order():
    e = []
    print('Cuantos equipos desea registrar?')
    n = int(input(""))
    for i in range(n):
        num = random.randrange(100)
        nombre = random.choice(Equipo.nombre)
        precio = random.randrange(1000, 9999)
        tip_apar = random.randrange(40)
        cod_pais = random.randrange(20)
        equipo = Equipo.Equipo(num, nombre, precio, tip_apar, cod_pais)
        add_in_order(e, equipo)
    print("\nCarga generada correctamente.\n")
    return e

def mostrar(e):
    p = int(input("Ingrese el precio minimo para los registros a mostrar: "))
    for i in range(len(e)):
        if e[i].precio > p and e[i].cod_pais != 8:
            print(Equipo.to_string(e[i]))
            print()
    input("Lectura terminada. Enter para continuar.")

def buscar(e):
    number = int(input("Ingresar el numero de identificacion a buscar: "))
    band_buscar = False

    for i in range(len(e)):
        if e[i].num == number:
            print("Se ha encontrado un numero de identificacion similar, el siguiente: ")
            print(Equipo.to_string(e[i]))
            band_buscar = True
            break

    if band_buscar == False:
        print("No se han encontrado valores con ese numero de identificacion.")

def main():
    op = 0
    arreglo = []
    while op != 6:
        op = int(input("Empresa Equipo Medico\n"
                       "Elija entre las siguientes opciones:\n"
                       "1- Cargar datos de equipos medicos.\n"
                       "2- Mostrar registros con filtrado\n"
                       "3- Buscar registro con numero de identificacion especifico\n"
                       "4- Generar archivo en base a promedio de precios\n"
                       "5- Mostrar archivo y cantidad de registros en el.\n"
                       "6- Salir del programa\n"
                       "Ingrese su opción: "))
        if op == 1:
            e = carg_arreglo_in_order()
        elif op == 2:
            mostrar(e)
        elif op == 3:
            buscar(e)
        elif op == 4:
            generator.gen_archive(e)
        elif op == 5:
            generator.show_archive()
        elif op == 6:
            pass

    input("Programa finalizado. Enter para cerrar")

if __name__ == '__main__':
    main()
