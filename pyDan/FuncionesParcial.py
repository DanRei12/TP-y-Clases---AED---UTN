while (pun1 < x) or (pun2 < x):
    cant_de_jug += 1
    print("-" * 90)
    print("\t\tRonda Nro", cant_de_jug)
    print("-" * 90)
    time.sleep(2)

    #MENU DE OPCIONES PARA EL PRIMER JUGADOR.
    print(jug_1,"Seleccione alguna de las opciones:\n"
            "1 - Par.\n"
            "2 - Impar.\n")
    op1 = int(input("Elija una opción (1 o 2): "))
    time.sleep(1)

    #SE DETECTA CUÁL OPCIÓN ELIGIÓ Y SE CAMBIA EL VALOR DE val1 DEPENDIENDO LA RESPUESTA.
    if op1 == 1:
        print("¡", jug_1, ", has seleccionado PAR!", random.choice(caritasf))
        val1 = True

    elif op1 == 2:
        print("¡", jug_1, ", has seleccionado IMPAR!", random.choice(caritasf))
        val1 = False

    #EN CASO DE ESCRIBIR UNA OPCIÓN NO VÁLIDA, SE PIDE NUEVAMENTE LA OPCIÓN.
    while (op1 < 1) and (op1 > 2):
        print("La opción elegida no es válida", random.choice(caritase))
        op1 = int(input("Ingresar abajo nuevamente su opción (1 para par ; 2 para impar).\n"))
    time.sleep(1)

    #SE LLAMA A LA FUNCIÓN "dados" Y SE ESTABLECEN LOS VALORES.
    dad1, dad2, dad3, may, men = dados(dad1, dad2, dad3, may, men)

    #SE MUESTRAN LOS VALORES PARA QUE LOS JUGADORES PUEDAN HACER LA SUMA
    #CONFIRMANDO ASÍ LO CALCULADO POR EL PROGRAMA.

    print("Los resultados de tus dados son:")

    print("Dado 1:", dad1)
    time.sleep(1)

    print("Dado 2:", dad2)
    time.sleep(1)

    print("Dado 3:", dad3)
    time.sleep(1)

    #-----------------------------------------------------------------------------------------------------------

    #VERIFICADORES Y ALGORITMO DE LA RONDA PARA EL PRIMER JUGADOR (EN CASO DE SELECCIONAR LA OPCION 1: PAR).

    if val1 == True:

        print(jug_1, "Tira los dados y busca la sumatoria de números → PARES ←")
        time.sleep(1)

        #SE VERIFICA QUE LA SUMA DE LOS DADOS SEA DIVISIBLE POR 2 Y DE 0, CONFIRMANDO QUE EL NÚMERO ES PAR.
        if (dad1 + dad2 + dad3) % 2 == 0:

            aciertos_jug_1 += 1


            print("La sumatoria de los dados es PAR!", random.choice(caritasf))
            time.sleep(1)

            punt_ronda_jug_1 = may

            #EN EL CASO DE QUE TODOS LOS NÚMEROS SEAN PARES,
            #SE APLICA LA REGLA DEL JUEGO, EN DONDE SE MULTIPLICA EL PUNTAJE POR DOS.
            if ((dad1 % 2) == 0) and ((dad2 % 2) == 0) and ((dad3 % 2) == 0):

            punt_ronda_jug_1 = may * 2

            print("Y los dados también son PARES!\n", random.choice(caritasf))

    else:

        #SI LA SUMA DE LOS DADOS ES IMPAR, SE RESTA EL MENOR.
        print("La sumatoria de los dados es IMPAR!", random.choice(caritast))

        punt_ronda_jug_1 -= men


