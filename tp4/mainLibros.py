
# Enunciado...
"""m = open("libros.csv", mode="rt", encoding="utf8")

Se pide desarrollar un menú con las siguientes opciones:

Cargar: Cargar el contenido del archivo en un vector de registros de libros, que siempre debe mantenerse ordenado por
isbn (Omitir la primera línea del archivo, que contiene el nombre de los campos)

Sumar revisión: El usuario puede optar por buscar el libro por ISBN o por título. Según el criterio elegido se debe
ingresar por teclado el ítem a buscar. Si existe en el vector el libro con el criterio buscado,  mostrar sus datos y
sumar una revisión al mismo. Si no existe mostrar un mensaje por pantalla.

Mayor revisiones: Buscar en el vector el libro con mayor cantidad de revisiones. Informar si su rating es mayor, menor
o igual al rating promedio de su mismo idioma.

Popularidad 2000: A partir del vector, generar una matriz donde cada fila sea un idioma y cada columna
un año de publicación. La celda debe contener el libro que tenga mayor rating para ese idioma y año
(si hubiera varios, elegir sólo uno) sólo para los libros publicados entre el año 2000 y el 2020 (ambos incluídos).

Publicaciones por década: A partir del vector, generar un vector de conteo donde cada celda representa una década entre
1900 y 2000. La celda debe indicar cuántos libros se publicaron en esa década. Mostrar todas las cantidades mayores a
cero. Informar además cuál fue la década con más publicaciones. Si varias tuvieran la misma cantidad, informar todas.

Guardar populares: Si la matriz de la opción 4 ya fue generada, almacenar su contenido registros por registro (omitiendo
las celdas vacías) en un archivo binario llamado populares.dat e informar la cantidad de registros grabados. Si la
matriz aún no fue generada, informarlo.

Mostrar archivo: Listar el contenido del archivo generado en el punto anterior.

"""
# Lista de imports...
import archivegenerator
import Funciones

__author__ = "Grupo_229"


# Función principal...
def main():
    vec1 = []
    band_carga = False
    op = 0
    arreglo = []
    while op != 8:
        op = int(input("Libreria Digital\n"
                       "Elija entre las siguientes opciones:\n"
                       "1- Cargar datos desde el archivo.\n"
                       "2- Sumar revisión\n"
                       "3- Mayor revisión\n"
                       "4- Popularidad del año 2000 hasta 2020.\n"
                       "5- Publicaciones por decada.\n"
                       "6- Guardar populares en archivo binario\n"
                       "7- Mostrar archivo binario\n"
                       "8- Salir del programa\n"
                       "Ingrese su opción: "))
        if op == 1:
            # Cargar datos...
            vec1 = Funciones.carg_arreglo_in_order()
            band_carga = True
        elif op == 2:
            if band_carga:
                # Buscar libro...
                vec1 = Funciones.buscar(vec1)
            else:
                # Si no se encuentra...
                print("Error, vector no generado, por favor ejecutar primero el punto 1")
        elif op == 3:
            if band_carga:
                # Si el vector se encuentra...
                Funciones.may_revs(vec1)
            else:
                # Si el vector no se encuentra...
                print("Error, vector no generado, por favor ejecutar primero el punto 1")
        elif op == 4:
            # Cargar por popularidad en el siglo XXI
            if band_carga:
                # Si se encuentra en el vector...
                popularity = Funciones.gen_matriz(vec1)
            else:
                # Si NO se encuentra en el vector...
                print("Error, vector no generado, por favor ejecutar primero el punto 1")
        elif op == 5:
            if band_carga:
                # Buscar publicaciones por década, sólo si se encuentra en el vector...
                Funciones.pub_dec(vec1)
            else:
                # Si NO se encuentra en el vector...
                print("Error, vector no generado, por favor ejecutar primero el punto 1")
        elif op == 6:
            # Guardar lista de populares...
            archivegenerator.gen_archive(popularity)
        elif op == 7:
            # Mostrar archivo de la opción 6...
            archivegenerator.show_archive()
        elif op == 8:
            # Salir del programa...
            pass

    input("Programa finalizado. Enter para cerrar")

# Script principal...
if __name__ == '__main__':
    main()
