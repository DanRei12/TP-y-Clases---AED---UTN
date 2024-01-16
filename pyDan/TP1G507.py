__author__ = "Grupo 507"

#LIBRERÍA UTILIZADA PARA LA GENERACIÓN DEL NÚMERO DE LOS DADOS.
import random

#TÍTULO Y PRESENTACIÓN DEL PROGRAMA.
print("\t\t", "=" * 27, "\n"
      "\t\t   | Juego de Dos o Tres |\n"
      "\t\t", "=" * 27, "\n")

print("¡Bienvenido al juego de Dos o Tres!. Antes de comenzar con el programa,\n"
      "hemos de advertirle que el mismo contiene pausas para hacerlo más comprensible a la lectura.\n"
      "De modo que, cuando el programa muestre [...], deberá presionar ENTER para continuar.\n")
print(input("[...]"))

print("Para comenzar, por favor, ingrese los nombres de los jugadores.\n"
      "")

# ---VARIABLES UTILIZADAS EN EL PROGRAMA.---

#VARIANTES DEL PROGRAMA PARA EL INGRESO DE FRASES.

frase1 = ("Ingrese su nombre por favor: "), ("¿Cuál es su nombre?:"), ("Ingrese su nombre aquí:"), \
         ("Escriba aquí su nombre:"), ("Pon tu nombre aquí:"), ("Escriba su nombre a continuación:"), \
         ("¡Escribe tu nombre!:"), ("¡Ingresa tu nombre!:"), ("¡Tu nombre va aquiiii! :"), \
         ("Estimado, favor de colocar su nombre aquí:"), ("Me encantaria que escriba su nombre a continuación:"), \
         ("¡Aqui!, ¡nombre!, ¡ya!, uga uga:")

elogio1 = ("¡Hermoso nombre!"), ("¡Que lindo nombre tienes!"), ("Nice name!"), ("¡Que buen nombre!"), \
          ("Me gusta tu nombre"), ("¡Rayos, tu nombre está muy bueno!"), ("¡Lindo nombre te llevas!"), \
          ("¡Me encanta tu nombre!"), ("Amo tu nombre"), ("Mmm, buen nombre"), ("Ha sido duro, ¿no?"), ("..."), \
          ("Gracias por ingresar tu nombre"),("Tu eres el verdadero"), ("Sin duda eres el rey de reyes"), \
          ("Awww, que lindo nombre portas"), ("Estupendo, tu nombre es el de todo un ganador"), \
          ("¿QUEE? Asi que tu eres el que se habia comido mis doritos"), ("Aahhh, así que vos eras el famosisimo")

frase2 = ("¡Felicidades!"), ("¡FELICIDADES!"), ("¡¡Guau!!"), ("¡Excelente!"), ("¡EXCELENTE!"), ("CONGRATULATIONS!"), \
         ("¡Lo has hecho!"), (":o"), ("¡¡WOW!!"), ("Suertudito")

frase3 = ("¡Buen intento!"), ("Será a la próxima"), ("Lo lamento"), ("¡Buen juego!"), ("Good game!"), \
         ("Excelente juego"), ("Ta bien"), ("Sapeee"), ("Alto juego te mandaste chabón"), ("No me la contés"), \
         ("No me la Constantine"), ("No me la Contastinopla"), ("No me la conteiner")

frase4 = ("¡Menudo combo, chaval!"), ("¡Fua, te salió la 10"), ("¡WOW!¡MIRA ÉSTE COMBO!"), ("Te la rifaste"), \
         ("¡MADRE MÍA, WILLY!"), ("Definitivamente la estás ganando, observa"), ("ONICHAN MITE MITE"), \
         ("¡No me la contés, mirá!"), ("¡¡Yamete kudasai!!"), ("Faa, te sacaste alto combo, ah re")

caritasf = ("(✿◠‿◠)"), ("╰(✿´⌣`✿)╯♡"), ("(≧o≦)"), ("(☆▽☆)"), ("(⌒‿⌒)"), ("( ´ ▽ ` )"), ("╰(*´︶`*)╯"), \
           ("(*¯︶¯*)"), ("(〃＾▽＾〃)"), ("(ﾉ´ヮ`)ﾉ*: ･ﾟ"), ("(๑˃ᴗ˂)ﻭ"), ("(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧"), ("(⁀ᗢ⁀)"), ("(*￣▽￣)b"), \
           ("≧◡≦"), ("≧◉◡◉≦❤"), ("(ˆ‿ˆԅ)❤"), ("（っ＾▿＾）"), ("ヽ(*⌒▽⌒*)ﾉ"), ("٩(◕‿◕｡)۶"), ("(＠＾◡＾)"), \
           ("(￣ω￣)"), ("(o´▽`o)"), ("(＾▽＾)"), ("╰(▔∀▔)╯"), ("ヽ(>∀<☆)ノ"), ("(*¯︶¯*)"), ("(>◡<)")

