'''Enunciado:
Una revista científica desea un programa para procesar los datos de los trabajos que le son enviados para su publicación.
Por cada Trabajo se tienen los siguientes datos: número de identificación del trabajo, título del trabajo, cantidad de
páginas, cantidad de autores, código de área temática del trabajo (un valor entre 0 y 9 ambos incluidos, de la forma 0:
Inteligencia artificial, 1: Informática 2: Lenguajes de programación, etc.). Se desea almacenar la información referida
a los n trabajos en un arreglo de registros de tipo Trabajo (definir el tipo Trabajo y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos, que
permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de los n trabajos. Valide que el tipo de área temática de los trabajos sea
un valor entre 0 y 9 (ambos incluidos). Puede hacer la carga en forma manual, o puede generar los datos en forma
automática (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2- Mostrar todos los datos de los trabajos, en un listado ordenado de menor a mayor según el número de identificación
del trabajo.  Al final del listado mostrar una línea adicional, en la que se indique la cantidad promedio de páginas de
todas las obras que se mostraron.

3- Usando el arreglo creado en el punto 1, determine la cantidad de trabajos por cada área temática (o sea,
10 contadores). Muestre sólo los resultados que correspondan a las áreas cuyo código de área temática sea un número impar.

4- Determinar el trabajo que posea la mayor cantidad de autores y mostrar sus datos. Si existe más de un registro
con esa mayor cantidad de autores, mostrar sólo uno.

5- Determinar si existe un trabajo cuyo número de identificación sea igual a x, siendo x un valor que se carga
por teclado. Si existe mostrar todos sus datos, junto con el importe total a pagar para su publicación, sabiendo que
por cada página debe abonar 350 pesos. Si no existe, informar con un mensaje.'''

import random
import Trabajos

# Funciones.
def carga_manual(n):
    vec = []
    for i in range(n):
        numero = Trabajos.verificar_con_mayor(0,"Ingrese el número de identificación: ")
        titulo = input("Ingrese el titulo: ")
        area = Trabajos.verificar_con_rango(0, 9, "Ingrese el código de area tematica: \n\b0- Inteligencia Artificial \n\b1- Informatica \n\b2- Lenguajes de programación "
                                   "\n\b3- Ayudante \n\b4- Gestión \n\b5- Contaduria "
                                   "\n\b6- Derechos \n\b7- Area de compra "
                                   "\n\b8- Secretaría \n\b9- Limpieza "
                                   "\nIngrese su opción: ")
        cant_pag = int(input("Ingrese la cantidad de paginas: "))
        cant_aut = int(("Ingrese la cantidad de autores: "))
        tra = Trabajos.Trabajos(numero, titulo, area, cant_pag, cant_aut)
        vec.append(tra)
    return vec

def ordenarTrab(vec, n):
    for i in range(len(vec)-1):
        for j in range(i+1, len(vec)):
            if vec[i].numero > vec[j].numero:
                vec[i], vec[j] = vec[j], vec[i]
    return vec

def mostrarTrab(vec):
    for i in range(len(vec)):
        print(Trabajos.to_string(vec[i]), "\n")

def cont_areas(vec):
    cont = [0] * 10
    for i in range(len(vec)):
        cont[vec[i].area] += 1
    return cont

def mostrar_conts(vec_conteo):
    for i in range(len(vec_conteo)):
        if vec_conteo[i] % 2 != 0:
            print("\nCantidad total por area:", Trabajos.areas[i],  ":", vec_conteo[i], "\n")

def Max_cant_aut(vec):
    vec_max = None
    max_cant_aut = 0
    for i in range(len(vec)):
        if vec[i].cant_aut > max_cant_aut:
            max_cant_aut = vec[i].cant_aut
            vec_max = i
    print("\nEl trabajo con mayor cantidad de autores es el siguiente:\n", Trabajos.to_string(vec[vec_max], "\n"))

def buscar_num_id(vec, num):
    importe = 0
    for i in range(len(vec)):
        if vec[i].numero == num:
            print(Trabajos.to_string(vec[i]))
            importe = vec[i].cant_pag * 350
            print("\nEl importe total de publicacion es de:", importe, "\n")
            return importe

def main():
    op = 0
    while op < 7:
        op = int(input("Revista de Cientificos. \nSeleccione una de las siguientes opciones: \n\b "
                       "1- Cargar datos de trabajos. \n\b "
                       "2- Muestra de datos según número de identificación. \n\b "
                       "3- Cantidad de trabajos por area. \n\b "
                       "4- Trabajo con mas autores. \n\b "
                       "5- Verificar si existe el numero identificador (y darle importe) \n\b"
                       "6- Salir del programa. \n\b"
                       "Ingrese su opción: "))

        if op == 1:
            n = int(input("Ingresar la cantidad de Trabajos a registrar: "))
            band_carga = False
            while band_carga == False:
                carga = int(input("¿Desea una carga manual(0) o automatica(1)?\n"))

                if carga == 0:
                    vecTrabajos = carga_manual(n)
                    print("La carga manual ha sido correcta.\n")
                    band_carga = True

                elif carga == 1:
                    vecTrabajos = Trabajos.carga_automatica(n)
                    print("\nLa carga automatica ha sido correcta.\n")
                    band_carga = True

                else:
                    print("Carga incorrecta.\n")

            input("Enter para continuar.")
            cargado = True

        elif op == 2:
            cont_pag = 0
            if cargado:
                vec = ordenarTrab(vecTrabajos, n)
                mostrarTrab(vec)
                for i in range(n):
                    cont_pag += vec[i].cant_pag
                print("\n El promedio de paginas es de:", cont_pag / n)
            else:
                print("Ejecutar primero la opción 1 por favor.")

        elif op == 3:
            if cargado:
                vec_conteo = cont_areas(vecTrabajos)
                mostrar_conts(vec_conteo)
            else:
                print("Ejecutar primero la opción 1 por favor.")

        elif op == 4:
            if cargado:
                Max_cant_aut(vecTrabajos)
            else:
                print("Ejecutar primero la opción 1 por favor.")

        elif op == 5:
            if cargado:
                numero = int(input("\nIngrese el numero identificador a buscar: \n"))
                tra = buscar_num_id(vecTrabajos, numero)
                if tra == None:
                    print("\nNo existen trabajos con ese numero de identificación.\n")
            else:
                print("\nEjecutar primero la opción 1 por favor.\n")

        elif op == 6:
            print("Eligio terminar el programa.")
            input("Presione enter para terminar.")

    print("Fin del programa.")

# Main script...
if __name__ == "__main__":
    main()
