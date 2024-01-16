'''Desarrollar un programa controlado por menú de opciones, que permita
gestionar un arreglo de registros (puede suponer el mismo tipo Libro que hemos usado como
ejemplo en esta misma Ficha), y a partir de las opciones del menú proceda a generar un archivo con los datos del arreglo
(o viceversa: volver a crear el arreglo a partir de los datos del archivo). Las opciones que debería incluir son las siguientes:

a.) Crear y cargar un arreglo v de n registros de tipo Libro (puede hacer esta carga en
forma automática).

b.) Mostrar el arreglo.

c.) Crear un archivo libros.dat que contenga todos los registros del arreglo original. Si el
archivo ya existía, eliminar su contenido y comenzar desde cero.

d.) Mostrar el contenido del archivo libros.dat.

e.) Crear nuevamente el archivo libros.dat, de forma que ahora contenga sólo los datos
de los libros cuyo código sea menor que x, cargando el código x por teclado. Si el
archivo ya existía, eliminar su contenido y comenzar desde cero.

f.) A partir del archivo libros.dat, volver a crear en memoria el arreglo v, de forma que
contenga todos los registros del archivo. Reemplace el arreglo creado en el punto a.)
por el que se le pide crear ahora.

g.) A partir del archivo libros.dat, volver a crear en memoria el arreglo v, que contenga
sólo los registros de los libros cuyo código sea mayor a x (cargue x por teclado).
Reemplace el arreglo creado en el punto a.) por el que se le pide crear ahora.
'''
import os.path
import Libros
import pickle

fd = "libros.dat"
def main():
    op = 0
    while op < 8:
        op = int(input("Libros. \nSeleccione una de las siguientes opciones: \n\b "
                       "1- Crear y cargar Libros. \n\b "
                       "2- Muestra arreglo Libros. \n\b "
                       "3- Crear archivo con arreglos. \n\b "
                       "4- Mostrar archivo. \n\b "
                       "5- Crear archivo con Libros menor a código x \n\b"
                       "6- Crear arreglo en base a archivo, y suplanta la del punto 1. \n\b"
                       "7- Crear arreglo en base a archivo, y suplanta la del punto 1, pero con codigo mayor a x. \n\b"
                       "8- Salir. \n\b"
                       "Ingrese su opción: "))

        if op == 1:
            n = int(input("Ingresar la cantidad de Libros a registrar: "))
            vecLibros = Libros.carga_automatica(n)
            print("\nLa carga automatica ha sido correcta.\n")
            input("Enter para continuar.")
            cargado = True

        if op == 2:
            if cargado:
                print("Los libros cargados son los siguientes: \n")
                for i in range(n):
                    print(Libros.to_string(vecLibros[i]), "\n")
            else:
                print("No se a cargado un arreglo de Libros, favor de ejecutar primero la opción 1.")

        if op == 3:
            if cargado:
                m = open(fd, "wb")
                for i in range(n):
                    pickle.dump(vecLibros[i], m)
                m.close()
                print("\nSe han grabado satisfactoriamente los libros.\n")
            else:
                print("No se a cargado un arreglo de Libros, favor de ejecutar primero la opción 1.")

        if op == 4:
            m = open(fd, "rb")
            t = os.path.getsize(fd)
            while m.tell() < t:
                lib = pickle.load(m)
                print("\n", Libros.to_string(lib), "\n")
            m.close()

        if op == 5:
            if cargado:
                x = int(input("Ingrese la cantidad máxima de ISBN para los libros ingresados (los ISBN van desde 1000 hasta 9999): "))
                m = open(fd, "wb")
                for i in range(n):
                    if vecLibros[i].isbn < x:
                        pickle.dump(vecLibros[i], m)
                m.close()
                print("\nSe han grabado satisfactoriamente los libros con ISBN menor a", x, "\n")
            else:
                print("No se ha cargado un arreglo de Libros, favor de ejecutar primero la opción 1.")

        if op == 6:
            m = open(fd, "rb")
            t = os.path.getsize(fd)
            vecLibros = []
            while m.tell() < t:
                vecLibros.append(pickle.load(m))
            print("\nSe ha creado satisfactoriamente el arreglo.\n")
            input()
            for i in range(len(vecLibros)):
                    print(Libros.to_string(vecLibros[i]), "\n")

        if op == 7:
            m = open(fd, "rb")
            x = int(input("Ingrese la cantidad minima de ISBN a ser cargados: "))
            t = os.path.getsize(fd)
            vecLibros = []
            while m.tell() < t:
                vec = pickle.load(m)
                if vec.isbn > x:
                    vecLibros.append(vec)
            print("\nSe ha creado satisfactoriamente el arreglo.\n")
            input()
            for i in range(len(vecLibros)):
                    print(Libros.to_string(vecLibros[i]), "\n")


if __name__ == "__main__":
    main()


