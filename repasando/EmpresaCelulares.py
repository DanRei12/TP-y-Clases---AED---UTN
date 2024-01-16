"""Una empresa dedicada a la venta de líneas para celulares nos pidió un programa que permita realizar una serie de
informes. De cada línea se sabe numero, titular, tipo de plan (valor de 0 a 19), cantidad de minutos consumidos,
provincia donde se activo la línea (valor de 1 a 23)

Usted debe realizar dicho programa, controlado por un menú de opciones para que lleve a cabo los siguientes ítems:

1 - Cargar un vector de n Líneas, validando que el tamaño a cargar sea mayor a cero y que el tipo de producto y tipo de
plan sean válidos. El Arreglo debe generarse en forma ordenada por numero.

2 - Listar todas las líneas a razón de un registro por vez

3 - Generar un archivo binario con todas las líneas donde la cantidad de minutos consumidos superen un valor X ingresado
 por teclado. Muestre dicho archivo a razón de una registro a la vez y al final indique que porcentaje representan las
 líneas del plan Y ingresado por parámetro sobre el total de líneas del archivo

4 - Determinar e informar la cantidad de minutos consumidos por cada tipo de plan y en cada provincia a la que pertenece
esa línea. Son 460 contadores

5 - Mostrar la línea con menor cantidad de minutos consumidos para las provincias x o y (donde ambos valores son
ingresados por parámetro), en caso que haya mas de una mostrarlas a todas

6 - Buscar una línea X ingresada por teclado. Si existe incrementar sus minutos consumidos en un 20% y mostrar los
datos de la línea. Caso contrario indicar con un mensaje que no existe"""

import os.path
import pickle
import random
import io

__author__ = "DanRei"

class Lineas:
    def __init__(self, num, tit, plan, cantmin, prov):
        self.numero = num
        self.titular = tit
        self.plan = plan
        self.cantmin = cantmin
        self.provincia = prov


def to_string(lin):
    r = ''
    r += '{:<20}'.format('Número: ' + str(lin.numero))
    r += '{:<20}'.format('Titular: ' + lin.titular)
    r += '{:<20}'.format('Tipo de plan: ' + str(lin.plan))
    r += '{:<20}'.format('Cantidad de minutos consumidos: ' + str(lin.cantmin))
    r += '{:<20}'.format(' Provincia donde se activó la linea: ' + str(lin.provincia))
    return r

def validate(min, max):
    print("Ingrese un valor entre", min, "y", max,)
    v = int(input())
    while v < min or v > max:
        print("¡¡Error, valor ingresado no valido!!")
        print("Ingrese un valor entre", min, "y", max,)
        v = int(input())
    return v

def add_in_order(l, linea):
    n = len(l)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if l[c].numero == linea.numero:
            pos = c
            break
        if linea.numero < l[c].numero:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    l[pos:pos] = [linea]

def charge_array_in_order():
    l = []
    print('A continuacion ingresara la cantidad de lineas...')
    n = validate(0, 99999999999999999999)
    print()
    print('Ingrese los datos de las lineas...')
    for i in range(n):
        print('Número de linea...')
        num = validate(0, 99999999999999999999)
        tit = input('Titular: ')
        print('Tipo de plan...')
        plan = validate(0, 19)
        print('Cantidad de minutos consumidos...')
        min = int(input("Ingresar la cantidad de minutos: "))
        print('Provincia de linea activa...')
        prov = validate(1, 23)
        linea = Lineas(num, tit, plan, min, prov)
        add_in_order(l, linea)
        print()
    return l

def show_arrray(l):
    for lin in range(len(l)):
        print(to_string(l[lin]))
        print()
    input("Lectura terminada. Enter para continuar.")

def gen_archive(l):
    global FD

    if len(l) == 0:
        print('No hay datos cargados...')
        print()
        return

    m = open(FD, "a+b")
    x = int(input("Cantidad de minutos minima para cada registro a ingresar en el archivo: "))
    for lin in range(len(l)):
        if l[lin].cantmin > x:
            pickle.dump(l[lin], m)

    m.close()
    print("\nArchivo generado correctamente\n")