#-----------------------------------------------------------------------------------------------------------

    #VERIFICADORES Y ALGORITMO DE LA RONDA PARA EL PRIMER JUGADOR (EN CASO DE SELECCIONAR LA OPCION 2: IMPAR).

    #SE VERIFICA QUE EL VALOR DE val1 SEA FALSO, ES DECIR, QUE SE HAYA SELECCIONADO LA SEGUNDA OPCION.
    if val1 == False:

        aciertos_jug_1 += 1

        print(jug_1,"Tira los dados y busca la sumatoria de números → IMPARES ←")
        time.sleep(1)

        #SE VERIFICA QUE LA SUMA DE LOS DADOS, AL DIVIRSE POR 2, NO SEA 0. ES DECIR, QUE SEA IMPAR.
        if (dad1 + dad2 + dad3) % 2 != 0:

            print("La sumatoria de los dados es IMPAR!", random.choice(caritasf))
            time.sleep(1)

            punt_ronda_jug_1 = may

                #EN EL CASO DE QUE TODOS LOS NÚMEROS SEAN IMPARES,
                #SE APLICA LA REGLA DEL JUEGO, EN DONDE SE MULTIPLICA EL PUNTAJE POR DOS.
                if ((dad1 % 2) != 0) and ((dad2 % 2) != 0) and ((dad3 % 2) != 0):

                punt_ronda_jug_1 = may * 2

                print("Y los dados también son IMPARES!\n", random.choice(caritasf))

        else:

            #SI LA SUMA DE LOS DADOS ES PAR, SE RESTA EL MENOR.
            print("La sumatoria de los dados es PAR!", random.choice(caritasf))

            punt_ronda_jug_1 -= men

    time.sleep(1)
    pun1 += punt_ronda_jug_1


#-----------------------------------------------------------------------------------------------------------

    #LO MISMO OCURRE PARA EL JUGADOR 2.

    print("■■■■■■■■■■■■■■■■")
    print(jug_2,"\n1 - Par.\n"        #MENU PARA EL SEGUNDO JUGADOR.
            "2 - Impar.\n")
    op2 = int(input("Elija una opción (1 o 2): "))
    time.sleep(1)

    #SE DETECTA CUÁL OPCIÓN ELIGIÓ Y SE CAMBIA EL VALOR DE val2 DEPENDIENDO LA RESPUESTA.
    if op2 == 1:
        print("¡", jug_2, ", has seleccionado PAR!", random.choice(caritasf))
        val2 = True

    elif op2 == 2:
        print("¡", jug_2, ", has seleccionado IMPAR!", random.choice(caritasf))
        val2 = False

    #EN CASO DE ESCRIBIR UNA OPCIÓN NO VÁLIDA, SE PIDE NUEVAMENTE LA OPCIÓN.
    while (op2 < 1) and (op2 > 2):
        print("La opción elegida no es válida", random.choice(caritase))
        op1 = int(input("Ingresar abajo nuevamente su opción (1 para par ; 2 para impar).\n"))
    time.sleep(1)

    #SE LLAMA A LA FUNCIÓN "dados" Y SE ESTABLECEN LOS VALORES.
    dad1, dad2, dad3, may, men = dados(dad1, dad2, dad3, may, men)

    #SE MUESTRAN LOS VALORES PARA QUE LOS JUGADORES PUEDAN HACER LA SUMA
    #CONFIRMANDO ASÍ LO CALCULADO POR EL PROGRAMA.

    print("Los resultados de tus dados son:")

    print("Dado 1:", dad1)
    time.sleep(1)

    print("Dado 2:", dad2)
    time.sleep(1)

    print("Dado 3:", dad3)
    time.sleep(1)

    #-----------------------------------------------------------------------------------------------------------

    #VERIFICADORES Y ALGORITMO DE LA RONDA PARA EL SEGUNDO JUGADOR (EN CASO DE SELECCIONAR LA OPCION 1: PAR).

    if val2 == True:

        print(jug_2, "Tira los dados y busca la sumatoria de números → PARES ←")
        time.sleep(1)

        #SE VERIFICA QUE LA SUMA DE LOS DADOS SEA DIVISIBLE POR 2 Y DE 0, CONFIRMANDO QUE EL NÚMERO ES PAR.
        if (dad1 + dad2 + dad3) % 2 == 0:

            aciertos_jug_2 += 1

            print("La sumatoria de los dados es PAR!", random.choice(caritasf))
            time.sleep(1)

            punt_ronda_jug_2 = may

            #EN EL CASO DE QUE TODOS LOS NÚMEROS SEAN PARES,
            #SE APLICA LA REGLA DEL JUEGO, EN DONDE SE MULTIPLICA EL PUNTAJE POR DOS.
            if ((dad1 % 2) == 0) and ((dad2 % 2) == 0) and ((dad3 % 2) == 0):

            punt_ronda_jug_2 = may * 2

            print("Y los dados también son PARES!\n", random.choice(caritasf))

    else:

        #SI LA SUMA DE LOS DADOS ES IMPAR, SE RESTA EL MENOR.
        print("La sumatoria de los dados es IMPAR!", random.choice(caritast))

        punt_ronda_jug_2 -= men