caritast = ("(˘︹˘)"), ("(´ヘ｀;)"), ("(╯︵╰,)"), ("(╯◕_◕)╯"), ("(⋋▂⋌)"), ("(´ー｀)"), ("(︶︹︺)"), ("ಥ_ಥ"), \
           ("o(╥﹏╥)o"), ("(｡ŏ﹏ŏ)"), ("(｡>﹏<｡)"), ("ಢ_ಢ༽"), ("(T_T)")

caritase = ("(ノಠ益ಠ)ノ彡"), ("щ(ಠ益ಠщ)"), ("щ(ಥДಥщ)"),("(￣。￣)"), ("٩(͡๏̯͡๏)۶"), ("(；￣Д￣)"), ("(」゜ロ゜)」")

#NOMBRE DEL PRIMER JUGADOR:
print("Jugador 1,", (random.choice(frase1)))
jug_1 = str(input(""))

print (random.choice(elogio1) + ",", jug_1, (random.choice(caritasf)), "\n")

#NOMBRE DEL SEGUNDO JUGADOR:
print ("Jugador 2,", (random.choice(frase1)))
jug_2 = str(input(""))

print(random.choice(elogio1) + ",", jug_2, (random.choice(caritasf)), "\n")

#PUNTAJE DEL PRIMER JUGADOR:
pun1 = 0

#PUNTAJE DEL SEGUNDO JUGADOR:
pun2 = 0

#PRIMER DADO:
dad1 = random.randint(1, 6)

#SEGUNDO DADO:
dad2 = random.randint(1, 6)

#TERCER DADO:
dad3 = random.randint(1, 6)

#OPCIONES DEL JUGADOR 1:
op1 = 0

#OPCIONES DEL JUGADOR 2:
op2 = 0

#VALORES DEL JUGADOR 1:
val1 = True

#VALORES DEL JUGADOR 2:
val2 = True

#-----------------------------------------------------------------------------------------------------------
reglas = str(input("Antes de empezar... ¿Quieres ver las reglas de juego? (´ω｀)" "\n"
                "Responde que si, si quieres ver las reglas: "))

if (reglas == ("Si quiero")) or (reglas == ("si quiero")) or (reglas == ("Si")) or (reglas == ("si")):
    print ("")
    print ("_" * 120)
    print ("# REGLAS DEL JUEGO:")
    print ("_" * 120)
    print ("\t""Este fue pensado para 2 jugadores")
    print ("\t""El juego consiste en dos tiradas de 3 dados de manera simultánea para cada jugador, en el ")
    print ("\t""que el objetivo será acumular la mayor cantidad de puntos posibles.""\n")
    print ("-| REGLAS DE LA PRIMERA RONDA:")
    print ("\t""Aquí el jugador debera hacer su tirada, en caso de")
    print ("\t""obtener tres números iguales, sumara 6 puntos; dos iguales, 3 puntos")
    print ("\t""y en caso de no tener numeros coincidentes, 0 puntos.")
    print ("\t""En el caso de sacar dos números coincidentes, el jugador debera tirar nuevamente el tercer dado")
    print ("\t""intentando conseguir un tercer coincidente.""\n")
    print ("-| REGLAS DE LA SEGUNDA RONDA:""\n"
       "\t""En esta ronda, el jugador ha de apostar si la suma de sus dados en su próxima tirada será par o impar.""\n"
       "\t""En caso de acertar, sumar el número mayor de dado obtenido a tu puntaje total, y en caso de""\n"
       "\t""no acertar, restar el número menor obtenido a tu puntaje total.""\n"
       "\t""Por último, tener en cuenta que en caso de que los tres dados sean de la paridad elegida""\n"
       "\t""el jugador debera de duplicar sus puntos.")
    print("\n"
          "!Comencemos con el juego!", random.choice(caritasf))
    print(input("[...]"))

else:
    print("¡Entonces empecemos el juego!", random.choice(caritasf))
    print(input("[...]"))


#-----------------------------------------------------------------------------------------------------------