def show_archive():
    global FD

    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe...')
        print()
        return

    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')

    cont_all = 0
    cont_plan = 0

    print("A continuacion ingresara que tipo de plan quiere comprobar su porcentaje con respecto al archivo creado.")
    y = validate(0, 19)

    print('Contenido del archivo', FD, '...')
    while m.tell() < tbm:
        lin = pickle.load(m)
        cont_all += 1
        if lin.plan == y:
            cont_plan += 1
        print(to_string(lin))

    m.close()
    print()

    porc = (cont_plan / cont_all) * 100
    print("El porcentaje que representan el tipo de plan", y, "con respecto al total, es de", str(porc) + "%")

def conteo(l):
    if len(l) == 0:
        print('No hay datos cargados...')
        print()
        return

    cf, cc = 20, 23
    cant = [cc*[0] for f in range(cf)]

    for lin in l:
        f = lin.plan
        c = lin.provincia - 1
        cant[f][c] += lin.cantmin

    print('Cantidad de minutos consumidos por plan y provincia...')
    for f in range(cf):
        for c in range(cc):
            if cant[f][c] != 0:
                print('Tipo de plan: ', f, ' - Provincia: ', c+1, ' - Cantidad de minutos: ', cant[f][c])

def search_min(l):
    min = []
    filter = []
    print("Ingresar los valores x o y para las provincias a buscar.")
    print("\nValor de x...")
    x = validate(1, 23)
    print("\nValor de y...")
    y = validate(1, 23)

    print("La/Las Linea/Lineas con menor cantidad de minutos, son las siguientes: ")
    for i in range(len(l)):
        if l[i].provincia == x or l[i].provincia == y:
                filter.append(l[i])

    for i in range(len(filter)-1):
        if filter[i].cantmin < filter[i+1].cantmin:
            if min == []:
                min.append(filter[i])

            elif filter[i].cantmin < min[0].cantmin:
                min = []
                min.append(filter[i])

            elif filter[i].cantmin == min[0].cantmin:
                min.append(filter[i])

        elif filter[i].cantmin > filter[i+1].cantmin:
            if min == []:
                min.append(filter[i+1])

            elif filter[i+1].cantmin < min[0].cantmin:
                min = []
                min.append(filter[i+1])

            elif filter[i+1].cantmin == min[0].cantmin:
                min.append(filter[i+1])

    for i in range(len(min)):
        print(to_string(min[i]))

def search_numb(l):
    print("A continuacion ingresara el número que desea buscar.")
    x = validate(0, 999999999999999999)
    band = False

    for i in range(len(l)):
        if l[i].numero == x:
            print("Se incrementa la cantidad de minutos al siguiente registro.")
            print(to_string(l[i]))
            l[i].cantmin += l[i].cantmin / 5
            print("\nAhora el mismo con su aumento de 20% en minutos, es el siguiente:\n")
            print(to_string(l[i]))
            band = True

    if band == False:
        print("\nNo se han encontrado lineas con ese número\n")


def main():
    global FD
    FD = "Lineas.csv"

    op = 0
    l = []
    while op != 7:
        op = int(input("Empresa de Celulares - Gestión de Lineas\n"
                       "Elija entre las siguientes opciones:\n"
                       "1- Cargar Lineas\n"
                       "2- Mostrar Lineas\n"
                       "3- Generar archivo con cierta cantidad de minutos mayor a x\n"
                       "4- Cantidad de minutos por plan y provincia\n"
                       "5- Lineas con menor cantidad de minutos en provincias seleccionadas por usuario\n"
                       "6- Buscar una Linea\n"
                       "7- Salir del programa\n"
                       "Ingrese su opción: "))
        if op == 1:
            l = charge_array_in_order()

        elif op == 2:
            show_arrray(l)

        elif op == 3:
            gen_archive(l)
            show_archive()

        elif op == 4:
            conteo(l)

        elif op == 5:
            search_min(l)

        elif op == 6:
            search_numb(l)

        elif op == 7:
            pass
    input("Programa finalizado. Enter para cerrar")

# script principal...
if __name__ == '__main__':
    main()
