texto = input("Ingresar aqui su texto: ")
texto = texto.lower()

'''Puntos básicos'''

#Función es_vocal.
def es_vocal(letra):
    return letra in 'aeiouAEIOUáéíóúÁÉÍÓÚüÜ'

#Función es_consonante.
def es_consonante(letra):
    resultado = False
    vocales = 'bcdfghjklmnpqrstvwxyz'
    if letra in vocales:
        resultado = True

    return resultado

#Función es_digito.
def es_digito(digitos):
    return digitos in '0123456789'

#Función cantidad de palabras
def CantPal(text):
    cant_palabras = 0

    for letra in text:
        if letra == "." or letra == " ":
            cant_palabras += 1
    print("La cantidad de palabras en el texto son: ", cant_palabras)
    return cant_palabras

#Función cantidad de letras.
def CantLetras(text):
    cant_letras = 0
    for letra in text:
        if letra != " " and letra != "." and letra != "," and letra != "!" and letra != "¡" and letra != "?" and letra != "¿":
            cant_letras += 1
    return cant_letras

#Función cantidad de vocales.
def CantVoc(text):
    cant_vocales = 0
    for letra in text:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            cant_vocales += 1
    return cant_vocales

#Función cantidad de consonantes.
def CantCons(text):
    cant_consonantes = 0
    for letra in text:
        if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u" and letra != " " and letra != "." and letra != "," and letra != "!" and letra != "¡" and letra != "?" and letra != "¿" and letra != "0" and letra != "1" and letra != "2" and letra != "3" and letra != "4" and letra != "5" and letra != "6" and letra != "7" and letra != "8" and letra != "9":
            cant_consonantes += 1
    return cant_consonantes

'''Dificultad baja'''

#Función promedio de letras por palabra.
def PromLetPorPalabra(text):
    cant_pal = CantPal(text)
    cant_let = CantLetras(text)
    PromLetXPal = cant_let / cant_pal
    print("La cantidad promedio de letras por palabra es:", PromLetXPal)

#Función promedio de vocales por palabra.
def PromVocalesPorPalabra(text):
    cant_pal = CantPal(text)
    cant_voc = CantVoc(text)
    promVocXPal = cant_voc / cant_pal
    print("El promedio de vocales por palabra es de:", promVocXPal)

#Función promedio de consonantes por palabra.
def PromConsPorPalabra(text):
    cant_pal = CantPal(text)
    cant_cons = CantCons(text)
    promConsXPal = cant_cons / cant_pal
    print("El promedio de consonantes por palabra es de:", promConsXPal)

#Función cantidad de palabras que incluyeron alguna letra (en este caso “e”).
def cantPalcon_e(text):
    cant_pal_e = 0
    band_e = False
    for letra in texto:
        if letra == "e":
            band_e = True
        if letra == " " or letra == ".":
            if band_e:
                cant_pal_e += 1
                band_e = False
    print("La cantidad de palabras con alguna 'e' son:", cant_pal_e)
    return cant_pal_e

#Función porcentaje de palabras con alguna consonante.
def PorcPalConCons(text):
    cant_pal = CantPal(text)
    band_consonantes = False
    pal_con_cons = 0
    for letra in text:
        if letra != "a" and letra != "e" and letra != "i" and letra != "o" and letra != "u" and letra != " " and letra != "." and letra != "," and letra != "!" and letra != "¡" and letra != "?" and letra != "¿" and letra != "0" and letra != "1" and letra != "2" and letra != "3" and letra != "4" and letra != "5" and letra != "6" and letra != "7" and letra != "8" and letra != "9":
            band_consonantes = True
        if letra == " " or letra == ".":
            if band_consonantes:
                pal_con_cons += 1
                band_consonantes = False
    porc_pal_cons = pal_con_cons * 100 / cant_pal
    print("El porcentaje de plabras con alguna consonante son:", str(porc_pal_cons) +"%")

