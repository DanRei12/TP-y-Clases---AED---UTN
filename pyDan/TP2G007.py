'''
Cada jugador solo apuesta por par o impar. Si acierta gana el puntaje equivalente al dado de
mayor valor, y adicionalmente este puntaje se duplica si todos los dados son de dicha paridad. Si pierde, resta el dado
de menor valor (puede quedar con puntaje negativo).

Se debe mostrar por cada turno el valor de los dados y el puntaje parcial del jugador.

Al terminar el turno de ambos jugadores, se verifica si alguno de ellos alcanzó el puntaje objetivo. Si no es así,
vuelven a jugar ambos (cada uno debe completar su turno) hasta finalizar el juego.

Al terminar el juego, se debe mostrar el nombre y puntaje total obtenido de cada jugador e informar el nombre del
ganador. Si ambos jugadores llegaran a tener el mismo puntaje final, gana aquel jugador que tenga la mayor cantidad
de jugadas ganadas. Si coinciden también en cantidad de jugadas, entonces es un empate.

'''

__author__ = "Grupo 007"

#LIBRERÍA UTILIZADA PARA LA GENERACIÓN DEL NÚMERO DE LOS DADOS.
import random
import time

#TÍTULO Y PRESENTACIÓN DEL PROGRAMA.
print("\t\t", "=" * 27, "\n"
      "\t\t   | Juego de Dados |\n"
      "\t\t", "=" * 27, "\n")

print("¡Bienvenido al juego de Dados!. Antes de comenzar con el programa,\n"
      "hemos de advertirle que el mismo contiene pausas para hacerlo más comprensible a la lectura.\n")

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
jug_1 = str(input("Su nombre: "))
print (random.choice(elogio1) + ",", jug_1, (random.choice(caritasf)), "\n")
time.sleep(0.7)

#NOMBRE DEL SEGUNDO JUGADOR:
print ("Jugador 2,", (random.choice(frase1)))
jug_2 = str(input("Su nombre: "))
print(random.choice(elogio1) + ",", jug_2, (random.choice(caritasf)), "\n")
time.sleep(1.3)

#-----------------------------------------------------------------------------------------------------------

#PUNTAJE DEL PRIMER JUGADOR:
pun1 = 0

#PUNTAJE DEL SEGUNDO JUGADOR:
pun2 = 0

#PUNTAJE POR RONDA DEL JUGADOR 1:
punt_ronda_jug_1 = 0

#PUNTAJE POR RONDA DEL JUGADOR 2:
punt_ronda_jug_2 = 0

#CANTIDAD DE TURNOS SEGUIDOS GANADOS POR EL JUGADOR 1.
turn_gan_jug_1 = 0

#CANTIDAD DE TURNOS SEGUIDOS GANADOS POR EL JUGADOR 2.
turn_gan_jug_2 = 0

#RESPUESTA DE TURNOS SEGUIDOS JUGADOR 1:
resp_turn_gan_jug_1 = "El jugador 1 no logró ganar 3 turnos seguidos."

#RESPUESTA DE TURNOS SEGUIDOS JUGADOR 2:
resp_turn_gan_jug_2 = "El jugador 2 no logró ganar 3 turnos seguidos."

#CANTIDAD DE JUGADAS DEL JUEGO:
cant_de_jug = 0

#ACIERTOS DEL JUGADOR 1:
aciertos_jug_1 = 0

#ACIERTOS DEL JUGADOR 2:
aciertos_jug_2 = 0

#OPCIONES DEL JUGADOR 1:
op1 = 0

#OPCIONES DEL JUGADOR 2:
op2 = 0

#VALORES DEL JUGADOR 1:
val1 = True

#VALORES DEL JUGADOR 2:
val2 = True

#RESPUESTA DE ESTADISTICA 2
resp = 0

#-----------------------------------------------------------------------------------------------------------
reglas = str(input("Antes de empezar... ¿Quieres ver las reglas de juego? (´ω｀)" "\n"
                "Responde que si, si quieres ver las reglas: "))

if (reglas == ("Si quiero")) or (reglas == ("si quiero")) or (reglas == ("Si")) or (reglas == ("si")):
    print("")
    print("_" * 120)
    print("# REGLAS DEL JUEGO:")
    print("_" * 120)
    print("\tEl juego consiste en tiradas de 3 dados de manera simultánea para cada jugador, en el que el objetivo")
    print("\tserá acumular la cantidad de puntos propuesta por los jugadores.\n")
    print("\n\tCada jugador, en cada ronda, deberá apostar si la suma de sus dados en su tirada será par o impar.\n"
       "\tEn caso de acertar, se sumará el número mayor de dado obtenido a su puntaje total, y en caso de\n"
       "\tno acertar, se restará el número menor obtenido a su puntaje total.\n"
       "\tAdemás, debera de tener en cuenta que en caso de que los tres dados sean de la paridad elegida\n"
       "\tel jugador duplicara sus puntos obtenidos en esa ronda."
       "\tGanará el jugador que llegue mas pronto a la cantidad estipulada, en caso de producirse un empate, se "
       "\trecurrira a determinar al ganador mediante la cantidad de rondas(jugadas) ganadas, en caso de persistir la "
       "\tigualdad, se declarara un empate entre ambos jugadores.")
    time.sleep(1)
    input("\n¿Estas listo? (Presiona enter)")
    print("\n"
          "Bien, pues... !Comencemos con el juego!", random.choice(caritasf))
    time.sleep(1)

