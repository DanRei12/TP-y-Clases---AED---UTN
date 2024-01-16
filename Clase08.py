import random
import time
'''Programa simulando piedra, papel y tijeras. Aquí se vera con ingenio el uso de tuplas 
y el uso intensivo de las funciones random.'''

#Empieza el programa
print ("Este programa servira para que usted juegue contra la computadora en "
       "un juego de piedra, papel y tijeras, o en sus siglas (PPyT).")
time.sleep(2)
print ("¡¡Comencemos!!")
time.sleep(1)

#Ingreso de datos del usuario
jug1 = str(input("Ingresar el nombre del jugador 1: "))

#Variables a usar por el programa
elementos = ("Piedra", "Papel", "Tijera")

elog1 = ("Good name, broh"), ("Un nombre... curioso (-_-)"), ("WRYYYYY"), ("Ese nombre lo creo el mismisimo Satanás"), ("F por tu nombre")
nomR = ("Ricardo"), ("Roberto"), ("Ramiro"), ("Raúl"), ("Ronnie"), ("Rony"), ("Rooney"), ("Rodrigo"),("El Admin")
descrip = ("ha recorrido los largos valles de Konoha, aumentando su chakra entre juego y juego, hoy es conocido como el Hokage del PPyT."), ("estuvo presente en los juegos de Cell, en donde venció a Satan usando su papel. \nEstuvo en el enfrentamiento en Namek, lugar en donde asesino a Freezer con \nsu imponente piedra, ahora reconocido máximo guerrero del Planeta Vegeta, hoy es el Emperador del Universo 7"), ("marginado en la isla de Water Seven, él es un muchacho que obtuvo los poderes de la\n fruta 'Jankenpo Jankenpo no mi', logró capturar al famoso Gol D. Roger y detuvo los planes del \nmalvado Doflamingo, hoy es un reconocido almirante de la Marina")

#Empieza el juego
print (random.choice(elog1))
time.sleep(2)
jug2 = random.choice(nomR)
print ("Oh no, hoy tu contrincante sera...")
time.sleep(3)
print (jug2)
print (":o")
time.sleep(2)
print (jug2 + ",", random.choice(descrip))
input("\n Presione enter para continuar")

print ("-" * 90)
print ("\t \t \t Piedra... Papel o ¡¡TIJERAS!!")
print ("_" * 90)
time.sleep(2)
print ("\n Empecemos el juego, wiiii")
time.sleep(1)
print ("\t1 - Piedra \n\t2 - Papel \n\t3 - Tijera")
opc_nro_user = int(input("Ingresa tu valor (seleccionando un número del 1 al 3 porfis): "))
opc_user = elementos[opc_nro_user - 1]
print ("Chaval, has seleccionado ==>", opc_user)
time.sleep(2)
opc_compu = random.choice(elementos)
print (jug2, "-", '"Jajaja, te derrotare facilmente, muestra tu mano maldito, ¡¡TE DESTROZAREEEE!!"\n')
time.sleep(3)
print (jug2 + ",", "ha elegido", opc_compu)
time.sleep(2)
if opc_user == opc_compu:
    resultado = "¿¿QUEEE?? Em...patamos :O"
else:
    if (opc_user == "Piedra" and opc_compu == "Tijera") \
        or (opc_user == "Papel" and opc_compu == "Piedra") \
        or (opc_user == "Tijera" and opc_compu == "Papel"):
        resultado = "no... no... NOOOOOOOO\nMe derrotaste esta vez, pero no podras la proxima"
    else:
        resultado = "Te derrote, ahora... ¡¡MUEREEE!!"
print (resultado)
time.sleep(3)
print (time.strptime("To be continued", str))
print("(Ingresar 'Roundabout' de Yes)")
input()
