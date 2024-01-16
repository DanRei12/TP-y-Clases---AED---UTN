'''
Scrip básico para el parcial
def principal():
    contador_letras = contador_palabras = 0

    cadena = input('Ingrese el texto a procesar (Finaliza con "."): ')
    cadena = cadena.lower()

    for car in cadena:
        if car != ' ' and car != '.':
            contador_letras += 1


        else:
            if contador_letras == 0:
                continue
            contador_palabras += 1

            contador_letras = 0

    if contador_palabras > 0:
        print(f'La cantidad de palabras de texto fue: {contador_palabras}')


if __name__ == '__main__':
    principal()
'''

texto = input()
cant_palabras = 0

cant_r = band_car = False
pal_mas_1_digito = 0

letra_ant = None
band_vocal = False
pal_with_voc_and_cons = 0

letra_antPunto3 = None
cont_punto3 = 0
porc_punto3 = "a"

cant_letras_por_palabra = 0
cant_letras = 0
palabra = 0
band_letra_a = False
band_er = False
pos_letra_a = 0
cont_pal_punto4 = 0
cumple_funcion_1 = False
cumple_funcion_2 = False
letraspunto4 = 0
prom_punto4 = 0

texto = texto.lower

for letra in texto:
    if letra == " " or letra == ".":
        cant_palabras += 1

    #Punto 1 (Cantidad de palabras que tuvieron al menos un digito (caracter del 0 al 9) y tambien la letra "r")
    if letra == "r":
        cant_r = True
    elif letra == " " or letra == "." or letra == ",":
        cant_r = False

    if letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5" or letra == "6" or letra == "7" or letra == "8" or letra == "9" or letra == "0":
        band_car = True
    elif letra == " " or letra == "." or letra == ",":
        band_car = False

    if cant_r and band_car:
        pal_mas_1_digito += 1
        band_car = False
        cant_r = False

    #Punto 2 (Porcentaje de palabras (con respecto al total de palabras del texto) que comenzaron con vocal y terminaron en consonante)
    if (letra_ant == " " or letra_ant == None) and (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        band_vocal = True
    if (letra_ant != " " and letra_ant != "a" and letra_ant != "e" and letra_ant != "i" and letra_ant != "o" and letra_ant != "u" and letra_ant != "," and letra_ant != "." and letra_ant != "0" and letra_ant != "1" and letra_ant != "2" and letra_ant != "3" and letra_ant != "4" and letra_ant != "5" and letra_ant != "6" and letra_ant != "7" and letra_ant != "8" and letra_ant != "9") and (letra == " " or letra == "." or letra == ",") and band_vocal:
        pal_with_voc_and_cons += 1
    if letra == " ":
        band_vocal = False

    #Punto 3 (Cantidad de palabras que comenzaron con la misma letra que terminó la palabra anterior.)
    if letra == "," or (letra == " " and letra_ant != ","):
        letra_antPunto3 = letra_ant
    if letra_ant == " " and letra == letra_antPunto3:
        cont_punto3 += 1

    #Punto 4 (Promedio de letras por palabra pero solo de las palabras que tuvieron al menos una "a" en la primera mitad y terminaron en "er")
    if letra != "." and letra != " " and letra != ",":
        cant_letras_por_palabra += 1
        if letra == "a" and band_letra_a == False:
            band_letra_a = True
            pos_letra_a = cant_letras_por_palabra
    else:
        palabra = cant_letras_por_palabra
        cant_letras_por_palabra = 0
        if (pos_letra_a != 0 and palabra != 0) and palabra / 2 >= pos_letra_a and band_letra_a:
            cumple_funcion_1 = True

    if letra_ant == "e" and letra == "r":
        band_er = True
    if (letra == "," or letra == " " or letra == ".") and letra_ant == "r" and band_er:
        cumple_funcion_2 = True
    if cumple_funcion_1 and cumple_funcion_2:
        cont_pal_punto4 += 1
        letraspunto4 += palabra
    if letra == "." or letra == " " or letra == ",":
        band_letra_a = False
        band_er = False
        cumple_funcion_1 = False
        cumple_funcion_2 = False
        pos_letra_a = 0
        palabra = 0

    letra_ant = letra

#Porcentaje punto 2
if pal_with_voc_and_cons != 0:
    porc_punto3 = (pal_with_voc_and_cons * 100) / cant_palabras
    porc_punto3 = str(porc_punto3)

#Promedio punto 4
if letraspunto4 != 0:
    prom_punto4 = letraspunto4 / cont_pal_punto4

print("La cantidad de palabras con 'r' y mas de un digito son:", pal_mas_1_digito)

print("La cantidad de palabras que empiezan con vocal y terminan con consonante son:", pal_with_voc_and_cons)
print("El porcentaje de palabras que empiezan con vocal y terminan con consonante con respecto al total son:", porc_punto3 + "%")

print("La cantidad de palabras que empiezan con la misma letra con la que termino la anterior son:", cont_punto3)

print("La cantidad de letras en palabras con 'a' en la primera mitad y terminan en 'er':", letraspunto4)
print("La cantidad de palabras con 'a' en la primera mitad y terminan en 'er':", cont_pal_punto4)
print("El promedio de letras con respecto a palabras con 'a' en la primera mitad y terminan en 'er':", prom_punto4)
