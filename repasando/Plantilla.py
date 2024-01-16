"""

"""
import os.path
import pickle
import random
import io

__author__ = " "

class :
    def __init__(self, , , , , ):
        self. =
        self. =
        self. =
        self. =
        self. =

def to_string(lin):
    r = ""
    r += "{:<20}".format(" " + str())
    r += "{:<30}".format(" " + )
    r += "{:<20}".format(" " + )
    r += "{:<20}".format(" " + )
    r += "{:<20}".format(" " + )
    return r

def validar(min, max):
    print("Ingrese un valor entre", min, "y", max,)
    v = int(input())
    while v < min or v > max:
        print("¡¡Error, valor ingresado no valido!!")
        print("Ingrese un valor entre", min, "y", max,)
        v = int(input())
    return v

def validar_car(caracteres):
    c = ' '
    while c not in caracteres:
        c = input('Letras válidas ' + str(caracteres) + ': ')
        if c not in caracteres:
            print('\t\tError... letra no válida... cargue de nuevo...')
    return c

def validar_con_min(lim):
    n = lim - 1
    while n <= lim:
        n = int(input('Valor mayor a ' + str(lim) + ' por favor: '))
        if n <= lim:
            print('\t\tError... cargue de nuevo...')
    return n

#Con busqueda binaria
def add_in_order(arreglo, registro):
    n = len(arreglo)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if arreglo[c].numero == registro.numero :
            pos = c
            break
        if registro.numero < arreglo[c].numero:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    arreglo[pos:pos] = [registro]

def cargar_arreglo_ordenado():
    arreglo = []
    print('A continuacion ingresara la cantidad de registros...')
    n = validar(0, 2**50)
    print()
    print('Ingrese los datos de los registros...')
    for i in range(n):
        print('Valor 1...')
        var1 = validar(0, 2**50)
        str = input('String: ')
        print('Otro tipo de valor...')
        var2 = validar(0, 19)
        print('Otro tipo de valor...')
        var3 = int(input("Ingresar la cantidad: "))
        registro = Registro(var1, str, var2, var3)
        add_in_order(arreglo, registro)
        print()
    return arreglo

def mostrar(arreglo):
    for registro in range(len(arreglo)):
        print(to_string(arreglo[registro]))
        print()
    input("Lectura terminada. Enter para continuar.")

def gen_archive(arreglo):
    global FD

    if len(arreglo) == 0:
        print('No hay datos cargados...')
        print()
        return

    m = open(FD, "a+b")

    for registro in range(len(arreglo)):
        pickle.dump(arreglo[registro], m)

    #Usar lo siguiente en caso de que pidan ingresar solo registros con cierta cantidad minima o maxima de algun valor. (y suplantar
    # por el for anterior, claro)
    """
    x = int(input("Cantidad minima de x para cada registro a ingresar en el archivo: "))
    for registro in range(len(arreglo)):
        if arreglo[registro].val > x:
            pickle.dump(arreglo[registro], m)
    """

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

    #Lo siguiente solo en caso de que te pidan sacar un porcentaje con respecto al total.
    """ 
    cont_all = 0
    cont_valor = 0
    print("A continuacion ingresara valor para comprobar su porcentaje con respecto al archivo creado.")
    y = validar(val1, val2)"""

    print('Contenido del archivo', FD, '...')
    while m.tell() < tbm:
        registro = pickle.load(m)

        #Solo en caso de porcentaje
        """cont_all += 1
        if registro.valor == y:
            cont_val += 1"""

        print(to_string(registro))

    m.close()
    print()

    #Porcentaje, jsdjfsd
    """
    porc = (cont_valor / cont_all) * 100
    print("El porcentaje que representan el valor", y, "con respecto al total, es de", str(porc) + "%")
    """

def conteo(l):
    if len(l) == 0:
        print('No hay datos cargados...')
        print()
        return

    cf, cc = ?, ?
    cant = [cc*[0] for f in range(cf)]

    for registro in arreglo:
        f = registro.var1
        c = registro.var2
        cant[f][c] += registro.var3
        or
        cant[f][c] += 1

    print('Cantidad de var3 por var1 y var2...')
    for f in range(cf):
        for c in range(cc):
            if cant[f][c] != 0:
                print('Var1: ', f, ' - Var2: ', c, ' - Var3: ', cant[f][c])

def main():
    global FD
    FD = "(Nombre del archivo)"

    op = 0
    arreglo = []
    while op != 7:
        op = int(input("Empresa de Celulares - Gestión de Lineas\n"
                       "Elija entre las siguientes opciones:\n"
                       "1- Cargar\n"
                       "2- Mostrar\n"
                       "3- \n"
                       "4- \n"
                       "5- \n"
                       "6- \n"
                       "7- Salir del programa\n"
                       "Ingrese su opción: "))
        if op == 1:
            arreglo = cargar_arreglo_ordenado()
        elif op == 2:
            mostrar(arreglo)
        elif op == 3:
            #Función
            pass
        elif op == 4:
            #Función
            pass
        elif op == 5:
            #Función
            pass
        elif op == 6:
            #Función
            pass
        elif op == 7:
            pass
    input("Programa finalizado. Enter para cerrar")

# script principal...
if __name__ == '__main__':
    main()
