import os.path
import pickle
import random
import io
import Registro

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

        print(Registro.to_string(registro))

    m.close()
    print()

    #Porcentaje, jsdjfsd
    """
    porc = (cont_valor / cont_all) * 100
    print("El porcentaje que representan el valor", y, "con respecto al total, es de", str(porc) + "%")
    """