#COMIENZO DE LA PRIMERA RONDA.

print("\t~~~~~~~~~~~~~~~~~\n"
      "\t! RONDA 1 (≧◡≦)!\n"
      "\t~~~~~~~~~~~~~~~~~")

print("■■■■■■■■■■■■■■■■■■■■■■■")
print(jug_1,"¡ES TU TURNO!", random.choice(caritasf))
print(input("Presiona enter para tirar tus dados..."))
print("......................")
print("Dado 1:", dad1)
print("Dado 2:", dad2)
print("Dado 3:", dad3)
print("......................")
print(input("Presiona enter para continuar..."))

#-----------------------------------------------------------------------------------------------------------

#VERIFICADORES Y ALGORITMO DE LA PRIMERA RONDA (PARA EL JUGADOR 1).

if dad1 == dad2 == dad3:    #SE VERIFICA SI LOS DADOS SON IGUALES.

     pun1 = pun1 + 6

     print(jug_1,"acumuló:", pun1 ,"Puntos.")

#SE VERIFICA SI EL DADO 3 ES DIFERENTE Y SE GENERA UN NUEVO VALOR
elif dad1 == dad2 != dad3:

    print("Se volverá a lanzar el dado 3!", random.choice(caritasf))
    print(input("[...]"))

    dad3 = random.randint(1, 6)

    print("Dado 3:", dad3)

    #SI EL DADO VUELVE A SER DIFERENTE, SE AÑADEN 3 PUNTOS AL CONTADOR DE PUNTOS
    if dad1 == dad2 != dad3:

        pun1 = pun1 + 3

        print(jug_1,"acumuló:", pun1, "Puntos.")

    #SI EL DADO ES IGUAL A LOS OTROS DOS, SE AÑADEN 6 PUNTOS AL CONTADOR DE PUNTOS:
    elif dad1 == dad2 == dad3:

        pun1 = pun1 + 6

        print(jug_1,"acumuló:", pun1 ,"Puntos.")

#SE REPITE EL MISMO PROCEDICIEMTNO CON EL DADO 2:
elif dad1 == dad3 != dad2:

    print("Se volverá a lanzar el dado 2!", random.choice(caritasf))
    print(input("[...]"))

    dad2 = random.randint(1, 6)

    print("Dado 2:", dad2)

    if dad1 == dad3 != dad2:

        pun1 = pun1 + 3

        print(jug_1,"acumuló:", pun1 ,"Puntos.")

    elif dad1 == dad3 == dad2:

        pun1 = pun1 + 6

        print(jug_1,"acumuló:", pun1 ,"Puntos.")

#SE REPITE EL MISMO PROCEDIMIENTO CON EL DADO 1.
elif dad3 == dad2 != dad1:

    print("Se volverá a lanzar el dado 1!", random.choice(caritasf))
    print(input("[...]"))

    dad1 = random.randint(1, 6)

    print("Dado 1:", dad1)

    if dad3 == dad2 != dad1:

        pun1 = pun1 + 3

        print(jug_1,"acumuló:", pun1 ,"Puntos.")

    elif dad3 == dad2 == dad1:

        pun1 = pun1 + 6

        print(jug_1,"acumuló:", pun1 ,"Puntos.")

#SE DETECTA QUE TODOS LOS DADOS SON DIFERENTES Y SE SUMAN 0 PUNTOS.
elif dad1 != dad2 != dad3:

    pun1 = 0

    print(jug_1,"acumuló", pun1 ,"Puntos, suerte la próxima.", random.choice(caritast), "\n"
                                   "")
print((input("[...]")))

#-----------------------------------------------------------------------------------------------------------

#SE GENERAN NUEVOS VALORES PARA LOS 3 DADOS, PARA EL TURNO DEL JUGADOR 2.
dad1 = random.randint(1, 6)

dad2 = random.randint(1, 6)

dad3 = random.randint(1, 6)

print("■■■■■■■■■■■■■■■■■■■■■■■")
print(jug_2,"¡ES TU TURNO!", random.choice(caritasf))
print(input("Presiona enter para lanzar los dados..."))
print("......................")
print("Dado 1:",dad1)
print("Dado 2:",dad2)
print("Dado 3:",dad3)
print("......................")
print(input("Presiona enter para continuar..."))

#-----------------------------------------------------------------------------------------------------------

#MISMOS VERIFICADORES Y ALGORITMOS PARA EL JUGADOR 2.