else:
    print("\n¡Entonces empecemos el juego!\n", random.choice(caritasf))
    time.sleep(1)


#-----------------------------------------------------------------------------------------------------------

#COMIENZO DEL JUEGO.

#Valor por teclado del puntaje a alcanzar,
x = int(input("\nIngresar abajo la cantidad de puntos a alcanzar para poder ganar el juego. "
              "(Este número debe de ser mayor a 10)\n"))
while x <= 10:
    x = int(input("¡Error! Número invalido, por favor ingresar el valor nuevamente.\nIngresar aquí: "))

time.sleep(1)
while (pun1 < x) and (pun2 < x):
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

    #EN CASO DE ESCRIBIR UNA OPCIÓN NO VÁLIDA, SE PIDE NUEVAMENTE LA OPCIÓN.
    while (op1 != 1) and (op1 != 2):
        print("La opción elegida no es válida", random.choice(caritase))
        op1 = int(input("Ingresar abajo nuevamente su opción (1 para par ; 2 para impar).\n"))

    #SE DETECTA CUÁL OPCIÓN ELIGIÓ Y SE CAMBIA EL VALOR DE val1 DEPENDIENDO LA RESPUESTA.
    if op1 == 1:
        print("¡", jug_1, ", has seleccionado PAR!", random.choice(caritasf))
        val1 = True

    elif op1 == 2:
        print("¡", jug_1, ", has seleccionado IMPAR!", random.choice(caritasf))
        val1 = False

    time.sleep(1)

    #SE ESTABLECEN LOS NUMEROS DE LOS DADOS PARA EL JUGADOR 1.
    dad1 = random.randint(1, 6)
    dad2 = random.randint(1, 6)
    dad3 = random.randint(1, 6)

    may = max(dad1, dad2, dad3)
    men = min(dad1, dad2, dad3)

    #SE MUESTRAN LOS VALORES PARA QUE LOS JUGADORES PUEDAN HACER LA SUMA
    #CONFIRMANDO ASÍ LO CALCULADO POR EL PROGRAMA.

    print("\nLos resultados de tus dados son:")

    print("Dado 1:", dad1)
    time.sleep(1)

    print("Dado 2:", dad2)
    time.sleep(1)

    print("Dado 3:", dad3)
    time.sleep(1)

    #-----------------------------------------------------------------------------------------------------------

    #VERIFICADORES Y ALGORITMO DE LA RONDA PARA EL PRIMER JUGADOR (EN CASO DE SELECCIONAR LA OPCION 1: PAR).

    if val1 == True:

        print(jug_1, "Tiró los dados buscando la sumatoria de números → PARES ←\n")
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

        print(jug_1,"Tiró los dados buscando la sumatoria de números → IMPARES ←\n")
        time.sleep(1)

        #SE VERIFICA QUE LA SUMA DE LOS DADOS, AL DIVIRSE POR 2, NO SEA 0. ES DECIR, QUE SEA IMPAR.
        if (dad1 + dad2 + dad3) % 2 != 0:

            aciertos_jug_1 += 1
            print("La sumatoria de los dados es IMPAR!", random.choice(caritasf))
            time.sleep(1)

            punt_ronda_jug_1 = may

            #EN EL CASO DE QUE TODOS LOS NÚMEROS SEAN IMPARES,
            #SE APLICA LA REGLA DEL JUEGO, EN DONDE SE MULTIPLICA EL PUNTAJE POR DOS.
            if ((dad1 % 2) != 0) and ((dad2 % 2) != 0) and ((dad3 % 2) != 0):

                punt_ronda_jug_1 = may * 2

                print("Y los dados también son IMPARES!", random.choice(caritasf))

        else:

            #SI LA SUMA DE LOS DADOS ES PAR, SE RESTA EL MENOR.
            print("La sumatoria de los dados es PAR!", random.choice(caritast))

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

    #EN CASO DE ESCRIBIR UNA OPCIÓN NO VÁLIDA, SE PIDE NUEVAMENTE LA OPCIÓN.
    while (op1 != 1) and (op1 != 2):
        print("La opción elegida no es válida", random.choice(caritase))
        op1 = int(input("Ingresar abajo nuevamente su opción (1 para par ; 2 para impar).\n"))

    #SE DETECTA CUÁL OPCIÓN ELIGIÓ Y SE CAMBIA EL VALOR DE val2 DEPENDIENDO LA RESPUESTA.
    if op2 == 1:
        print("¡", jug_2, ", has seleccionado PAR!", random.choice(caritasf))
        val2 = True

    elif op2 == 2:
        print("¡", jug_2, ", has seleccionado IMPAR!", random.choice(caritasf))
        val2 = False

    time.sleep(1)

    #SE ESTABLECEN LOS NUMEROS DE LOS DADOS PARA EL JUGADOR 1.
    dad1 = random.randint(1, 6)
    dad2 = random.randint(1, 6)
    dad3 = random.randint(1, 6)

    may = max(dad1, dad2, dad3)
    men = min(dad1, dad2, dad3)

    #SE MUESTRAN LOS VALORES PARA QUE LOS JUGADORES PUEDAN HACER LA SUMA
    #CONFIRMANDO ASÍ LO CALCULADO POR EL PROGRAMA.

    print("\nLos resultados de tus dados son:")

    print("Dado 1:", dad1)
    time.sleep(1)

    print("Dado 2:", dad2)
    time.sleep(1)

    print("Dado 3:", dad3)
    time.sleep(1)

    #-----------------------------------------------------------------------------------------------------------

    #VERIFICADORES Y ALGORITMO DE LA RONDA PARA EL SEGUNDO JUGADOR (EN CASO DE SELECCIONAR LA OPCION 1: PAR).

    if val2 == True:

        print(jug_2, "Tiró los dados buscando la sumatoria de números → PARES ←\n")
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

        print(jug_2,"Tiró los dados buscando la sumatoria de números → IMPARES ←")
        time.sleep(1)

        #SE VERIFICA QUE LA SUMA DE LOS DADOS, AL DIVIRSE POR 2, NO SEA 0. ES DECIR, QUE SEA IMPAR.
        if (dad1 + dad2 + dad3) % 2 != 0:

            aciertos_jug_2 += 1
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
            print("La sumatoria de los dados es PAR!", random.choice(caritast))

            punt_ronda_jug_2 -= men

    time.sleep(1)
    pun2 += punt_ronda_jug_2

    print("\nEn esta ronda nro", cant_de_jug, ":", jug_1, "consiguió", punt_ronda_jug_1, "puntos. Un total de", pun1, "por ahora.")
    print("Y", jug_2, "consiguió", punt_ronda_jug_2, "puntos. Un total de", pun2, "por ahora.")
    time.sleep(2)

    if punt_ronda_jug_1 > punt_ronda_jug_2:
        turn_gan_jug_1 += 1
        turn_gan_jug_2 = 0

    elif punt_ronda_jug_2 > punt_ronda_jug_1:
        turn_gan_jug_2 += 1
        turn_gan_jug_1 = 0

    elif punt_ronda_jug_1 == punt_ronda_jug_2:
        turn_gan_jug_1 = 0
        turn_gan_jug_2 = 0
        resp = "Hubo al menos una jugada con puntaje similar entre ambos jugadores."

    if turn_gan_jug_1 >= 3:
        resp_turn_gan_jug_1 = "El jugador 1 logró ganar 3 o mas turnos seguidos."

    elif turn_gan_jug_2 >= 3:
        resp_turn_gan_jug_2 = "El jugador 2 logró ganar 3 o mas turnos seguidos."


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
    if aciertos_jug_1 > aciertos_jug_2:
        winner = jug_1
        print("********************************************\n"
          "*         EL GANADOR DEL JUEGO ES:         *\n"
          "*",                "\t\t", winner + "!",                "*\n"
          "********************************************\n"
          "")
        print(random.choice(frase2), random.choice(caritasf))

    elif aciertos_jug_2 > aciertos_jug_1:
        winner = jug_2
        print("********************************************\n"
          "*         EL GANADOR DEL JUEGO ES:         *\n"
          "*",                "\t\t", winner + "!",                "*\n"
          "********************************************\n"
          "")
        print(random.choice(frase2), random.choice(caritasf))

    else:
        winner = None
        print("********************************************\n"
            "*                 ¡EMPATE!                 *\n"
            "*                                          *\n"
            "********************************************\n"
            "")

        print(random.choice(frase3), random.choice(caritast))
time.sleep(2)

#MOSTRAMOS LAS ESTADISTICAS PEDIDAS POR EL TP.
print("\nEstadisticas del juego:")

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
print(resp_turn_gan_jug_1)
print(resp_turn_gan_jug_2)

#MENSAJE FINAL
print("GRACIAS POR JUGAR!", random.choice(caritasf))
input("\nPresiona enter para salir.")
