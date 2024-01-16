import os.path
import pickle
import random
import io


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