#SE VERIFICA QUE LOS DADOS SEAN IGUALES Y SE AÑADEN 6 PUNTOS:
if dad1 == dad2 == dad3:

    pun2 = pun2 + 6

    print(jug_2,"acumuló:", pun2 ,"Puntos.", random.choice(caritasf))

#SE DETECTA QUE EL DADO 3 ES DIFERENTE Y SE GENERA UN NUEVO VALOR PARA EL DADO 3.
elif dad1 == dad2 != dad3:

    print("Se volverá a lanzar el dado 3!", random.choice(caritasf))
    print(input("[...]"))

    dad3 = random.randint(1, 6)

    print("Dado 3:", dad3)

    #SI VUELVE A DAR DIFERENTE, ENTONCES SE SUMAN 3 PUNTOS.
    if dad1 == dad2 != dad3:

        pun2 = pun2 + 3

        print(jug_2,"acumuló:", pun2 ,"Puntos.")

    #EN CASO DE DAR IGUALES, SE SUMAN 6 PUNTOS.
    elif dad1 == dad2 == dad3:

        pun2 = pun2 + 6

        print(jug_2,"acumuló:", pun2 ,"Puntos.")

#SE REPITE EL MISMO PROCESO CON EL DADO 2.
elif dad1 == dad3 != dad2:

    print("Se volverá a lanzar el dado 2!", random.choice(caritasf))
    print(input("[...]"))

    dad2 = random.randint(1, 6)

    print("Dado 2:", dad2)

    if dad1 == dad3 != dad2:

        pun2 = pun2 + 3

        print(jug_2,"acumuló:", pun2 ,"Puntos.")

    elif dad1 == dad3 == dad2:

        pun2 = pun2 + 6

        print(jug_2,"acumuló:", pun2 ,"Puntos.")

#SE REPITE EL MISMO PROCESO CON EL DADO 1.
elif dad3 == dad2 != dad1:

    print("Se volverá a lanzar el dado 1!", random.choice(caritasf))
    print(input("[...]"))

    dad1 = random.randint(1, 6)

    print("Dado 1:", dad1)

    if dad3 == dad2 != dad1:

        pun2 = pun2 + 3

        print(jug_2,"acumuló:", pun2 ,"Puntos.")

    elif dad3 == dad2 == dad1:

        pun2 = pun2 + 6

        print(jug_2,"acumuló:", pun2 ,"Puntos.")

#SE DETECTA QUE TODOS LOS DADOS DIERON DIFERENTES NUMEROS Y SE SUMAN 0 PUNTOS.
elif dad1 != dad2 != dad3:

    pun2 = 0

    print(jug_2,"acumuló", pun2 ,"Puntos, suerte la próxima.", random.choice(caritast), "\n"
                                   "")
print(input("[...]"))

#-----------------------------------------------------------------------------------------------------------

#COMIENZO DE LA SEGUNDA RONDA.

#TÍTULO
print("\t~~~~~~~~~~~~~~~~~~~\n"
      "\t! RONDA 2 ❀◕‿◕❀!\n"       
      "\t~~~~~~~~~~~~~~~~~~~\n"
      "")

#EXPLICACIÓN.
print("\t", "*" * 79, "\n"
      "\t* En esta ronda, se apuestan los puntos de la ronda anterior. Deberán decidir *\n"
      "\t* si la sumatoria de los dados será par o impar!                              *\n"       
      "\t\t\t*!Que comiencen las apuestas (•⊙ω⊙•)!*\n"
      "\t", "*" * 79, "\n"
      "")
print(input("[...]"))

#MENU DE OPCIONES PARA EL PRIMER JUGADOR.
print(jug_1,"Seleccione alguna de las opciones:\n"
            "1 - Par.\n"
            "2 - Impar.\n")

op1 = int(input("Eliga una opción (1 o 2): "))

#SE DETECTA CUÁL OPCIÓN ELIGIÓ Y SE CAMBIA EL VALOR DE val1 DEPENDIENDO LA RESPUESTA.
if op1 == 1:
    print("¡", jug_1, ", has seleccionado PAR!", random.choice(caritasf))
    val1 = True

elif op1 == 2:
    print("¡", jug_1, ", has seleccioando IMPAR!", random.choice(caritasf))
    val1 = False

#EN CASO DE ESCRIBIR UNA OPCIÓN NO VÁLIDA, EL PROGRAMA SE DETIENE.
else:
    print("La opción elegida no es válida", random.choice(caritase))
    print(input("Presiona [Enter] para salir."))
    exit()

