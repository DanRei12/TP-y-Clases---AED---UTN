import time
import random
#Empieza el programa
print("Bienvenido a este nuevo programa.\n")
prog = 1
while prog:
    # Elección de nuestras opciones.
    prog = int(input("Selecciona una de las siguientes opciones ingresando el número correspondiente:"
                     "\n""1- Juego de golf (3 jugadores)""\n""2- Diferencia de numeros"
                     "\n""3- Contar cadena de caracteres"
                     "\n""4- Terminar programa\n"
                     "\n""Numerito aqui: "))


    # Opción para el programa 1.
    if prog == 1:

        print("En este juego de golf, usted ingresara el handicap y los dos golpes de 3 jugadores de golf.\n")
        time.sleep(2)

        # Ingresamos los nombres de los jugadores.
        jugador1 = str(input("Ingresar nombre del primer jugador: "))
        time.sleep(2)
        jugador2 = str(input("Ingresar nombre del segundo jugador: "))
        time.sleep(2)
        jugador3 = str(input("Ingresar nombre del tercer jugador: "))
        time.sleep(2)

        # Ingresamos los handicaps
        print("\nAhora indicaremos los handicaps para cada uno.")
        time.sleep(2)
        hand1 = int(input("\nIngrese la cantidad de handicap de " + jugador1 + " (tiene que estar entre 0 y 36)\n"))
        time.sleep(2)
        hand2 = int(input("Ingrese la cantidad de handicap de " + jugador2 + " (tiene que estar entre 0 y 36)\n"))
        time.sleep(2)
        hand3 = int(input("Ingrese la cantidad de handicap de " + jugador3 + " (tiene que estar entre 0 y 36)\n"))
        time.sleep(2)

        # Verificador de error.
        while (hand1 < 0 or hand1 > 36) or (hand2 < 0 or hand2 > 36)  or (hand3 < 0 or hand3 > 36):
            print("Hubo un error en alguno de los handicaps, por favor, ingresarlos nuevamente.")
            hand1 = int(input("Ingrese la cantidad de handicap de " + jugador1 + " (tiene que estar entre 0 y 36)\n"))
            hand2 = int(input("Ingrese la cantidad de handicap de " + jugador2 + " (tiene que estar entre 0 y 36)\n"))
            hand3 = int(input("Ingrese la cantidad de handicap de " + jugador3 + " (tiene que estar entre 0 y 36)\n"))

        # Ingresamos los golpes por cada jugador.
        gr1 = int(input("Ingrese la cantidad de golpes dados por " + jugador1 + "\n"))
        time.sleep(2)
        gr2 = int(input("Ingrese la cantidad de golpes dados por " + jugador2 + "\n"))
        time.sleep(2)
        gr3 = int(input("Ingrese la cantidad de golpes dados por " + jugador3 + "\n"))
        time.sleep(1)

        print("Please stand by.")
        time.sleep(1)
        print("...\n")
        time.sleep(1)

        # Definimos la cantidad de golpes finales por jugador.
        gf1 = gr1 - hand1
        gf2 = gr2 - hand2
        gf3 = gr3 - hand3

        # Definimos el ganador.
        if gf1 < gf2 and gf1 < gf3:
            print("¡¡Felicidades!!", jugador1 + ", ganaste, con un puntaje final de", gf1, "golpes.\n")
            dif1 = gf2 - gf1
            dif2 = gf3 - gf1
            print("Tus diferencias con los demás jugadores son:\n -Diferencia de", dif1, "con", jugador2,
                  "\n -Diferencia de", dif2, "con", jugador3)

        elif gf2 < gf1 and gf2 < gf3:
            print("¡¡Felicidades!!", jugador2 + ", ganaste, con un puntaje final de", gf2, "golpes.\n")
            dif1 = gf1 - gf2
            dif2 = gf3 - gf2
            print("Tus diferencias con los demás jugadores son:\n -Diferencia de", dif1, "con", jugador1,
                  "\n -Diferencia de", dif2, "con", jugador3)

        elif gf3 < gf2 and gf3 < gf1:
            print("¡¡Felicidades!!", jugador3 + ", ganaste, con un puntaje final de", gf3, "golpes.\n")
            dif1 = gf1 - gf3
            dif2 = gf2 - gf3
            print("Tus diferencias con los demas jugadores son:\n -Diferencia de", dif1, "con", jugador1,
                  "\n -Diferencia de", dif2, "con", jugador2)

        # En caso de empate...
        else:
            print("Hubo un milagroso empate muchachos, ustedes se sacaron:\n",
                  jugador1 + ":", gf1, "\n", jugador2 + ":", gf2, "\n", jugador3 + ":", gf3)

        time.sleep(3)
        print("\nBuen juego muchachos.")

    # Opción para el programa 2. (Se eligio la opción "a" del enunciado.)
    elif prog == 2:
        # Empieza el programa.
        print("Aquí ingresara una secuencia de numeros, se calculara el mayor de estos, el menor, y la diferencia entre ambos. \nLa carga termina cuando ingresas 0"
              "(Nota: Puedes usar tanto numeros positivos como negativos.)\n")
        time.sleep(2)

        # Definimos las variables.
        n = int(input("Ingrese su primer número: \n"))
        may = 0
        men = n

        # Ciclos para determinar variables
        while n != 0:
            if n >= may:
                may = n

            if n <= men:
                men = n

            n = int(input("Ingrese otro número:\n"))

        dif = may - men
        print("El número mayor fue", may, "\nEl menor fue", men, "\nY la diferencia entre ambos fue de", dif, "\n")

    # Programa para la opción 3.
    elif prog == 3:
        print("Este programa le permitira ingresar un texto, el mismo determinara los caracteres no "
              "alfanumericos, y se le informara \nla cantidad de estos, y el porcentaje que representan frente al texto.")
        time.sleep(3)

        # Ingresamos nuestro texto.
        texto = str(input("\nIngrese su texto:\n"))
        texto = texto.lower()

        # Definimos las variables.
        caracteres = 0
        no_alfnum = 0

        # Aplicamos el condicional para determinar nuestras variables.
        for i in texto:

            caracteres += 1

            if (i != "0") and (i != "1") and (i != "2") and (i != "3") and (i != "4") and (i != "5") and (i != "6") \
                    and (i != "7") and (i != "8") and (i != "9") and (i != "a") and (i != "á") and (i != "b") \
                    and (i != "c") and (i != "d") and (i != "e") and (i != "é") and (i != "f") and (i != "g") \
                    and (i != "h") and (i != "i") and (i != "í") and (i != "j") and (i != "k") and (i != "l") \
                    and (i != "m") and (i != "n") and (i != "ñ") and (i != "o") and (i != "ó") and (i != "p") \
                    and (i != "q") and (i != "r") and (i != "s") and (i != "t") and (i != "u") and (i != "ú") \
                    and (i != "v") and (i != "w") and (i != "x") and (i != "y") and (i != "z"):

                no_alfnum += 1

        # Sacamos el porcentaje.
        porc = no_alfnum * (100 / caracteres)
        porc = round(porc, 1)
        porc = str(porc)

        # Dictamos los resultados
        time.sleep(3)
        print("La cantidad de caractéres son", caracteres)
        print("La cantidad de no alfanumericos fueron ", no_alfnum)
        time.sleep(2)
        print("Y representó un " + porc + "% del total del texto.\n")


    # Opción para la finalización del programa
    elif prog == 4:
        print("\nPrograma terminado.")
        exit()
    else:
        time.sleep(2)
        print("\n¡¡ERROR!! Volver a ingresar un valor.\n")

    time.sleep(2)
# Fin del programa.