#-----------------------------------------------------------------------------------------------------------

    #VERIFICADORES Y ALGORITMO DE LA RONDA PARA EL SEGUNDO JUGADOR (EN CASO DE SELECCIONAR LA OPCION 2: IMPAR).

    #SE VERIFICA QUE EL VALOR DE val2 SEA FALSO, ES DECIR, QUE SE HAYA SELECCIONADO LA SEGUNDA OPCION.
    if val2 == False:

        aciertos_jug_2 += 1

        print(jug_2,"Tira los dados y busca la sumatoria de números → IMPARES ←")
        time.sleep(1)

        #SE VERIFICA QUE LA SUMA DE LOS DADOS, AL DIVIRSE POR 2, NO SEA 0. ES DECIR, QUE SEA IMPAR.
        if (dad1 + dad2 + dad3) % 2 != 0:

            print("La sumatoria de los dados es IMPAR!", random.choice(caritasf))
            time.sleep(1)

            punt_ronda_jug_2 = may

            #EN EL CASO DE QUE TODOS LOS NÚMEROS SEAN IMPARES,
            #SE APLICA LA REGLA DEL JUEGO, EN DONDE SE MULTIPLICA EL PUNTAJE POR DOS.
            if ((dad1 % 2) != 0) and ((dad2 % 2) != 0) and ((dad3 % 2) != 0):

                punt_ronda_jug_2 = may * 2

                print("Y los dados también son IMPARES!\n", random.choice(caritasf))

        else:

            #SI LA SUMA DE LOS DADOS ES PAR, SE RESTA EL MENOR.
            print("La sumatoria de los dados es PAR!", random.choice(caritasf))

            punt_ronda_jug_2 -= men

    time.sleep(1)
    pun2 += punt_ronda_jug_2

    print("En esta ronda nro", cant_de_jug, ":", jug_1, "consiguió", punt_ronda_jug1, "puntos. Un total de", pun1, "por ahora.")
    print("Y", jug_2, "consiguió", punt_ronda_jug2, "puntos. Un total de", pun2, "por ahora.")
    time.sleep(2)

    if punt_por_ronda_1 == punt_por_ronda_2:
        resp = "Hubo al menos una jugada con puntaje similar entre ambos jugadores."


#-----------------------------------------------------------------------------------------------------------


#CALCULO FINAL DEL PROGRAMA.

#TÍTULO
print("\t~~~~~~~~~~~~~~~~~~~\n"
      "\t !HA TERMINADO EL JUEGO! \n"       
      "\t~~~~~~~~~~~~~~~~~~~\n"
      "")
time.sleep(1)

#PUNTUACIÓN FINAL DEL JUGADOR 1.
print(jug_1,"Tu puntuación total fue de:", pun1)
time.sleep(1)

#PUNTUACIÓN FINAL DEL JUGADOR 2.
print(jug_2,"Tu puntuación total fue de:", pun2)
time.sleep(2)

#EN CASO DE QUE EL PUNTAJE FINAL DEL JUGADOR 1 SEA MAYOR AL JUGADOR 2, SE MUESTRA EL MENSAJE QUE ESTA DEBAJO.
if pun1 > pun2:

    winner = jug_1
    print("********************************************\n"
          "*         EL GANADOR DEL JUEGO ES:         *\n"
          "*",                "\t\t", winner + "!",                "*\n"
          "********************************************\n"
          "")
    print(random.choice(frase2), random.choice(caritasf))

#EN CASO DE QUE EL PUNTAJE FINAL DEL JUGADOR 2 SEA MAYOR AL JUGADOR 2, SE MUESTRA EL MENSAJE QUE ESTA DEBAJO.
elif pun2 > pun1:

    winner = jug_2
    print("********************************************\n"
          "*         EL GANADOR DEL JUEGO ES:         *\n"
          "*",                "\t\t", winner + "!",                "*\n"
          "********************************************\n"
          "")
    print(random.choice(frase2), random.choice(caritasf))