#SE GENERAN NUEVOS VALORES PARA LOS DADOS.
dad1 = random.randint(1, 6)

dad2 = random.randint(1, 6)

dad3 = random.randint(1, 6)

may = max(dad1, dad2, dad3)

men = min(dad1, dad2, dad3)

#SE MUESTRAN LOS VALORES PARA QUE LOS JUGADORES PUEDAN HACER LA SUMA
#Y PARA QUE SE CONFIRMEN LA SUMA/RESTA HECHA POR EL PROGRAMA.

print("Los resultados de tus dados son:")

print("Dado 1:", dad1)

print("Dado 2:", dad2)

print("Dado 3:", dad3)
print(input("[...]"))

#-----------------------------------------------------------------------------------------------------------

#VERIFICADORES Y ALGORITMO DE LA SEGUNDA RONDA PARA EL PRIMER JUGADOR (EN CASO DE SELECCIONAR LA OPCION 1: PAR).

if val1 == True:

    print(jug_1, "Tira los dados y busca la sumatoria de números → PARES ←")

    #SE VERIFICA QUE LA SUMA DE LOS DADOS SEA DIVISIBLE POR 2 Y DE 0, CONFIRMANDO QUE EL NÚMERO ES PAR.
    if (dad1 + dad2 + dad3) % 2 == 0:

        print("La sumatoria de los dados es PAR!", random.choice(caritasf))

        pun1 = pun1 + may

        print("Su resultado es,", pun1)

        #EN EL CASO DE QUE TODOS LOS NÚMEROS SEAN PARES,
        #SE APLICA LA REGLA DEL JUEGO, EN DONDE SE MULTIPLICA EL PUNTAJE POR DOS.
        if (dad1 % 2) == 0 and (dad2 % 2) == 0 and (dad3 % 2) == 0:

            pun1 = pun1 * 2

            print("Los dados también son PARES!\n", random.choice(caritasf),
                    "Su resultado final es:", pun1)

    else:

        #SI LA SUMA DE LOS DADOS ES IMPAR, SE RESTA EL MENOR.
        print("La sumatoria de los dados es IMPAR!", random.choice(caritast))

        pun1 = pun1 - men

        print("Su resultado final es:", pun1)

    print(input("[...]"))
#-----------------------------------------------------------------------------------------------------------

#VERIFICADORES Y ALGORITMO DE LA SEGUNDA RONDA PARA EL PRIMER JUGADOR (EN CASO DE SELECCIONAR LA OPCION 2: IMPAR).

#SE VERIFICA QUE EL VALOR DE val1 SEA FALSO, ES DECIR, QUE SE HAYA SELECCIONADO LA SEGUNDA OPCION.
if val1 == False:

    print(jug_1,"Tira los dados y busca la sumatoria de números → IMPARES ←")

    #SE VERIFICA QUE LA SUMA DE LOS DADOS, AL DIVIRSE POR 2, NO SEA 0. ES DECIR, QUE SEA IMPAR.
    if (dad1 + dad2 + dad3) % 2 != 0:

        print("La sumatoria de los dados es IMPAR!", random.choice(caritasf))

        pun1 = pun1 + may

        print("Su resultado es,", pun1)

    else:

        #SI LA SUMA DE LOS DADOS ES PAR, SE RESTA EL MENOR.
        print("La sumatoria de los dados es PAR!", random.choice(caritasf))

        pun1 = pun1 - men

        print("Su resultado final es:", pun1, random.choice(caritast))

    print(input("[...]"))
#-----------------------------------------------------------------------------------------------------------

#LO MISMO OCURRE PARA EL JUGADOR 2.

print("■■■■■■■■■■■■■■■■")
print(jug_2,"\n1 - Par.\n"        #MENU PARA EL SEGUNDO JUGADOR.
            "2 - Impar.\n")

op2 = int(input("Seleccione una opción (1 o 2): "))

#SE VERIFICA QUÉ OPCIÓN SELECCIONÓ Y SE CAMBIA LA VARIABLE val2.
if op2 == 1:
    print("¡", jug_2, ", has seleccionado PAR.", random.choice(caritasf))
    val2 = True
    print(input("[...]"))

elif op2 == 2:
    print("¡", jug_2, ", has seleccionado IMPAR.", random.choice(caritasf))
    val2 = False
    print(input("[...]"))

