import time
import random

'''               Programa el cual se dedica a la simulación de un juego de dados para 2 jugadores.
                      En la primera tirada, el jugador solo puede conseguir 0, 3 y 6 puntos.
                              0 en caso de que los números de los dados no coincidan
                       3 en caso de que los números de los dados coincidan únicamente dos
                          (esto luego de haber tirado el dado no coincidente y fallar.)
                                  Y 6 en caso de que los tres dados coincidan

              En la segunda tirada el jugador debe de apostar que la suma de los dados de su segunda tirada sean par
            o impar (a elección), en caso de acertar, debe de sumar el mayor número conseguido en esta ronda al puntaje
                       total, en caso de fallar, debe de restar el dado de menor valor a su puntaje total.
            Por último, en caso de que los 3 dados coincidan con la paridad elegida, su puntaje debe de duplicarse.'''



print ("_" * 120)
print ("\t""\t""                                |Juego de dados|")
print ("-" * 120)
time.sleep (1)

print ("=" * 120)
print ("REGLAS DEL JUEGO:")
print ("=" * 90)
print ("\t""Este fue pensado para 2 jugadores")
time.sleep (2)
print ("\t""El juego consiste en dos tiradas de 3 dados de manera simultánea para cada jugador, en el ")
print ("\t""que el objetivo será acumular la mayor cantidad de puntos posibles.""\n")
time.sleep (8)
print ("-| REGLAS DE LA PRIMERA RONDA:")
time.sleep (2)
print ("\t""Aquí el jugador debera hacer su tirada, en caso de")
print ("\t""obtener tres números iguales, sumara 6 puntos; dos iguales, 3 puntos")
print ("\t""y en caso de no tener numeros coincidentes, 0 puntos.")
print ("\t""En el caso de sacar dos números coincidentes, el jugador debera tirar nuevamente el tercer dado")
print ("\t""intentando conseguir un tercer coincidente.""\n")
time.sleep (13)
print ("-| REGLAS DE LA SEGUNDA RONDA:""\n"
       "\t""En esta ronda, el jugador ha de apostar si la suma de sus dados en su próxima tirada será par o impar.""\n"
       "\t""En caso de acertar, sumar el número mayor de dado obtenido a tu puntaje total, y en caso de""\n"
       "\t""no acertar, restar el número menor obtenido a tu puntaje total.""\n"
       "\t""Por último, tener en cuenta que en caso de que los tres dados sean de la paridad elegida""\n"
       "\t""el jugador debera de duplicar sus puntos.")
time.sleep (13)
print ("=" * 120)

print (input("'Enter' para empezar a jugar."))
print ("¡¡Comienza el juego!!")
time.sleep (1)
elog = "Que bonito nombre tienes", "Tu nombre es genial,", "Me gusta tu nombre", "Ese nombre es épico,", "Your name is sooooo cute,", "¿Y ese nombre? Se nota que a vos no te querian de chiquito"
Nombre1=input("\n""Introduzca el nombre del primer jugador: ")
print (random.choice (elog), Nombre1)
time.sleep (1)
Nombre2=input("\n""Introduzca el nombre del segundo jugador: ")
print (random.choice (elog), Nombre2)
time.sleep (1)

t1_1= random.randint(1, 6)
t1_2= random.randint(1, 6)
t2_1= random.randint(1, 6)
t2_2= random.randint(1, 6)
t3_1= random.randint(1, 6)
t3_2= random.randint(1, 6)

print (input("\n""Genial, empecemos."
             "\n""|Jugador 1| Presione 'enter' para tirar sus dados""\n"))

time.sleep (1)
print ("Sus dados empezaron a rodar")
time.sleep (2)
print ("Rodando...")
time.sleep (1)
print ("Rodando...")
time.sleep (1)
print ("Se estan parando y...")
time.sleep (3)
print ("Empezaron a rodar de vuelta")
time.sleep (1)
print ("Rodando...")
time.sleep (1)
print ("Rodando...")
time.sleep (2)

print ("Sacaste un", t1_1, "; un", t2_1,  "; y un", t3_1)
time.sleep (3)

