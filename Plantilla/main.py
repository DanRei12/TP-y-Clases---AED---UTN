"""

"""
import os.path
import pickle
import random
import io
import Registro
import Generador

__author__ = " "

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
    n = Registro.validar(0, 2**50)
    print()
    print('Ingrese los datos de los registros...')
    for i in range(n):
        print('Valor 1...')
        var1 = Registro.validar(0, 2**50)
        str = input('String: ')
        print('Otro tipo de valor...')
        var2 = Registro.validar(0, 19)
        print('Otro tipo de valor...')
        var3 = int(input("Ingresar la cantidad: "))
        registro = Registro(var1, str, var2, var3)
        add_in_order(arreglo, registro)
        print()
    return arreglo

def mostrar(arreglo):
    for registro in range(len(arreglo)):
        print(Registro.to_string(arreglo[registro]))
        print()
    input("Lectura terminada. Enter para continuar.")

def conteo(arreglo):
    if len(arreglo) == 0:
        print('No hay datos cargados...')
        print()
        return

    cf, cc = ?, ?
    cant = [cc*[0] for f in range(cf)]

    for registro in arreglo:
        f = registro.var1
        c = registro.var2
        cant[f][c] += registro.var3

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
            Generador.gen_archive(arreglo)
        elif op == 4:
            #Función
            Generador.show_archive()
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
