import os.path
import io
import pickle

#Listas con generos e idiomas.
generos = ["Balada", "Pop", "Rock", "Folclore", "Electrónica", "Otros"]
idiomas = ["Español", "Inglés", "Francés", "Portugués", "Otros"]

#Definición de la clase Tema
class Tema:
    def __init__(self, Titulo="", Genero=0, Idioma=0):
        self.Titulo = Titulo
        self.Genero = Genero
        self.Idioma = Idioma


    def __str__(self):
        cad = "Título: {:<15} Género: {:<30} Idioma:{:>3} "
        cad = cad.format(self.Titulo, self.Genero, self.Idioma)
        return cad

#Función de validación, mayor que...
def validar_mayor(lim):
    n = lim - 1
    while n <= lim:
        n = int(input("Valor mayor a " + str(lim) + " por favor: "))
        if n <= lim:
            print("\t\tError... se pidio mayor a", lim, "... cargue de nuevo...")
    return n


#Función de validación, entre los...
def validar_intervalo(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input("Valor entre " + str(inf) + " y " + str(sup)+ " por favor: "))
        if n < inf or n > sup:
            print("\t\tError... se pidió entre", inf, "y", sup, "... cargue de nuevo...")
    return n

#Función para búsqueda binaria
def busq_bin(vec, tit):
    n = len(vec)
    new_vec = []
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2

        if vec[c].Titulo == tit:
            new_vec.append(vec[c])
            return new_vec

        if tit < vec[c].Titulo:
            der = c - 1
        else:
            izq = c + 1

    return -1

#Función para generar vector con orden por titulo
def add_in_order(vec, tema):
    n = len(vec)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if vec[c].Titulo == tema.Titulo:
            pos = c
            break
        if tema.Titulo < vec[c].Titulo:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vec[pos:pos] = [tema]

#Función para cargar arreglo del archivo.
def carg_arreglo_in_order():
    if not os.path.exists("musica.csv"):
        print("El archivo musica.csv aún no existe. Por favor ejecutar primero ese módulo.\n")
        input()
        return []
    vec = []
    m = open("musica.csv", mode="rt", encoding="utf8")

    for tema in m:
        tema = tema[:-1]
        token = tema.split(",")
        tema = Tema(token[0], int(token[1]), int(token[2]))
        add_in_order(vec, tema)

    print("\nCarga generada correctamente.\n")
    m.close()
    input()

    to_string(vec)
    input()
    return vec

#Función para leer los registros de un vector.
def to_string(vec):
    for i in range(len(vec)):
        r = ""
        r += "{:<20}".format("Título: " + vec[i].Titulo)
        r += "{:<30}".format(" - Género: " + generos[vec[i].Genero])
        r += "{:<20}".format(" - Idioma: " + idiomas[vec[i].Idioma])
        print(r)

#Función busqueda mediante cantidad de temas e idioma.
def temaeidioma(vec):
    if len(vec) == 0:
        print("No hay datos cargados aún, por favor ejecutar opción 1 primero")
        print()
        return

    print("A continuacion ingresara el numero del idioma a buscar.")
    print("IDIOMAS: \n 0 - Español \n 1 - Inglés \n 2 - Francés \n 3 - Portugués \n 4 - Otros")
    i = validar_intervalo(0, 4)

    print("A continuacion ingresara el numero de temas de ese idioma a mostrar.")
    n = validar_mayor(0)

    new_vec = []
    cont = 0

    for tema in vec:
        if tema.Idioma == i:
            new_vec.append(tema)
            cont += 1

        if cont == n:
            to_string(new_vec)
            return new_vec

    if cont < n:
        print("\nNo se han logrado encontrar la cantidad de temas pedidos")
        input()
        print("Cantidad de temas encontrados:", cont, "\n")
        input()
        to_string(new_vec)
        return new_vec

#Generación de matriz
def matriz_conteo(vec):
    if len(vec) == 0:
        print("No hay datos cargados aún, por favor ejecutar opción 1 primero")
        print()
        return []

    cf, cc = 6, 5
    matriz = [cc*[0] for f in range(cf)]

    for tema in vec:
        f = tema.Genero
        c = tema.Idioma
        matriz[f][c] += 1

    print("Cantidad de temas por género e idioma:")
    for f in range(cf):
        for c in range(cc):
            if matriz[f][c] != 0:
                print("Género: " + generos[f] + " - Idioma: " + idiomas[c] + " - Cantidad de temas: ", matriz[f][c])
    return matriz

#Mostrar cantidad de género teniendo en cuenta la matriz.
def busc_gen(matriz):
    if len(matriz) == 0:
        print("No hay datos matriz cargados aún, por favor ejecutar opción 3 primero")
        print()
        return

    print("A continuación ingresará el género a buscar.")
    print("GÉNEROS: \n 0 - Balada \n 1 - Pop \n 2 - Rock \n 3 - Folclore \n 4 - Electrónica \n 5 - Otros")
    n = validar_intervalo(0, 5)
    total = 0

    for i in range(len(matriz[n])):
        total += matriz[n][i]

    print("La cantidad de temas del género " + generos[n] + " es de", total)

#Buscar un tema por su titulo en el vector.
def busc_title(vec):
    if len(vec) == 0:
        print("No hay datos cargados aún, por favor ejecutar opción 1 primero")
        print()
        return

    title = input("Ingresar el nombre del tema a buscar: ")
    new_vec = []
    resp = busq_bin(vec, title)
    if resp == -1:
        print("No se ha encontrado el tema solicitado.")
        input()
    else:
        print("Se ha encontrado el tema solicitado: ")
        to_string(resp)

#Generar archivo binario para idioma especifico.
def gen_bin_arch(vec):
    if len(vec) == 0:
        print("No hay datos cargados aún, por favor ejecutar opción 1 primero")
        print()
        return

    print("A continuacion ingresara el numero del idioma a ingresar en el archivo.")
    print("IDIOMAS: \n 0 - Español \n 1 - Inglés \n 2 - Francés \n 3 - Portugués \n 4 - Otros")
    i = validar_intervalo(0, 4)

    FD = "MusicaIdioma" + str(i) + ".dat"

    m = open(FD, "w+b")
    for tema in vec:
        if tema.Idioma == i:
            pickle.dump(tema, m)

    m.close()
    print("Archivo generado correctamente.")

#Comprobar o generar archivo binario para idioma determinado.
def comp_arch(vec):
    print("A continuacion ingresara el numero del idioma a comprobar si existe para el archivo.")
    print("IDIOMAS: \n 0 - Español \n 1 - Inglés \n 2 - Francés \n 3 - Portugués \n 4 - Otros")
    i = validar_intervalo(0, 4)

    FD = "MusicaIdioma" + str(i) + ".dat"
    flag = show_archive(FD)
    if not flag:
        m = open(FD, "a+b")
        for tema in vec:
            if tema.Idioma == i:
                pickle.dump(tema, m)
        m.close()
    else:
        return

    print("Dado a que no existe, se procede a generar un archivo.\nArchivo generado correctamente.")
    input()

#Mostrar contenido del archivo binario.
def show_archive(FD):
    vec = []
    if not os.path.exists(FD):
        print("El archivo", FD, "aun no existe.\n")
        return False

    tbm = os.path.getsize(FD)
    m = open(FD, 'rb')

    print("Contenido de el archivo", FD, "\n")
    while m.tell() < tbm:
        registro = pickle.load(m)
        vec.append(registro)

    print(to_string(vec))

    m.close()
    return True
