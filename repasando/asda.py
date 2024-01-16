'''Desarrollar un programa que permita cargar, para una empresa de cobro de servicios, el detalle de n cobranzas realizadas (n se carga por teclado) conteniendo la siguiente información: número de caja (0-9 inclusive), turno (0=mañana, 1= tarde, 2 = noche) y monto cobrado.

A medida que se cargan los datos, se pide generar una tabla resumen, dando a elegir al usuario una carga manual o automática, donde cada fila represente una caja y cada columna un turno, totalizando los montos cobrados.

Mostrar el contenido de la tabla, y luego informar:

Recaudación promedio, para una caja que se ingresa por teclado
Total recaudado por cada turno, cuál es el mayor y qué porcentaje representa sobre la recaudación total.
Qué caja y turno tuvo la menor recaudación acumulada'''
import random

#from general import *

def cargar_matriz(n, carga, m):
    for i in range(n):
        if carga == 'M' or carga =='m':
            # Manualmente...
            caja = validar_entre(0, 9, 'ingrese caja (0-9): ')
            turno = validar_entre(0, 2, 'Ingrese tuno (0-2): ')
            monto = validar_mayor_que(0, 'Ingrese monto: $')
        elif carga == 'A' or carga == 'a':
            caja = random.randint(0, 9)
            turno = random.randint(0, 2)
            monto = random.randint(100, 1000)
        m[caja][turno] += monto



def validar_mayor_que(inf, mensaje):
    num = int(input(mensaje))
    while num <= inf:
        print('ERROR! Se requiere un valor mayor que ', inf)
        num = int(input(mensaje))

    return num


def validar_entre(inf, sup, mensaje):
    num = int(input(mensaje))
    while num < inf or num > sup:
        print('ERROR! Se requiere un valor entre', inf, 'y ',sup)
        num = int(input(mensaje))

    return num

def principal():
    print('COBRO DE SERVICIOS')
    n = validar_mayor_que(0, 'Ingrese cantidad de cobranzas: ')
    carga = input('Elija carga (M)anual o (A)utomática: ')
    m = [[0] * 3 for f in range(10)]
    print(m)
    cargar_matriz(n, carga, m)



if __name__ == '__main__':
    principal()
