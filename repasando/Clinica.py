"""Un consultorio médico necesita un programa para gestionar los datos de sus
pacientes. Por cada paciente, se deben almacenar los siguientes elementos: número de
historia clínica (un número entero), nombre del paciente, fecha de la última visita (en días –
otro número entero) y código de la enfermedad o problema registrado (un valor entre 0 y 9
incluidos). Los datos deben cargarse y almacenarse inicialmente en un arreglo de registros, a
razón de un registro por paciente, el cual debe mantenerse en todo momento ordenado de
menor a mayor de acuerdo al valor del número de historia clínica de los pacientes. El
programa debe incluir un menú con las opciones siguientes:

    1. Cargar el arreglo con los registros pedidos (recuerde: el arreglo debe mantenerse
    ordenado por historia clínica: cada registro debe insertarse en el lugar correcto
    cuando se agrega al arreglo).

    2. Cargar por teclado un número entero d, y mostrar por pantalla los datos de todos los
    pacientes del arreglo que hayan asistido al consultorio por última vez en un período
    de d días o más.

    3. Determinar si en el arreglo existe un paciente con número de historia clínica igual a x.
    Si existe, mostrar todos sus datos. Si no, dar un mensaje de error.

    4. Mostrar todos los datos del arreglo.

    5. Grabe todos los datos del arreglo en un archivo (para favorecer el desarrollo de los
    puntos que siguen, asegúrese de hacerlo de forma que cada registro se grabe por
    separado, uno por uno). El archivo debe ser creado si no existía, y todo dato que
    hubiese contenido debe ser eliminado si ya existía.

    6. Mostrar el archivo generado en el punto anterior.

    7. Usando el archivo creado en el punto 5, crear en memoria otro arreglo que contenga
    los registros de los pacientes cuyo código de enfermedad sea 8 o 9. Recuerde: debe
    crear otro arreglo de registros, y no eliminar ni modificar el original que se creó en el
    punto 1.

    8. Mostrar el arreglo creado en el punto 7"""

import pickle
import os.path
__author__ = 'Catedra de AED'
class Paciente:
    def __init__(self, hc, nom, fec, cod):
        self.hist_clinica = hc
        self.nombre = nom
        self.fecha = fec
        self.cod_problema = cod

def to_string(pac):
    r = ''
    r += '{:<25}'.format('Historia Clinica: ' + str(pac.hist_clinica))
    r += '{:<30}'.format('Nombre: ' + pac.nombre)
    r += '{:<20}'.format('Fecha: ' + str(pac.fecha))
    r += '{:<20}'.format('Problema: ' + str(pac.cod_problema))
    return r

def validar_mayor(lim):
    n = lim - 1
    while n <= lim:
        n = int(input('Valor mayor a ' + str(lim) + ' por favor: '))
        if n <= lim:
            print('\t\tError... se pidio mayor a', lim, '... cargue de nuevo...')
    return n

def validar_intervalo(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Valor entre ' + str(inf) + ' y ' + str(sup)+ ' : '))
        if n < inf or n > sup:
            print('\t\tError... cargue de nuevo...')
    return n

def add_in_order(p, paciente):
    n = len(p)
    pos = n
    for i in range(n):
        if paciente.hist_clinica < p[i].hist_clinica:
            pos = i
            break
    p[pos:pos] = [paciente]
'''
# Misma función, pero con búsqueda binaria...
def add_in_order(p, paciente):
    n = len(p)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if p[c].hist_clinica == paciente.hist_clinica:
            pos = c
            break
        if paciente.hist_clinica < p[c].hist_clinica:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    p[pos:pos] = [paciente]
'''

def cargar_arreglo_ordenado():
    p = []
    print('Cantidad de pacientes...')
    n = validar_mayor(0)
    print()
    print('Ingrese los datos de los pacientes...')
    for i in range(n):
        print('Número de historia clínica...')
        hc = validar_mayor(0)
        nom = input('Nombre: ')
        print('Días transcurridos desde su última visita...')
        dias = validar_mayor(0)
        print('Código de enfermedad o problema...')
        cod = validar_intervalo(0, 9)
        paciente = Paciente(hc, nom,dias, cod)
        add_in_order(p, paciente)
        print()

    return p

def listado_por_dias(p):
    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return
    d = int(input('Días a comprobar desde la última visita: '))
    print('Pacientes con', d, 'o más días desde la última visita')
    for paciente in p:
        if paciente.fecha >= d:
            print(to_string(paciente))
            print()

def mostrar_arreglo(p, mensaje='Contenido:'):
    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return
    print(mensaje)
    for paciente in p:
        print(to_string(paciente))
        print()

def buscar(p):
    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return
    x = int(input('Número de historia clínica a buscar: '))
    n = len(p)
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if p[c].hist_clinica == x:
            print('Paciente encontrado...')
            print(to_string(p[c]))
            print()
            return
        if x < p[c].hist_clinica:
            der = c - 1
        else:
            izq = c + 1
    print('No hay un paciente con ese número de historia clínica')
    print()

def crear_archivo(p):
    global FD
    if len(p) == 0:
        print('No hay datos cargados...')
        print()
        return

    print('Grabando todos los datos en el archivo', FD, '...')
    m = open(FD, 'wb')
    for paciente in p:
        pickle.dump(paciente, m)
    m.close()
    print('... hecho')
    print()

def mostrar_archivo():
    global FD
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe...')
        print()
        return
    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')
    print('Contenido del archivo', FD, '...')
    while m.tell() < tbm:
        pac = pickle.load(m)
        print(to_string(pac))
    m.close()
    print()

def crear_segundo_arreglo():
    global FD
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe...')
        print()
        return
    p2 = []
    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')
    print('Creando el segundo vector desde el archivo', FD, '...')
    while m.tell() < tbm:
        pac = pickle.load(m)
        if pac.cod_problema in [8, 9]:
            p2.append(pac)
    m.close()
    print('... hecho')
    print()
    return p2

def main():
    global FD
    FD = 'pacientes.med'
    p, p2 = [], []
    op = 0
    while op != 9:
        print('Consultorio Dr. Matasanos')
        print(' 1. Registrar pacientes en forma ordenada')
        print(' 2. Listado de pacientes según días de su última visita')
        print(' 3. Buscar un paciente por historia clínica')
        print(' 4. Listado completo de pacientes')
        print(' 5. Creación de un archivo con todos los datos registrados')
        print(' 6. Mostrar el archivo')
        print(' 7. Crear arreglo desde el archivo (código de enfermedad 8 o 9)')
        print(' 8. Mostrar el arreglo (código de enfermedad 8 o 9)')
        print(' 9. Salir')
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()
        if op == 1:
            p = cargar_arreglo_ordenado()
        elif op == 2:
            listado_por_dias(p)
        elif op == 3:
            buscar(p)
        elif op == 4:
            mostrar_arreglo(p, 'Listado completo de pacientes registrados')
        elif op == 5:
            crear_archivo(p)
        elif op == 6:
            mostrar_archivo()
        elif op == 7:
            p2 = crear_segundo_arreglo()
        elif op == 8:
            mostrar_arreglo(p2, 'Pacientes (código de enfermedad 8 o 9)')
        elif op == 9:
            pass

# script principal...
if __name__ == '__main__':
    main()

