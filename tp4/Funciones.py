import os.path
import io
class Libro:
    def __init__(self, tit="", rev=0, yer=0, idiom=0, rat=0, cod=0):
        self.Titulo = tit
        self.Revisiones = rev
        self.Year = yer
        self.Idioma = idiom
        self.Rating = rat
        self.ISBN = cod

def add_in_order(vec1, libro):
    n = len(vec1)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if vec1[c].ISBN == libro.ISBN :
            pos = c
            break
        if libro.ISBN < vec1[c].ISBN:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vec1[pos:pos] = [libro]

def carg_arreglo_in_order():
    vec1 = []
    m = open("libros.csv", mode="rt", encoding="utf8")
    flag = False

    for libro in m:
        if flag:
            libro = libro[:-1]
            token = libro.split(",")
            libro = Libro(token[0], int(token[1]), int(token[2]), int(token[3]), float(token[4]), token[5])
            add_in_order(vec1, libro)
        flag = True

    print("\nCarga generada correctamente.\n")
    input()
    for i in vec1:
        print(to_string(i))
    m.close()
    return vec1

def to_string(libro):
    r = ""
    r += "{:<20}".format("Título: " + libro.Titulo)
    r += "{:<30}".format(" - Revisiones: " + str(libro.Revisiones))
    r += "{:<20}".format(" - Año: " + str(libro.Year))
    r += "{:<20}".format(" - Idioma: " + str(libro.Idioma))
    r += "{:<20}".format(" - Rating: " + str(libro.Rating))
    r += "{:<20}".format(" - ISBN: " + libro.ISBN)
    return r

def buscar(reg):
    opc = int(input("¿Quiere busqueda por titulo o ISBN?\n1- Titulo\n2- ISBN\nIngresar su elección: "))
    while opc != 0:
        if opc == 1:
            tit = input("Ingresar el titulo a buscar: ")
            band_buscar = False

            for i in range(len(reg)):
                if reg[i].Titulo == tit:
                    print("Se ha encontrado un título similar, el siguiente: ")
                    print(to_string(reg[i]))
                    reg[i].Revisiones += 1
                    print("Revisión sumada")
                    band_buscar = True
                    return reg

            if band_buscar == False:
                print("No se han encontrado libros con ese título.")

        elif opc == 2:
            cod = input("Ingresar el ISBN a buscar: ")
            band_buscar = False

            for i in range(len(reg)):
                if reg[i].ISBN == cod:
                    print("Se ha encontrado un ISBN similar, el siguiente: ")
                    print(to_string(reg[i]))
                    reg[i].Revisiones += 1
                    print("Revisión sumada")
                    band_buscar = True
                    return reg

            if band_buscar == False:
                print("No se han encontrado libros con ese ISBN.")
        else:
            print("Error, nuevamente...")
            op = input("¿Quiere busqueda por titulo o ISBN?(1- Titulo\n2- ISBN)\nIngresar su elección: ")

    return reg

def may_revs(reg):
    flag = False
    for lib in reg:
        if flag:
            if lib.Revisiones > mayor.Revisiones:
                mayor = lib
        if not flag:
            mayor = lib
            flag = True
    print("El libro con mayor cantidad de revisiones es el siguiente: ")
    print(to_string(mayor))

def gen_matriz(reg):
    if len(reg) == 0:
        print('No hay datos cargados...')
        print()
        return

    cf, cc = 27, 21
    matriz = [cc*[0] for f in range(cf)]

    for lib in reg:
        if lib.Year >= 2000:
            f = lib.Idioma - 1
            c = lib.Year - 2000
            if not matriz[f][c]:
                matriz[f][c] = lib
            else:
                if matriz[f][c].Rating <= lib.Rating:
                    matriz[f][c] = lib
                else:
                    pass
    print("Matriz generada correctamente.")
    return matriz

def pub_dec(reg):
    cont = [0] * 10
    d = 1900
    cont_may = 0
    dec_may = 0
    for lib in reg:
        if 1910 >= lib.Year >= 1900:
            cont[0] += 1
        if 1920 >= lib.Year >= 1910:
            cont[1] += 1
        if 1930 >= lib.Year >= 1920:
            cont[2] += 1
        if 1940 >= lib.Year >= 1930:
            cont[3] += 1
        if 1950 >= lib.Year >= 1940:
            cont[4] += 1
        if 1960 >= lib.Year >= 1950:
            cont[5] += 1
        if 1970 >= lib.Year >= 1960:
            cont[6] += 1
        if 1980 >= lib.Year >= 1970:
            cont[7] += 1
        if 1990 >= lib.Year >= 1980:
            cont[8] += 1
        if 2000 >= lib.Year >= 1990:
            cont[9] += 1
    print("Los libros publicados por decada son los siguientes: ")

    for c in cont:
        if c != 0:
            print("\nEntre los años", d, "y los años", d+10, "la cantidad de libros publicados fue de", c)
            if c > cont_may:
                cont_may = c
                dec_may = d
        d += 10
    print("\nEn la decada en la que mas publicaciones hubieron fue en la de", dec_may, "hasta el año", dec_may+10, "con", cont_may, "publicaciones.\n")