#Función cantidad de palabras con exactamente (3) vocales.
def Pal3voc(text):
    cont_voc = 0
    band_voc = False
    cant_pal_3voc = 0
    for letra in text:
        if cont_voc == 3 and band_voc == False:
            cant_pal_3voc += 1
            band_voc = True
        if cont_voc > 3:
            cant_pal_3voc -= 1
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            cont_voc += 1
        if letra == " " or letra == "," or letra == ".":
            cont_voc = 0
            band_voc = False
    print("La cantidad de palabras con 3 vocales exactamente son:", cant_pal_3voc)

#Función porcentaje de palabras con algún digito.
def PorcPalConDig(text):
    cant_pal = CantPal(text)
    cant_pal_dig = 0
    band_dig = False
    for letra in text:
        if letra == "0" or letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5" or letra == "6" or letra == "7" or letra == "8" or letra == "9":
            band_dig = True
        if letra == " " or letra == ".":
            if band_dig:
                cant_pal_dig += 1
                band_dig = False
    if cant_pal_dig != 0:
        porc_pal_dig = cant_pal_dig * 100 / cant_pal
        print("El porcentaje de palabras con digitos es de:", str(porc_pal_dig) +"%")
    else:
        print("Error, no hay digitos.")

#Función cantidad de palabras con mas de (3) caracteres.
def cantPalcon_3car(text):
    carac_por_pal = 0
    cant_pal_3car = 0
    band_pal = True
    for letra in text:
        if letra != "," and letra != " " and letra != ".":
            carac_por_pal += 1
        else:
            carac_por_pal = 0
            band_pal = True
        if carac_por_pal > 3 and band_pal:
            cant_pal_3car += 1
            band_pal = False
    print("La cantidad de palabras con mas de 3 caracteres son:", cant_pal_3car)

'''Dificultad media'''

#Función cantidad de palabras que comienzan con la primera letra de todo el texto. (MALLLLL)
def Pal1letTex_com(text):
    cant_pal_1letTex = 0
    primera_letra = None
    band_1letra = False
    band_pal = True
    for letra in text:
        if band_1letra == False:
            primera_letra = letra
            band_1letra = True
        if letra == primera_letra and band_pal:
            cant_pal_1letTex += 1
        if letra == " ":
            band_pal = True
        else:
            band_pal = False
    print("La cantidad de palabras que empiezan con la primera letra del texto son:", cant_pal_1letTex)

#Función cantidad de palabras que terminan con la primera letra de todo el texto. (MALLLLLLLLLLLL)
def Pal1letTex_ter(text):
    cant_pal_1letTex = 0
    primera_letra = None
    band_1letra = False
    for letra in text:
        if band_1letra == False:
            primera_letra = letra
            band_1letra = True
        if letra != "," and letra != " " and letra != ".":
            ult_let = letra
        elif (letra == " " or letra == "," or letra == ".") and ult_let == primera_letra:
            cant_pal_1letTex += 1
    print("La cantidad de palabras que terminan con la primera letra del texto son:", cant_pal_1letTex)

#Función porcentaje de palabras que incluyen la primera letra del texto.(MALLLLLLLLLLLLLLL)
def PorcPalCon1Let(text):
    cant_pal = CantPal(text)
    band_1letra = False
    primera_letra = None
    cant_pal_1letTex = 0
    band_pal_1letTex = False
    for letra in text:
        if band_1letra == False:
            primera_letra = letra
            band_1letra = True
        if letra == primera_letra and band_pal_1letTex == False:
            cant_pal_1letTex += 1
            band_pal_1letTex = True
        if letra == " ":
            band_pal_1letTex = False
    porc_pal_1letTex = cant_pal_1letTex * 100 / cant_pal
    print("EL porcentaje de palabras que incluyen la primera letra del texto es: "+ str(porc_pal_1letTex) +"%")

#Función cantidad de palabras con "rr"(o cualquier otra silaba).
def cantPalcon_rr(text):
    band_r = False
    band_pal = True
    cant_pal_rr = 0
    for letra in text:
        if letra == " ":
            band_pal = True
        if letra == "r" and band_r and band_pal:
            cant_pal_rr += 1
            band_r = False
            band_pal = False
        if letra == "r":
            band_r = True
        else:
            band_r = False
    print("La cantidad de palabras con 'rr' son:", cant_pal_rr)