if (t1_1 != t2_1) and (t1_1 != t3_1) and (t2_1 != t3_1):
    print ("¡¡¡NOOO!!!", "Perdiste la ronda, no tenes dados iguales. 0 puntos")
    time.sleep(2)
    jug1punt1 = 0
elif (t1_1 == t2_1) and (t1_1 == t3_1):
    print ("Bien, obtuviste tres dados iguales, sumas 6 puntos.")
    time.sleep (2)
    jug1punt1 = 6
elif ((t1_1 == t2_1) and (t1_1 != t3_1)) or ((t1_1 == t3_1) and (t1_1 != t2_1)) or ((t2_1 == t3_1) and (t2_1 != t1_1)):
    print ("Joya, obtuviste dos dados iguales, vamos a por el tercero.")
    t4_1 = random.randint(1, 6)
    print (input("Presiona 'enter' para tirar el dado."))
    time.sleep (2)
    if ((t4_1 == t1_1) and (t4_1 == t2_1)) or ((t4_1 == t2_1) and (t4_1 == t3_1)) or ((t4_1 == t1_1) and (t4_1 == t3_1)):
        print ("Genial, sacaste otro", t4_1, "así que obtienes 6 puntos.")
        jug1punt1 = 6
        time.sleep (2)
    else:
        print ("Ups, sacaste un", t4_1, "y dado a que no es igual a tus otros dados, obtienes 3 puntos.")
        jug1punt1 = 3
        time.sleep (2)

print ("Bien, ahora proseguiremos con el jugador 2.")
print (input("\n""|Jugador 2| Presione 'enter' para tirar sus dados""\n"))

time.sleep (1)
print ("Tus dados empezaron a rodar")
time.sleep (2)
print ("Rodando...")
time.sleep (1)
print ("Rodando...")
time.sleep (1)
print ("Se estan deteniendo y...")
time.sleep (3)
print ("Empezaron a rodar de vuelta")
time.sleep (1)
print ("Rodando...")
time.sleep (1)
print ("Rodando...")
time.sleep (2)

print ("Sacaste un", t1_2, "; un", t2_2,  "; y un", t3_2)
time.sleep (3)

if (t1_2 != t2_2) and (t1_2 != t3_2) and (t2_2 != t3_2):
    print ("¡¡¡NOOO!!!", "Perdiste la ronda, no tenes dados iguales. 0 puntos")
    time.sleep(2)
    jug2punt1 = 0
elif (t1_2 == t2_2) and (t1_2 == t3_2):
    print ("Bien, obtuviste tres dados iguales, sumas 6 puntos.")
    time.sleep (2)
    jug2punt1 = 6
elif ((t1_2 == t2_2) and (t1_2 != t3_2)) or ((t1_2 == t3_2) and (t1_2 != t2_2)) or ((t2_2 == t3_2) and (t2_2 != t1_2)):
    print ("Joya, obtuviste dos dados iguales, vamos a por el tercero.")
    t4_2 = random.randint(1, 6)
    print (input("Presiona 'enter' para tirar el dado."))
    time.sleep (2)
    if ((t4_2 == t1_2) and (t4_2 == t2_2)) or ((t4_2 == t2_2) and (t4_2 == t3_2)) or ((t4_2 == t1_2) and (t4_2 == t3_2)):
        print ("Genial, sacaste otro", t4_2, "así que obtienes 6 puntos.")
        jug2punt1 = 6
        time.sleep (2)
    else:
        print ("Ups, sacaste un", t4_2, "y dado a que no es igual a tus otros dados, obtienes 3 puntos.")
        jug2punt1 = 3
        time.sleep (2)

print ("Bien, hemos concluido con la primera ronda, pasemos a la segunda")
time.sleep (2)

d1_1= random.randint(1, 6)
d1_2= random.randint(1, 6)
d2_1= random.randint(1, 6)
d2_2= random.randint(1, 6)
d3_1= random.randint(1, 6)
d3_2= random.randint(1, 6)
j1sumpunt2 = d1_1 + d2_1 + d3_1
j2sumpunt2 = d1_2 + d2_2 + d3_2
if (d1_1 > d2_1) and (d1_1 > d3_1):
    mayor1 = d1_1
elif (d2_1 > d1_1) and (d2_1 > d3_1):
    mayor1 = d2_1
