def Punto1(texto):
    cant_r = band_car = False
    pal_mas_1_digito = 0
    for letra in texto:
        #Punto 1
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
    return pal_mas_1_digito
texto = input()
cant_palabras = 0

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

texto.lower

pal_mas_1_digito = Punto1(texto)
print("La cantidad de palabras con 'r' y mas de un digito son:", pal_mas_1_digito)