#Función posición de la palabra mas larga del texto.
def PosLargTex(text):
    cantlet_pal = 0
    may_cant_let = 0
    cant_pal = 0
    pos_pal_may = 0
    for letra in text:
        if letra != "," and letra != " " and letra != ".":
            cantlet_pal += 1
        elif letra == " " or letra == ".":
            cant_pal += 1
            if cantlet_pal > may_cant_let:
                may_cant_let = cantlet_pal
                pos_pal_may = cant_pal
            cantlet_pal = 0
    print("La palabra mas larga de todo el texto es la palabra nro", pos_pal_may, "con", may_cant_let, "letras.")

'''Dificultad alta'''

#Función cantidad de palabras que tengan "ll" mas de una vez.
def Pal_ll_mas1vez(text):
    band_l = False
    band_ll = False
    cant_ll_mas1vez = 0
    for letra in text:
        if letra == "l" and band_l:
            if band_ll:
                cant_ll_mas1vez += 1
            band_ll = True
        if letra == "l":
            band_l = True
        else:
            band_l = False
        if letra == " ":
            band_l = False
            band_ll = False
    print("La cantidad de palabras con 'll' mas de una vez son:", cant_ll_mas1vez)

#Función cantidad de palabras que incluyen "10" despues de la primera mitad de tu palabra.
def Pal_10_2damitad(text):
    band_1 = False
    band_10 = False
    pos_10 = 0
    cant_pal_10 = 0
    cont_let_por_pal = 0
    for letra in texto:
        if letra != " " and letra != "," and letra != ".":
            cont_let_por_pal += 1
        else:
            if pos_10 > (cont_let_por_pal/2) and band_10:
                cant_pal_10 += 1
            band_1 = False
            band_10 = False
            pos_10 = 0
            cont_let_por_pal = 0
        if letra == "0" and band_1:
            band_10 = True
        if letra == "1":
            band_1 = True
            pos_10 = cont_let_por_pal
    print("La cantidad de palabras con '10' despues de la mitad son:", cant_pal_10)

#Función cantidad de palabras que contienen "u" y terminan en "lo".
def Pal_u_term_lo(text):
    band_u = False
    band_lo = False
    band_term_lo = False
    band_l = False
    cant_u_lo = 0
    for letra in text:
        if (letra == "," or letra == " " or letra == ".") and band_lo:
            band_term_lo = True
        else:
            band_lo = False
        if letra == "o" and band_l:
            band_lo = True
        if letra == "l":
            band_l = True
        else:
            band_l = False
        if letra == "u":
            band_u = True
        if letra == " " or letra == ".":
            if band_u and band_term_lo:
                cant_u_lo += 1
            band_u = False
            band_l = False
            band_lo = False
            band_term_lo = False
    print("La cantidad de palabras con 'u' y terminan en 'lo' son:", cant_u_lo)

#Promedio de letras por palabra pero solo de las palabras que tuvieron al menos una "a" en la primera mitad y terminaron en "er".
def sadsad(text):
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
    letra_ant = None
    for letra in text:
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
    print("La cantidad de letras en palabras con 'a' en la primera mitad y terminan en 'er':", letraspunto4)
    print("La cantidad de palabras con 'a' en la primera mitad y terminan en 'er':", cont_pal_punto4)
    print("El promedio de letras con respecto a palabras con 'a' en la primera mitad y terminan en 'er':", prom_punto4)
#Verificar las funciones.

PromLetPorPalabra(texto)
PromVocalesPorPalabra(texto)
PromConsPorPalabra(texto)
cantPalcon_e(texto)
PorcPalConCons(texto)
Pal3voc(texto)
PorcPalConDig(texto)
cantPalcon_3car(texto)

Pal1letTex_com(texto)
PorcPalCon1Let(texto)
Pal1letTex_ter(texto)
cantPalcon_rr(texto)
PosLargTex(texto)

Pal_ll_mas1vez(texto)
Pal_10_2damitad(texto)
Pal_u_term_lo(texto)