#EN CASO DE QUE EL PUNTAJE DE AMBOS JUGADORES SEA IGUAL, SE MUESTRA EL MENSAJE QUE ESTÁ DEBAJO.
elif pun1 == pun2:
    print("********************************************\n"
          "*                 ¡EMPATE!                 *\n"
          "*                                          *\n"
          "********************************************\n"
          "")
    print(random.choice(frase3), random.choice(caritast))
time.sleep(2)

#MOSTRAMOS LAS ESTADISTICAS PEDIDAS POR EL TP.

#ESTADISTICA 1
print("La cantidad de jugadas(rondas) fue de", cant_de_jug)

#ESTADISTICA 2
if resp == 0:
    print("No hubo ronda en donde ambos jugadores hayan obtenido igual puntaje.")
else:
    print(resp)

#ESTADISTICA 3
prom_pun1 = pun1 / cant_de_jug
prom_pun2 = pun2 / cant_de_jug

print("El promedio de puntos por jugada del jugador 1 fue de", prom_pun1, "puntos.")
print("El promedio de puntos por jugada del jugador 2 fue de", prom_pun1, "puntos.")

#ESTADISTICA 4
porc_aciert_jug_1 = (aciertos_jug_1 * 100) / cant_de_jug
porc_aciert_jug_2 = (aciertos_jug_2 * 100) / cant_de_jug
porc_aciert_jug_1str = str(porc_aciert_jug_1)
porc_aciert_jug_2str = str(porc_aciert_jug_2)

if (winner == jug_1) and (porc_aciert_jug_1 > porc_aciert_jug_2):
    print("El ganador", winner, "es el que ha conseguido mayor porcentaje de aciertos, con un "+porc_aciert_jug_1str+"% mayor al "+porc_aciert_jug_2str+"% de", jug_2)

elif (winner == jug_2) and (porc_aciert_jug_2 > porc_aciert_jug_1):
    print("El ganador", winner, "es el que ha conseguido mayor porcentaje de aciertos, con un "+porc_aciert_jug_2str+"% mayor al "+porc_aciert_jug_1str+"% de", jug_1)

else:
    print("El porcentaje de aciertos de", jug_1, "fue de "+porc_aciert_jug_1str+"% ; mientras que el de", jug_2, "fue de"+porc_aciert_jug_2str+"% ")

#ESTADISTICA 5

#MENSAJE FINAL
print("GRACIAS POR JUGAR!", random.choice(caritasf))

#CONSIGNA 1
'''
print("La cantidad de jugadas fue de", cant_de_jug, "en total.")
'''

#CONSIGNA 2
'''
if resp == 0:
print("No hubo ronda en donde ambos jugadores hayan obtenido igual puntaje.")
else:
print(resp)
'''

#CONSIGNA 3
'''
prom_pun1 = pun1 / cant_de_jug
prom_pun2 = pun2 / cant_de_jug

print("El promedio de puntos por jugada del jugador 1 fue de", prom_pun1, "puntos.")
print("El promedio de puntos por jugada del jugador 2 fue de", prom_pun1, "puntos.")
'''

#CONSIGNA 4
'''
porc_aciert_jug_1 = (aciertos_jug_1 * 100) / cant_de_jug
porc_aciert_jug_2 = (aciertos_jug_2 * 100) / cant_de_jug
porc_aciert_jug_1str = str(porc_aciert_jug_1)
porc_aciert_jug_2str = str(porc_aciert_jug_2)

if (winner == jug_1) and (porc_aciert_jug_1 > porc_aciert_jug_2):
    print("El ganador", winner, "es el que ha conseguido mayor porcentaje de aciertos, con un "+porc_aciert_jug_1str+"% mayor al "+porc_aciert_jug_2str+"% de", jug_2)

elif (winner == jug_2) and (porc_aciert_jug_2 > porc_aciert_jug_1):
    print("El ganador", winner, "es el que ha conseguido mayor porcentaje de aciertos, con un "+porc_aciert_jug_2str+"% mayor al "+porc_aciert_jug_1str+"% de", jug_1)
'''

#CONSIGNA 5
'''
if turn_jug_1 >= 3:
    print("El jugador 1 logró ganar 3 o más turnos seguidos.")
if turn_jug_2 >= 3:
    print("El jugador 2 logró ganar 3 o más turnos seguidos.")
'''
