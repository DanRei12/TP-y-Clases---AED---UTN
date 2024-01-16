import io
import os.path
import pickle

__author__ = 'Catedra de AED'
class Votante:
    def __init__(self, dn, nom, ed, sex):
        self.dni = dn
        self.nombre = nom
        self.edad = ed
        self.sexo = sex

def to_string(vot):
    sx = 'Hombre'
    if vot.sexo == 'm':
        sx = 'Mujer'
    r = ''
    r += '{:<20}'.format('DNI: ' + str(vot.dni))
    r += '{:<30}'.format('Nombre: ' + vot.nombre)
    r += '{:<20}'.format('Edad: ' + str(vot.edad))
    r += '{:<20}'.format('Sexo: ' + sx)
    return r

def validar_dni(lim):
    n = lim - 1
    while n <= lim:
        n = int(input('Valor mayor a ' + str(lim) + ' por favor: '))
        if n <= lim:
            print('\t\tError... cargue de nuevo...')
    return n

def validar_edad(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Entre ' + str(inf) + ' y ' + str(sup) + ': '))
        if n < inf or n > sup:
            print('Error... cargue de nuevo...')
    return n

def validar_sexo(caracteres):
    c = ' '
    while c not in caracteres:
        c = input('Letras válidas ' + str(caracteres) + ': ')
        if c not in caracteres:
            print('\t\tError... letra no válida... cargue de nuevo...')
    return c

def buscar(m, dni):
    global FD1
    t = os.path.getsize(FD1)
    fp_inicial = m.tell()
    m.seek(0, io.SEEK_SET)
    posicion = -1
    while m.tell() < t:
        fp = m.tell()
        vot = pickle.load(m)
        if vot.dni == dni:
            posicion = fp
            break
    m.seek(fp_inicial, io.SEEK_SET)
    return posicion

def cargar_archivo():
    global FD1
    m = open(FD1, 'a+b')
    print()
    print('DNI del votante a registrar (cargue 0 para salir): ')
    dni = validar_dni(-1)
    while dni != 0:
        # buscamos el registro con ese legajo...
        pos = buscar(m, dni)
        if pos == -1:
            # no estaba repetido... lo cargamos por teclado...
            nom = input('Nombre: ')
            print('Edad...')
            edad = validar_edad(0, 120)
            print('Sexo ("v": varón - "m": mujer)...')
            sex = validar_sexo(['V', 'v', 'M', 'm'])
            vot = Votante(dni, nom, edad, sex)
            # ...lo grabamos...
            pickle.dump(vot, m)
            # ...volcamos el buffer de escritura
            # para que el sistema operativo REALMENTE
            # grabe en disco el registro...
            m.flush()
            print('Registro grabado en el archivo...')
        else:
            print('DNI repetido... alta rechazada...')
        print()
        print('Otro dni de votante a registrar (cargue 0 para salir): ')
        dni = validar_dni(-1)
    m.close()
    print()

def mostrar_archivo(FD):
    if not os.path.exists(FD):
        print('El archivo', FD, 'no existe...')
        print()
        return
    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')
    print('Contenido del archivo', FD, '...')
    while m.tell() < tbm:
        vot = pickle.load(m)
        print(to_string(vot))
    m.close()
    print()

def buscar_votante():
    global FD1
    if not os.path.exists(FD1):
        print('El archivo', FD1, 'no existe...')
        print()
        return
    print()
    m = open(FD1, 'rb')
    print('DNI del votante a buscar: ')
    dni = validar_dni(0)
    pos = buscar(m, dni)
    if pos != -1:
        m.seek(pos, io.SEEK_SET)
        vot = pickle.load(m)
        print('Votante encontrado,..')
        print(to_string(vot))
    else:
        print('Ese votante no está registrado...')
    m.close()
    print()

def cantidad_por_sexo():
    global FD1
    if not os.path.exists(FD1):
        print('El archivo', FD1, 'no existe...')
        print()
        return
    print()
    tbm = os.path.getsize(FD1)
    m = open(FD1, 'rb')
    cv, cm = 0, 0
    while m.tell() < tbm:
        vot = pickle.load(m)
        if vot.sexo == 'v':
            cv += 1
        else:
            cm += 1
    m.close()
    print('Cantidad de votantes varones:', cv)
    print('Cantidad de votantes mujeres:', cm)
    print()

def crear_segundo_archivo():
    global FD1
    if not os.path.exists(FD1):
        print('El archivo', FD1, 'no existe...')
        print()
        return
    tbm = os.path.getsize(FD1)
    m = open(FD1, 'rb')
    s = open(FD2, 'wb')
    print('Creando archivo', FD2, 'con mayores a 70 años...')
    while m.tell() < tbm:
        vot = pickle.load(m)
        if vot.edad > 70:
            pickle.dump(vot, s)
    m.close()
    s.close()
    print('... hecho')
    print()

def main():
    global FD1, FD2
    FD1 = 'votantes.vot'
    FD2 = 'mayores.vot'
    op = 0
    while op != 7:
        print('Padrón electoral')
        print(' 1. Registrar votantes en el padrón')
        print(' 2. Listado de votantes')
        print(' 3. Buscar un votante por dni')
        print(' 4. Cantidad de varones y mujeres')
        print(' 5. Crear archivo con votantes mayores a 70 años')
        print(' 6. Mostrar el archivo de votantes mayores a 70 años')
        print(' 7. Salir')
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()
        if op == 1:
            cargar_archivo()
        elif op == 2:
            mostrar_archivo(FD1)
        elif op == 3:
            buscar_votante()
        elif op == 4:
            cantidad_por_sexo()
        elif op == 5:
            crear_segundo_archivo()
        elif op == 6:
            mostrar_archivo(FD2)
        elif op == 7:
            pass
# script principal...
if __name__ == '__main__':
    main()


