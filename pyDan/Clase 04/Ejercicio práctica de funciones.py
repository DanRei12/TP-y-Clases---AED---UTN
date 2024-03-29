'''Desarrollar un programa en Python que permita cargar por teclado un texto completo (analizar dos opciones: una es
cargar todo el texto en una variable de tipo cadena de caracteres y recorrerla con un for iterador; y la otra es cargar
cada caracter uno por uno a través de un while). Siempre se supone que el usuario cargará un punto para indicar el final
 del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:

a) Determinar cuántas palabras tenían más de 4 letras.

b) Determinar cuántas palabras tenían al menos una vez la letra "x" o la letra "y".

c) Determinar el promedio de letras por palabra en todo el texto.

d) Determinar cuántas palabras contuvieron sólo una vez la expresión "mo".

********************************************************************************
Ejemplo: 'el mono momoxy toca el xilofon.'
********************************************************************************
Palabras con más de 4 letras: 2
Palabras tenían al menos una vez la letra "x" o la letra "y": 2
El promedio de letras por palabra en todo el texto es: 4.17
Determinar cuántas palabras contuvieron sólo una vez la expresión "mo": 1'''

def mo (texto):
    cont = 0
    pal4let = 0
    palabra = False
    palabraMo = False
    palabranoMO = False
    xandy = 0
    cantpalabras = 0
    cantletras = 0
    MOs = 0
    for letra in texto:
        if letra == " " or letra == ".":
            cantpalabras += 1

        if (letra != " ") and (letra != ",") and (letra != "."):
            cont += 1
        else:
            cantletras += cont
            cont = 0

        if cont == 5:
            pal4let += 1

        if (letra == " ") or (letra == ",") or (letra == "."):
            palabra = False

        if (palabra == False) and (letra == "x" or letra == "y"):
            xandy += 1
            palabra = True

        if palabraMo == True and letra == "o":
            MOs += 1
            palabranoMO = True
        if letra == "m" and palabranoMO == False:
            palabraMo = True
        else:
            palabraMo = False
        if palabranoMO == True and palabraMo == True:
            MOs -= 1


    prom = cantletras / cantpalabras
    return pal4let, xandy, prom, MOs


texto = input("Insertar el texto a analizar debajo.\n")

pal4let, xandy, prom, MOs = mo(texto)
print ("Las palabras con mas de cuatro letras son:", pal4let)
print ("Las palabras con al menos una letra 'x' o 'y' son:", xandy)
print ("El promedio de letras por palabra son:", prom)
print ("Las palabras con 'mo' son:", MOs)