elif (d3_1 > d1_1) and (d3_1 > d2_1):
    mayor1 = d3_1

if (d1_1 < d2_1) and (d1_1 < d3_1):
    menor1 = d1_1
elif (d2_1 < d1_1) and (d2_1 < d3_1):
    menor1 = d2_1
elif (d3_1 < d1_1) and (d3_1 < d2_1):
    menor1 = d3_1

if (d1_2 > d2_2) and (d1_2 > d3_2):
    mayor2 = d1_2
elif (d2_2 > d1_2) and (d2_2 > d3_2):
    mayor2 = d2_2
elif (d3_2 > d1_2) and (d3_2 > d2_2):
    mayor2 = d3_2

if (d1_2 < d2_2) and (d1_2 < d3_2):
    menor2 = d1_2
elif (d2_2 < d1_2) and (d2_2 < d3_2):
    menor2 = d2_2
elif (d3_2 < d1_2) and (d3_2 < d2_2):
    menor2 = d3_2

resp1 = input("|Jugador 1| Ingrese su apuesta, par o impar: ")
print (input("\n""|Jugador 1| Por favor, presionar 'enter' para lanzar su dado." ))
time.sleep (1)
print ("Sus dados empezaron a rodar")
time.sleep (2)
print ("Rodando...")
time.sleep (1)
print ("Rodando...")
time.sleep (1)
print ("Se estan parando y...")
time.sleep (3)
print ("Empezaron a rodar de vuelta")
time.sleep (1)
print ("Rodando...")
time.sleep (1)
print ("Rodando...")
time.sleep (2)

print ("Sacaste un", d1_1, "; un", d2_1,  "; y un", d3_1)
time.sleep (3)

if ((resp1 == "par") or (resp1 == "Par")) and ((j1sumpunt2 % 2) == 0) and ((d1_1 % 2) == 0) and ((d2_1 % 2) == 0) and ((d3_1 % 2) == 0):
    print ("Espectacular, lo conseguiste, tienes tres numeros de una misma paridad, duplicaremos tu puntaje total.")
    puntT1 = jug1punt1 * 2
elif ((resp1 == "par") or (resp1 == "Par")) and ((j1sumpunt2 % 2) == 0) and (((d1_1 % 2) != 0) or ((d2_1 % 2) != 0) or ((d3_1 % 2) != 0)):
    print ("Bueno, obtuviste un resultado par, sumaremos el", mayor1, "a tu puntaje total.")
    puntT1 = jug1punt1 + mayor1
elif ((resp1 == "impar") or (resp1 == "Impar")) and ((j1sumpunt2 == 0) or (j1sumpunt2 ==1) or (j1sumpunt2 ==3) or (j1sumpunt2 ==5) or (j1sumpunt2 ==7) or (j1sumpunt2 ==9) or (j1sumpunt2 ==11) or (j1sumpunt2 ==13) or (j1sumpunt2 ==15) or (j1sumpunt2 ==17)) and ((d1_1 == 0) or (d1_1 ==1) or (d1_1 ==3) or (d1_1 ==5) or (d1_1 ==7) or (d1_1 ==9) or (d1_1 ==11) or (d1_1 ==13) or (d1_1 ==15) or (d1_1 ==17)) and ((d2_1 == 0) or (d2_1 ==1) or (d2_1 ==3) or (d2_1 ==5) or (d2_1 ==7) or (d2_1 ==9) or (d2_1 ==11) or (d2_1 ==13) or (d2_1 ==15) or (d2_1 ==17)) and ((d3_1 == 0) or (d3_1 ==1) or (d3_1 ==3) or (d3_1 ==5) or (d3_1 ==7) or (d3_1 ==9) or (d3_1 ==11) or (d3_1 ==13) or (d3_1 ==15) or (d3_1 ==17)):
    print ("Espectacular, lo conseguiste, tienes tres numeros de una misma paridad, duplicaremos tu puntaje total.")
    puntT1 = jug1punt1 * 2
