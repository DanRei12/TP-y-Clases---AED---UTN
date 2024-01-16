import random
import Transacción
'''Turno 3 - Enunciado 2 (T3E2)

Una entidad bancaria procesa transacciones desde su línea de cajas y a los efectos
de obtener alguna información estadística requiere la construcción de un programa
para registrar datos de cada una. Por cada transacción se tienen los datos siguientes:
el código de operación (un número del 1 al 20), el número de cuenta (un string), el
importe de la operación y el número de caja en la cual se efectuó. Se desea almacenar
la información referida a las n transacciones en un arreglo de registros de tipo
Transaccion (definir el tipo Transaccion y cargar n por teclado).

Se pide desarrollar un programa en Python controlado por un menú de opciones y que
posea como mínimo dos módulos, que permita gestionar las siguientes tareas:

1- Cargar el arreglo pedido con los datos de n transacciones. Valide que el código
de operación sea un número entre 1 y 20 ambos inclusive. Puede hacer la carga en forma
manual, o puede generar los datos en forma automática (con valores aleatorios) o puede
disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

2- Mostrar todos los datos de las transacciones, en un listado ordenado de menor a
mayor según el importe. Al final del listado, mostrar una línea adicional en la que
se indique el importe acumulado de todos los registros que se mostraron.

3- Usando el arreglo creado en el punto 1, determine el importe total de las
transacciones por cada tipo de operación (serán 20 acumuladores). Muestre sólo los
resultados mayores a 0 pero de las transacciones cuyo código de operación sea menor a 10.

4- Determinar la transacción con menor importe. Si ese menor importe es inferior a un
valor x que se carga por teclado y el código de operación del mismo es diferente de 1,
cambie el código de operación de ese registro por el valor 1. Muestre todos los datos
del registro (haya sido modificado o no).

5- Determinar si existe una transacción cuyo número de cuenta sea igual a x, siendo x
un valor que se carga por teclado. Si existe, mostrar sus datos. Si no existe, informar
con un mensaje. Si existe más de un registro que coincida con esos parámetros de
búsqueda, debe mostrar todos los que encuentre.'''



def manual_charge(n):
    vec = []
    for i in range(n):
        opcode = Transacción.validar_rango(1, 20, 'Ingrese el código de operación: ')
        numcuenta = input('Ingrese el numero de cuenta: ')
        importe = int(input('Ingrese el importe: '))
        caja_num = int(input('Ingresar el numero de caja: '))
        ins = Transacción.Transaccion(opcode, numcuenta, importe, caja_num)
        vec.append(ins)
    return vec

def sort_price(vec, n):
    for i in range(len(vec)-1):
        for j in range(i+1, len(vec)):
            if vec[i].importe > vec[j].importe:
                vec[i], vec[j] = vec[j], vec[i]

def mostrar(vec):
    for i in range(len(vec)):
        print(Transacción.to_string(vec[i]), '\n')

def search_num_cuenta(vec, num):
    vec2 = []
    for i in range(len(vec)):
        if vec[i].numcuenta == num:
            vec2.append(vec[i])
    if vec2 != []:
        return vec2
    else:
        return None

def cont_importes(vec):
    cont = [0] * 20
    cont2 = []
    for i in range(len(vec)):
        cont[vec[i].opcode] += vec[i].importe
    for i in range(len(cont) - 10):
        if cont[i] > 0:
            cont2.append(cont[i])
    return cont2

def mostrar_contadors(vec_conteo):
    for i in range(len(vec_conteo)):
        if vec_conteo[i] > 0:
            print('Importe por operación:', Transacción.opcode[i],  ':', vec_conteo[i])

def main():
    opc = 0
    while opc != 6:
        opc = int(input('Bienvenido a la tienda.\n'
              'Elije tu opción:\n'
              '1) Cargar datos de transacciones.\n'
              '2) Mostrar todas las transacciones. \n'
              '3) Total de transacciones por tipo de operación. \n'
              '4) Transacción con menor importe. \n'
              '5) Encontrar transacciones por número de cuenta. \n'
              '6) Salir.\nIngrese su opcion: '))
        if opc == 1:
            print('Usted eligió la opción 1.')
            n = int(input('Ingrese cantidad de transacciones: '))
            band_carga = False
            while band_carga == False:
                carga = int(input('¿Desea una carga manual(0) o automatica(1)?\n'))

                if carga == 0:
                    vecTransacciones = manual_charge(n)
                    print('La carga manual ha sido correcta.\n')
                    band_carga = True

                elif carga == 1:
                    vecTransacciones = Transacción.automatic_charge(n)
                    print('\nLa carga automatica ha sido correcta.\n')
                    band_carga = True

                else:
                    print('Carga incorrecta.\n')

            input('Enter para continuar.')
        elif opc == 2:
            if cargado:
                vec = sort_price(vecTransacciones, n)
                mostrar(vec)
                importe_total = 0
                for i in range(n):
                    importe_total += vec[i].importe
                print('\nLa cantidad de importe total es de:', importe_total, '\n')
            else:
                print('Ejecutar primero la opción 1 por favor.')
            cargado = True

        elif opc == 3:
            if cargado:
                vec_conteo = cont_importes(vecTransacciones)
                mostrar_contadors(vec_conteo)
            else:
                print("Ejecutar primero la opción 1 por favor.")

        elif opc == 5:
            if cargado:
                numero = int(input('Ingrese el numero identificador a buscar: '))
                trans = search_num_cuenta(vecTransacciones, numero)
                if trans != None:
                    print(Transacción.to_string(trans))
                else:
                    print('No existen inscripciones con esos datos.')
            else:
                print('Ejecutar primero la opción 1 por favor.')

# Main script...
if __name__ == "__main__":
    main()
