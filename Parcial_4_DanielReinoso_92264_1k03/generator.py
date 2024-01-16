import os.path
import pickle
import Equipo

FD = "equipo.equ"
def gen_archive(e):


    if len(e) == 0:
        print('No se encontraron datos para cargar\n')
        return

    m = open(FD, "a+b")
    x = 0

    for equipo in range(len(e)):
        x += e[equipo].precio

    x = x / len(e)
    for equipo in range(len(e)):
        if e[equipo].precio < x:
            pickle.dump(e[equipo], m)

    m.close()
    print("\nArchivo generado correctamente\n")

def show_archive():
    global FD

    if not os.path.exists(FD):
        print('El archivo', FD, 'aun no existe.\n')
        return

    tbm = os.path.getsize(FD)
    cont = 0
    m = open(FD, 'rb')

    print('Contenido de el archivo', FD, "\n")
    while m.tell() < tbm:
        equipo = pickle.load(m)
        cont += 1

        print(Equipo.to_string(equipo))

    m.close()
    print("\nLa cantidad total de equipos mostrados fue de", cont, "\n")
