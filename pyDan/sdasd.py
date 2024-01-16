def PalMas4Let (letra, cont_let, cont_palabras_4letras, band_cont_let, cont_let_palabra):
    if (letra != ".") and (letra != ",") and (letra != " ") and (letra != "!") and (letra != "¡") and (letra != "?") and (letra != "¿"):
        band_cont_let = True
        cont_let += 1
        cont_let_palabra += 1
    else:
        band_cont_let = False
        cont_let_palabra = 0

    if cont_let_palabra == 4 and band_cont_let == True:
        cont_palabras_4letras += 1
        cont_let_palabra = 0

    return cont_palabras_4letras, cont_let
def XandY (letra, band_xy, cont_xy):
    if (letra == "x") or (letra == "y") and band_xy == False:
        cont_xy += 1
        band_xy = True

    if (letra == ".") or (letra == ",") or (letra == " "):
        band_xy = False

    return cont_xy
def PromLet (letra, cont_palabras, band_punto):
    if (letra == " ") or (letra == ".") and band_punto == True:
        cont_palabras += 1
        band_punto = False
    else:
        band_punto = True

    return cont_palabras
def mo (letra, band_m, cant_pal_mo, cant_pal_mo1vez):
    if letra == " " or letra == "." or letra == "," and cant_pal_mo == 1:
        cant_pal_mo = 0
        cant_pal_mo1vez += 1
    elif letra == " " or letra == "." or letra == "," and cant_pal_mo != 1:
        cant_pal_mo = 0

    if letra == "m":
        band_m = True
    else:
        band_m = False

    if letra == "o" and band_m == True:
        cant_pal_mo += 1

    return cant_pal_mo1vez

opt = 1
while opt:
    print("\n1 - Cargar texto de manera completa."
          "\n2 - Cargar texto caracter por caracter."
          "\n3 - Terminar programa")

    opt = int(input("Ingresar aqui la opción a seleccionar: "))

    if opt == 1:
        texto = input("Ingresar abajo el texto a procesar.\n")
        texto.lower()
        cont_let = 0
        band_cont_let = False
        cont_palabras_4letras = 0
        cont_let_palabra = 0


        band_xy = False
        cont_xy = 0

        cont_palabras = 0
        band_punto = True

        band_m = False
        cant_pal_mo = 0
        cant_pal_mo1vez = 0

        for letra in texto:

            #Punto 1
            PalMas4Let(letra, cont_let, band_cont_let, cont_palabras_4letras, cont_let_palabra)
            cont_palabras_4letras, cont_let = PalMas4Let(letra, cont_let, band_cont_let, cont_palabras_4letras, cont_let_palabra)

            #Punto 2
            XandY(letra, band_xy, cont_xy)
            cont_xy = XandY(letra, band_xy, cont_xy)

            #Punto 3
            PromLet(letra, cont_palabras, band_punto)
            cont_palabras = PromLet(letra, cont_palabras, band_punto)

            #Punto 4
            mo(letra, band_m, cant_pal_mo, cant_pal_mo1vez)
            cant_pal_mo1vez = mo(letra, band_m, cant_pal_mo, cant_pal_mo1vez)

        prom = cont_let / cont_palabras
        prom = round(prom, 3)

        print("Palabras con más de 4 letras:", cont_palabras_4letras,
        "\nPalabras tenían al menos una vez la letra 'x' o la letra 'y':", cont_xy,
        "\nEl promedio de letras por palabra en todo el texto es:", prom,
        "\nDeterminar cuántas palabras contuvieron sólo una vez la expresión 'mo':", cant_pal_mo1vez)

    elif opt == 2:
        letra = str(input("Ingresar su letra (posteriormente al ingreso de la primera letra, seguir ingresando cada una, el proceso terminara con el ingreso de '0')"))
        band_cont_let = False
        cont_let = 0
        cont_palabras_4letras = 0
        band_xy = False
        cont_xy = 0
        cont_palabras = 0
        band_punto = True
        band_m = False
        cant_pal_mo = 0
        cant_pal_mo1vez = 0

        while letra != 0:

            #Problema 1
            if (letra != ".") or (letra != ",") or (letra != " ") or (letra != "!") or (letra != "¡") or (letra != "?") or (letra != "¿"):
                band_cont_let = True
                cont_let += 1
            else:
                band_cont_let = False
                #cont_let = 0

            if cont_let % 4 == 0 and band_cont_let == True:
                cont_palabras_4letras += 1
                #cont_let = 0

            #Problema 2
            if (letra == "x") or (letra == "y") and band_xy == False:
                cont_xy += 1
                band_xy = True

            if (letra == ".") or (letra == ",") or (letra == " "):
                band_xy = False

            #Problema 3
            if (letra == " ") or (letra == ".") and band_punto == True:
                cont_palabras += 1
                band_punto = False
            else:
                band_punto = True

            prom = cont_let / cont_palabras
            prom = round(prom, 3)

            #Problema 4
            if letra == " " or letra == "." or letra == "," and cant_pal_mo == 1:
                cant_pal_mo = 0
                cant_pal_mo1vez += 1
            elif letra == " " or letra == "." or letra == "," and cant_pal_mo != 1:
                cant_pal_mo = 0

            if letra == "m":
                band_m = True
            else:
                band_m = False

            if letra == "o" and band_m == True:
                cant_pal_mo += 1

    elif opt == 3:
            print("Usted decidió terminar con el programa. Hasta la próxima"
                  "\nPresione enter para terminar")
            input()
            exit()

    else:
        print("Error, opción invalida, responder nuevamente.")
