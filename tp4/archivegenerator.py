# Lista de imports...
import os.path
import pickle
import Funciones

FD = "populares.dat"


# Función para generar matriz...
def gen_archive(matriz):
    if len(matriz) == 0:
        print("No se encontraron datos del punto 4 para cargar\n")
        return
    cont = 0
    m = open(FD, "a+b")

    for i in range(27):
        for j in range(21):
            flag = False
            if not matriz[i][j]:
                flag = True
            if flag == False:
                pickle.dump(matriz[i][j], m)
                cont += 1

    m.close()
    print("\nArchivo generado correctamente\n")
    print("\nLa cantidad de registros generados fueron", cont, "\n")


# Función para mostrar archivo...
def show_archive():
    global FD

    if not os.path.exists(FD):
        print('El archivo', FD, 'aun no existe.\n')
        return

    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')

    print("Contenido de el archivo", FD, "\n")
    while m.tell() < tbm:
        registro = pickle.load(m)

        print(Funciones.to_string(registro))

    m.close()
