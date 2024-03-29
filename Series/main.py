"""Un amigo tiene una lista de series que le gustaría ver, guardadas en un archivo “series.csv” y nos pide ayuda para poder manejar dicha lista. El archivo posee la siguiente información de cada serie:

Título o nombre
Género: 0-Infantil, 1-Comedia, 2-Romántico, 3-Drama, 4-Ciencia Ficción, 5-Otros.
Idioma Original: 0-Español, 1: Inglés, 2: Francés, 3: Portugués, 4:Otros.
Cantidad de temporadas.
Duracion total (en minutos)
En primer lugar, cargar el contenido del archivo en un vector de registros y ordenarlo por título.

Luego, implementar un menú de opciones que permita:

Listar el contenido del vector, mostrando una línea por serie (usar género y el idioma en lugar de sus códigos).

Ingresar por teclado un idioma x. Generar un archivo cuyo nombre tenga la forma “SeriesX.dat” (reemplazando x por el número del idioma seleccionado) conteniendo todas las series de ese idioma que tengan más de una temporada. Mostrar el nuevo archivo generado.

Buscar en el vector una serie con el título x (x se ingresa por teclado). Si la serie existe, mostrar sus datos. Si no, informar con un mensaje.

Determinar la duración total de las series en idioma español por cada género disponible.

A partir del vector determinar la cantidad de series por género y por idioma. Para eso se debe utilizar una matriz de conteo. Mostrar las cantidades sólo cuando sean mayores a 0."""

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import os
import pickle
from registro import *


def mostrar_menu():
    print('-' * 80)
    print('CATÁLOGO DE SERIES')
    print('1. Mostrar vector')
    print('2. Generar archivo por idioma')
    print('3. Buscar por título')
    print('4. Duración de series en español por género')
    print('5. Contar por género e idioma')
    print('0. Salir')
    print('-' * 80)


def leer_csv(fd):
    v = list()
    if os.path.exists(fd):
        f = open(fd, "rt")
        for linea in f:
            serie = csv_to_Serie(linea)
            v.append(serie)
        f.close()
    else:
        print('El archivo', fd, 'no existe')
    return v


def mostrar_vector(v):
    mostrar_titulos()
    for reg in v:
        print(reg)


def ordenar_por_titulo(v):
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            if v[i].titulo > v[j].titulo:
                v[i], v[j] = v[j], v[i]


def validar_entre(desde, hasta, mensaje):
    num = int(input(mensaje))
    while num < desde or num > hasta:
        num = int(input('Inválido! ' + mensaje))
    return num


def generar_archivo(v, idioma, fd):
    f = open(fd, 'wb')
    for reg in v:
        if reg.idioma == idioma and reg.temporadas > 1:
            pickle.dump(reg, f)
    f.close()


def mostrar_archivo(fd):
    hay_datos = False
    if os.path.exists(fd):
        f = open(fd, "rb")
        size = os.path.getsize(fd)
        while f.tell() < size:
            hay_datos = True
            reg = pickle.load(f)
            print(reg)
        f.close()
    if not hay_datos:
        print('El archivo', fd, 'está vacío')


def buscar_binario(v, titulo):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].titulo == titulo:
            return c
        if titulo < v[c].titulo:
            der = c - 1
        else:
            izq = izq + 1
    return -1


def sumar_duracion_por_genero(v):
    va = [0] * 6
    for reg in v:
        if reg.idioma == 0:
            va[reg.genero] += reg.duracion
    return va


def mostrar_acumulador(va):
    for i in range(len(va)):
        print(GENEROS[i], ':', va[i], 'minutos')


def contar_por_genero_idioma(v):
    mc = [[0] * 5 for f in range(6)]
    for reg in v:
        mc[reg.genero][reg.idioma] += 1
    return mc


def mostrar_matriz(m):
    for i in range(len(m)):
        fila = GENEROS[i]
        for j in range(len(m[i])):
            if m[i][j] > 0:
                if fila != "":
                    print(fila)
                    fila = ''
                print('\t', IDIOMAS[j], ':', m[i][j])


def principal():
    v = leer_csv('series.csv')
    if len(v) > 0:
        ordenar_por_titulo(v)
        opcion = -1
        while opcion != 0:
            mostrar_menu()
            opcion = int(input('Ingrese su opción: '))
            if opcion == 1:
                mostrar_vector(v)
            elif opcion == 2:
                idioma = validar_entre(0, 4, 'Ingrese idioma: ')
                fd = "Series" + str(idioma) + ".dat"
                generar_archivo(v, idioma, fd)
                mostrar_archivo(fd)
            elif opcion == 3:
                titulo = input('Ingrese título a buscar: ')
                pos = buscar_binario(v, titulo)
                if pos == -1:
                    print('No se encontró esa serie')
                else:
                    print('Serie encontrada!', v[pos])
            elif opcion == 4:
                va = sumar_duracion_por_genero(v)
                mostrar_acumulador(va)
            elif opcion == 5:
                mc = contar_por_genero_idioma(v)
                mostrar_matriz(mc)


if __name__ == '__main__':
    principal()