elif ((resp1 == "impar") or (resp1 == "Impar")) and ((j1sumpunt2 == 0) or (j1sumpunt2 ==1) or (j1sumpunt2 ==3) or (j1sumpunt2 ==5) or (j1sumpunt2 ==7) or (j1sumpunt2 ==9) or (j1sumpunt2 ==11) or (j1sumpunt2 ==13) or (j1sumpunt2 ==15) or (j1sumpunt2 ==17)) and ((d1_1 != 0) or (d1_1 !=1) or (d1_1 !=3) or (d1_1 !=5) or (d1_1 !=7) or (d1_1 !=9) or (d1_1 !=11) or (d1_1 !=13) or (d1_1 !=15) or (d1_1 !=17)) or ((d2_1 != 0) or (d2_1 !=1) or (d2_1 !=3) or (d2_1 !=5) or (d2_1 !=7) or (d2_1 !=9) or (d2_1 !=11) or (d2_1 !=13) or (d2_1 !=15) or (d2_1 !=17)) or ((d3_1 != 0 or (d3_1 !=1) or (d3_1 !=3) or (d3_1 !=5) or (d3_1 !=7) or (d3_1 !=9) or (d3_1 !=11) or (d3_1 !=13) or (d3_1 !=15) or (d3_1 !=17))):
    print ("Bueno, obtuviste un resultado impar, sumaremos el", mayor1, "a tu puntaje total.")
    puntT1 = jug1punt1 + mayor1
elif ((resp1 == "par") or (resp1 == "Par")) and ((j1sumpunt2 % 2) != 0):
    print ("Que lastima campeón, obtuviste un resultado impar, restaremos el", menor1, "a tu puntaje total.")
    puntT1 = jug1punt1 - menor1
elif ((resp1 == "impar") or (resp1 == "Impar")) and ((j1sumpunt2 != 0) or (j1sumpunt2 !=1) or (j1sumpunt2 !=3) or (j1sumpunt2 !=5) or (j1sumpunt2 !=7) or (j1sumpunt2 !=9) or (j1sumpunt2 !=11) or (j1sumpunt2 !=13) or (j1sumpunt2 !=15) or (j1sumpunt2 !=17)):
    print ("Aaaah, te dió par, restaremos el", menor1, "a tu puntaje total.")
    puntT1 = jug1punt1 - menor1

time.sleep (3)
print ("Muy bien, proseguiremos con el jugador 2.")
time.sleep (2)
resp2 = input("|Jugador 2| Ingrese su apuesta, par o impar: ")
print (input("\n""|Jugador 2| Por favor, presionar 'enter' para lanzar su dado." ))
time.sleep (1)
print ("Sus dados empezaron a rodar")
time.sleep (2)
print ("Rodando...")
time.sleep (1)
print ("Rodando...")
time.sleep (1)
print ("Se estan parando y...")
time.sleep (3)
print ("Empezaron a rodar de vuelta")
time.sleep (1)
print ("Rodando...")
time.sleep (1)
print ("Rodando...")
time.sleep (2)

print ("Sacaste un", d1_2, "; un", d2_2,  "; y un", d3_2)
time.sleep (3)

if ((resp2 == "par") or (resp2 == "Par")) and ((j2sumpunt2 % 2) == 0) and ((d1_2 % 2) == 0) and ((d2_2 % 2) == 0) and ((d3_2 % 2) == 0):
    print ("Espectacular, lo conseguiste, tienes tres numeros de una misma paridad, duplicaremos tu puntaje total.")
    puntT2 = jug2punt1 * 2
elif ((resp2 == "par") or (resp2 == "Par")) and ((j2sumpunt2 % 2) == 0) and (((d1_2 % 2) != 0) or ((d2_2 % 2) != 0) or ((d3_2 % 2) != 0)):
    print ("Bueno, obtuviste un resultado par, sumaremos el", mayor2, "a tu puntaje total.")
    puntT2 = jug2punt1 + mayor2