else:
    print("No es una opción válida.")
    print(input("[...]"))
    exit()

#SE GENERAN NUEVOS DATOS PARA LOS DADOS.
dad1 = random.randint(1, 6)

dad2 = random.randint(1, 6)

dad3 = random.randint(1, 6)

may = max(dad1, dad2, dad3)

men = min(dad1, dad2, dad3)

#SE MUESTRAN LOS DATOS PARA REALIZAR LA SUMA Y PARA VERIFICAR QUE EL PROGRAMA
#REALIZÓ LA SUMA CORRECTAMENTE.
print("Dado 1:", dad1)

print("Dado 2:", dad2)

print("Dado 3:", dad3)
print(input("[...]"))

#-----------------------------------------------------------------------------------------------------------

#VERIFICADORES Y ALGORITMO DE LA SEGUNDA RONDA PARA EL SEGUNDO JUGADOR (EN CASO DE SELECCIONAR LA OPCION 1: PAR).

if val2 == True:

    print(jug_2,"Tira los dados y busca la sumatoria de números → PARES ←")

    if (dad1 + dad2 + dad3) % 2 == 0:

        print("La sumatoria de los dados es PAR!", random.choice(caritasf))

        pun2 = pun2 + may

        print("Su resultado es,", pun2)

        if (dad1 % 2) == 0 and (dad2 % 2) == 0 and (dad3 % 2) == 0:

            pun2 = pun2 * 2

            print("Los dados también son PARES!\n", random.choice(caritasf),
                    "Su resultado final es:", pun2)

    else:

        print("La sumatoria de los dados es IMPAR!", random.choice(caritast))

        pun2 = pun2 - men

        print("Su resultado final es:", pun2, random.choice(caritase))

    print(input("[...]"))
#-----------------------------------------------------------------------------------------------------------

#VERIFICADORES Y ALGORITMO DE LA SEGUNDA RONDA PARA EL SEGUNDO JUGADOR (EN CASO DE SELECCIONAR LA OPCION 2: IMPAR).

if val2 == False:

    print(jug_2,"Tira los dados y busca la sumatoria de números → IMPARES ←")

    if (dad1 + dad2 + dad3) % 2 != 0:

        print("La sumatoria de los dados es IMPAR!", random.choice(caritasf))

        pun2 = pun2 + may

        print("Su resultado es,", pun2)

        if (dad1 % 2) != 0 and (dad2 % 2) != 0 and (dad3 % 2) != 0:

            pun2 = pun2 * 2

            print("Los dados también son IMPARES!\n", random.choice(caritasf),
                    "Su resultado final es:", pun2)

    else:

        print("La sumatoria de los dados es PAR!", random.choice(caritast))

        pun2 = pun2 - men

        print("Su resultado final es:", pun2, random.choice(caritase))

    print(input("[...]"))

#-----------------------------------------------------------------------------------------------------------

#CALCULO FINAL DEL PROGRAMA.

#TÍTULO
print("\t~~~~~~~~~~~~~~~~~~~\n"
      "\t !RESULTADO FINAL! \n"       
      "\t~~~~~~~~~~~~~~~~~~~\n"
      "")

#PUNTUACIÓN FINAL DEL JUGADOR 1.
print(jug_1,"Su puntuación total fue de:", pun1)

#PUNTUACIÓN FINAL DEL JUGADOR 2.
print(jug_2,"Su puntuación total fue de:", pun2)

print(input("[...]"))

#EN CASO DE QUE EL PUNTAJE FINAL DEL JUGADOR 1 SEA MAYOR AL JUGADOR 2, SE MUESTRA EL MENSAJE QUE ESTA DEBAJO.
if pun1 > pun2:
    print("********************************************\n"
          "*         EL GANADOR DEL JUEGO ES:         *\n"
          "*",                "\t\t", jug_1 + "!",                "*\n"
          "********************************************\n"
          "")
    print(random.choice(frase2), random.choice(caritasf))

#EN CASO DE QUE EL PUNTAJE FINAL DEL JUGADOR 2 SEA MAYOR AL JUGADOR 2, SE MUESTRA EL MENSAJE QUE ESTA DEBAJO.
elif pun2 > pun1:
    print("********************************************\n"
          "*         EL GANADOR DEL JUEGO ES:         *\n"
          "*",                "\t\t", jug_2 + "!",                "*\n"
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
print(input("[...]"))

#MENSAJE FINAL
print("GRACIAS POR JUGAR!", random.choice(caritasf))