elif ((resp2 == "impar") or (resp2 == "Impar")) and ((j2sumpunt2 == 0) or (j2sumpunt2 == 1) or (j2sumpunt2 ==3) or (j2sumpunt2 ==5) or (j2sumpunt2 ==7) or (j2sumpunt2 ==9) or (j2sumpunt2 ==11) or (j2sumpunt2 ==13) or (j2sumpunt2 ==15) or (j2sumpunt2 == 17)) and ((d1_2 == 0) or (d1_2 ==1) or (d1_2 ==3) or (d1_2 ==5) or (d1_2 ==7) or (d1_2 ==9) or (d1_2 ==11) or (d1_2 ==13) or (d1_2 ==15) or (d1_2 ==17)) and ((d2_2 == 0) or (d2_2 ==1) or (d2_2 ==3) or (d2_2 ==5) or (d2_2 ==7) or (d2_2 ==9) or (d2_2 ==11) or (d2_2 ==13) or (d2_2 ==15) or (d2_2 ==17)) and ((d3_2 == 0) or (d3_2 ==1) or (d3_2 ==3) or (d3_2 ==5) or (d3_2 ==7) or (d3_2 ==9) or (d3_2 ==11) or (d3_2 ==13) or (d3_2 ==15) or (d3_2 ==17)):
    print ("Espectacular, lo conseguiste, tienes tres numeros de una misma paridad, duplicaremos tu puntaje total.")
    puntT2 = jug2punt1 * 2
elif ((resp2 == "impar") or (resp2 == "Impar")) and ((j2sumpunt2 != 0) or (j2sumpunt2 !=1) or (j2sumpunt2 !=3) or (j2sumpunt2 !=5) or (j2sumpunt2 !=7) or (j2sumpunt2 !=9) or (j2sumpunt2 !=11) or (j2sumpunt2 !=13) or (j2sumpunt2 !=15) or (j2sumpunt2 !=17)) and (((d1_2 != 0) or (d1_2 !=1) or (d1_2 !=3) or (d1_2 !=5) or (d1_2 !=7) or (d1_2 !=9) or (d1_2 !=11) or (d1_2 !=13) or (d1_2 !=15) or (d1_2 !=17)) or ((d2_2 != 0) or (d2_2 !=1) or (d2_2 !=3) or (d2_2 !=5) or (d2_2 !=7) or (d2_2 !=9) or (d2_2 !=11) or (d2_2 !=13) or (d2_2 !=15) or (d2_2 !=17)) or ((d3_2 != 0) or (d3_2 !=1) or (d3_2 !=3) or (d3_2 !=5) or (d3_2 !=7) or (d3_2 !=9) or (d3_2 !=11) or (d3_2 !=13) or (d3_2 !=15) or (d3_2 !=17))):
    print ("Bueno, obtuviste un resultado impar, sumaremos el", mayor2, "a tu puntaje total.")
    puntT2 = jug2punt1 + mayor2
elif ((resp2 == "par") or (resp2 == "Par")) and ((j2sumpunt2 % 2) != 0):
    print ("Que lastima campeón, obtuviste un resultado impar, sumaremos el", menor2, "a tu puntaje total.")
    puntT2 = jug2punt1 - menor2
elif ((resp2 == "impar") or (resp2 == "Impar")) and ((j2sumpunt2 != 0) or (j2sumpunt2 !=1) or (j2sumpunt2 !=3) or (j2sumpunt2 !=5) or (j2sumpunt2 !=7) or (j2sumpunt2 !=9) or (j2sumpunt2 !=11) or (j2sumpunt2 !=13) or (j2sumpunt2 !=15) or (j2sumpunt2 !=17)):
    print ("Aaaah, te dió par, restaremos el", menor2, "a tu puntaje total.")
    puntT2 = jug2punt1 - menor2

time.sleep (2)
print("\n""¡¡Esplendido!!")
print("Hemos terminado.")
print("\n", Nombre1 + ",", "tu puntaje es...")
time.sleep (2)
print (puntT1)
print("\n", Nombre2 + ",", "en cambio, vos sacaste...")
time.sleep (2)
print (puntT2, "\n")
time.sleep (3)
if puntT1 == puntT2:
    print ("Empataron :o")
    time.sleep(4)
    print ("...")
    time.sleep(4)
    print ("Chau")
elif puntT1 < puntT2:
    print ("¡¡VAMOOOOS!!", Nombre2+ ",", "ganaste, recogé tu premio en la torre de pueblo lavanda, jeje.")
elif puntT1 > puntT2:
    print ("¡¡Felicitaciones!!", Nombre1 + ",", "ganaste, que grande que sos. ")
print(input())

