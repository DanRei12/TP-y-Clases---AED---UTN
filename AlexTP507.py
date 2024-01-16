#TRABAJO PRACTICO
# "EL JUEGO DE DOS O TRES"
#
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@....%%%......%%%.@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@.....................@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@.......................@@@@@@
#@@@@@@@@@@@@@@@@@@@..............%%%......%%%.@@@@
#@@@@@@@@@@@@@@@@@@......%%@....................@@@
#@@@@@@@@@@@@@@@@@@......%%@.......@@.......@@..@@@
#@@@@@@@@@@@@@@@@@@@..............%%.......%@..@@@@
#@@@@@@@@@@@@@@@@@@@@@...............%%@.....@@@@@@
#@@@@@@@@@@@@@@@@...........................@@@@@@@
#@@@@@@@@@@@........@@.........%%@....%%@.@@@@@@@@@
#@@@@@@@@@..........%%%%..........%@@@@@@@@@@@@@@@@
#@@@@@@@@.%%%......................@@@@@@@@@@@@@@@@
#@@@@@@@@.%%%..................%%%.@@@@@@@@@@@@@@@@
#@@@@@@@@..........................@@@@@@@@@@@@@@@@
#@@@@@@@@...................%%%....@@@@@@@@@@@@@@@@
#@@@@@@@@..........................@@@@@@@@@@@@@@@@
#@@@@@@@@........%%%...............@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@....%%%....%%%....@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@......... @@@@@@@@@@@@@@@@@@@@@@@@







#Imports■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
import random
import PySimpleGUI as psg


#Bienvenida■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
psg.popup("■■■■■■■ El Juego de Dos o Tres ■■■■■■■\n", title="Bienvenida")


#Entrada de datos■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

P1 = str(psg.popup_get_text("Bienvenido al Juego de Dados!\nPor favor, ingrese el nombre del primer jugador:\n", "Identificación"))
P2 = str(psg.popup_get_text("Bien, ahora ingrese el nombre del segundo jugador:\n", "Identificación"))

psg.popup("Esta todo listo, juguemos!")

#Proceso■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■



    #Primera Ronda■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


#PLAYER 1···································································································


P1Score= 0
Ex= str("!")
psg.popup("Es el turno de",P1 + Ex)

P1FR= random.randint(1,6)

psg.popup("Primer dado:",P1FR,"Preciona OK para continuar con el siguiente dado!")

P1SR= random.randint(1,6)

psg.popup("Segundo dado:",P1SR,"Preciona OK para continuar con el siguiente dado!")

P1TR= random.randint(1,6)

psg.popup("Tercer dado:",P1TR,"Preciona OK para continuar")



if P1FR == P1SR == P1TR:
    P1Score= P1Score + 6
    psg.popup("Felicidades", P1,"tu puntaje es:",P1Score)


elif P1FR == P1SR != P1TR:
    psg.popup(P1," volvera lanzar!")
    P1TR= random.randint(1,6)

    if P1FR == P1SR == P1TR:
        P1Score= P1Score + 6
        psg.popup("Es un",P1TR)
        psg.popup("Felicidades", P1,"tu puntaje es:",P1Score)

    elif P1FR == P1SR != P1TR:
        P1Score= P1Score + 3
        psg.popup("Ooh,",P1,",mala suerte")
        psg.popup("Es un",P1TR)
        psg.popup("Felicidades", P1,"tu puntaje es:",P1Score)

elif P1FR == P1TR != P1SR:
    psg.popup(P1," volvera lanzar!")
    P1SR= random.randint(1,6)

    if P1FR == P1SR == P1TR:
        P1Score= P1Score + 6
        psg.popup("Es un",P1SR)
        psg.popup("Felicidades", P1,"tu puntaje es:",P1Score)

    elif P1FR == P1TR != P1SR:
        P1Score= P1Score + 3
        psg.popup("Ooh,",P1,",mala suerte")
        psg.popup("Es un",P1SR)
        psg.popup("Felicidades", P1,"tu puntaje es:",P1Score)

elif P1SR == P1TR != P1FR:
    psg.popup(P1," volvera lanzar!")
    P1FR= random.randint(1,6)

    if P1FR == P1SR == P1TR:
        P1Score= P1Score + 6
        psg.popup("Es un",P1SR)
        psg.popup("Felicidades", P1,"tu puntaje es:",P1Score)

    elif P1SR == P1TR != P1FR:
        P1Score= P1Score + 3
        psg.popup("Ooh,",P1,",mala suerte")
        psg.popup("Es un",P1FR)
        psg.popup("Felicidades", P1,"tu puntaje es:",P1Score)



else:
    P1Score= P1Score + 0
    psg.popup("Mala suerte", P1)
    psg.popup("Que mal,", P1,",tu puntaje es:",P1Score)

#PLAYER 2···································································································


P2Score= 0
psg.popup("Es el turno de",P2 + Ex)

P2FR= random.randint(1,6)

psg.popup("Primer dado:",P2FR,"Preciona OK para continuar con el siguiente dado!")

P2SR= random.randint(1,6)

psg.popup("Segundo dado:",P2SR,"Preciona OK para continuar con el siguiente dado!")

P2TR= random.randint(1,6)

psg.popup("Tercer dado:",P2TR,"Preciona OK para continuar")



if P2FR == P2SR == P2TR:
    P2Score= P2Score + 6
    psg.popup("Felicidades", P2,"tu puntaje es:",P2Score)


elif P2FR == P2SR != P2TR:
    psg.popup(P2," volvera lanzar!")
    P2TR= random.randint(1,6)

    if P2FR == P2SR == P2TR:
        P2Score= P2Score + 6
        psg.popup("Felicidades", P2,"tu puntaje es:",P2Score)

    elif P2FR == P2SR != P2TR:
        P2Score= P2Score + 3
        psg.popup("Ooh,",P2,",mala suerte")
        psg.popup("Es un",P2TR)
        psg.popup("Felicidades", P2,"tu puntaje es:",P2Score)

elif P2FR == P2TR != P2SR:
    psg.popup(P2," volvera lanzar!")
    P2SR= random.randint(1,6)

    if P2FR == P2SR == P2TR:
        P2Score= P2Score + 6
        psg.popup("Felicidades", P2,"tu puntaje es:",P2Score)

    elif P2FR == P2TR != P2SR:
        P2Score= P2Score + 3
        psg.popup(P2," mala suerte")
        psg.popup("Es un",P2SR)
        psg.popup("Felicidades", P2,"tu puntaje es:",P2Score)

elif P2SR == P2TR != P2FR:
    psg.popup(P2," volvera lanzar!")
    P2FR= random.randint(1,6)

    if P2FR == P2SR == P2TR:
        P2Score= P2Score + 6
        psg.popup("Es un",P2SR)
        psg.popup("Felicidades", P2,"tu puntaje es:",P2Score)

    elif P2SR == P2TR != P2FR:
        P2Score= P2Score + 3
        psg.popup("Ooh,",P2,",mala suerte")
        psg.popup("Es un",P2FR)
        psg.popup("Felicidades", P2,"tu puntaje es:",P2Score)


else:
    P2Score= P2Score + 0
    psg.popup("Mala suerte ", P2)
    psg.popup("Que mal,", P2,",tu puntaje es:",P2Score)

psg.popup("Termina la primera ronda\n", P1, " tiene ",P1Score, "puntos\n", P2, " tiene ",P2Score, "puntos\n",title="Conclución")

    #Segunda Ronda■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■


#Bienvenida···································································································
psg.popup("Comencemos la segunda ronda!",title= "2da Ronda")

#PLAYER1···································································································
psg.popup("Es el turno de",P1 + Ex)

P1FR= random.randint(1,6)

psg.popup("Primer dado:",P1FR,"Preciona OK para continuar con el siguiente dado!")

P1SR= random.randint(1,6)

psg.popup("Segundo dado:",P1SR,"Preciona OK para continuar con el siguiente dado!")

P1TR= random.randint(1,6)

psg.popup("Tercer dado:",P1TR,"Preciona OK para continuar")

BET= int(psg.popup_get_text("Es la suma de tus dados un número par o impar?\nPar: 0\nImpar: 1\n,","Apuesta"))
BETVAL=0
BET= 0 + BET
if BET == 0:
    VAL= P1FR+P1SR+P1TR
    if VAL % 2 == 0:
        SS= 0
        psg.popup("Acertaste!")
        if P1FR >= P1SR and P1FR >= P1TR:
            BETVAL= BETVAL + P1FR
        elif P1SR >= P1FR and P1SR >= P1TR:
            BETVAL= BETVAL + P1SR
        elif P1TR >= P1FR and P1TR >= P1SR:
            BETVAL= BETVAL + P1TR
    else:
        SS= 1
        psg.popup("Le erraste!")
        if P1FR <= P1SR and P1FR <= P1TR:
            BETVAL=  BETVAL + P1FR
        elif P1SR <= P1FR and P1SR <= P1TR:
            BETVAL=  BETVAL + P1SR
        elif P1TR <= P1FR and P1TR <= P1SR:
            BETVAL=  BETVAL + P1TR
elif BET == 1 :
    VAL= P1FR+P1SR+P1TR
    if VAL % 2 == 0:
        SS= 1
        psg.popup("Le erraste!")
        if P1FR <= P1SR and P1FR <= P1TR:
            BETVAL=  BETVAL + P1FR
        elif P1SR <= P1FR and P1SR <= P1TR:
            BETVAL=  BETVAL + P1SR
        elif P1TR <= P1FR and P1TR <= P1SR:
            BETVAL=  BETVAL + P1TR
    else:
        SS= 0
        psg.popup("Acertaste!")
        if P1FR >= P1SR and P1FR >= P1TR:
            BETVAL=  BETVAL + P1FR
        elif P1SR >= P1FR and P1SR >= P1TR:
            BETVAL=  BETVAL + P1SR
        elif P1TR >= P1FR and P1TR >= P1SR:
            BETVAL=  BETVAL + P1TR

else:
    psg.popup("Disculpeme don comedia,",BET,"no es un valor valido (╬ ಠ益ಠ)")
    SS= 1

if BET == 0 and SS == 0 and P1FR % 2 == 0 and P1SR % 2 == 0 and P1TR % 2 == 0:
    P1Score= ( P1Score + (BETVAL * 2))
    psg.popup("Tus dados tambien son par!")
    psg.popup("Ahora tienes ", P1Score," puntos!")

elif BET == 0 and SS == 0 and P1FR % 2 != 0 and P1SR % 2 != 0 and P1TR % 2 != 0:
    P1Score= (P1Score + BETVAL)
    psg.popup("Ahora tienes ", P1Score," puntos!")

elif BET == 1 and SS == 0 and P1FR % 2 != 0 and P1SR % 2 != 0 and P1TR % 2 != 0:
    P1Score= ( P1Score + (BETVAL * 2))
    psg.popup("Tus dados tambien son impar!")
    psg.popup("Ahora tienes ", P1Score," puntos!")

elif BET == 1 and SS == 0 and P1FR % 2 == 0 and P1SR % 2 == 0 and P1TR % 2 == 0:
    P1Score= (P1Score + BETVAL)
    psg.popup("Ahora tienes ", P1Score," puntos!")

elif SS == 1:
    P1Score= P1Score - BETVAL
    psg.popup("Que mal ",P1," hora tienes ", P1Score," puntos")

else: pass

#PLAYER2·············································································································
psg.popup("Es el turno de",P2 + Ex)

P2FR= random.randint(1,6)

psg.popup("Primer dado:",P2FR,"Preciona OK para continuar con el siguiente dado!")

P2SR= random.randint(1,6)

psg.popup("Segundo dado:",P2SR,"Preciona OK para continuar con el siguiente dado!")

P2TR= random.randint(1,6)

psg.popup("Tercer dado:",P2TR,"Preciona OK para continuar")

BET= int(psg.popup_get_text("Es la suma de tus dados un número par o impar?\nPar: 0\nImpar: 1","Apuesta"))
BETVAL=0
BET= 0 + BET
VAL= P2FR+P2SR+P2TR
if BET == 0:
    if VAL % 2 == 0:
        SS= 0
        psg.popup("Acertaste!")
        if P2FR >= P2SR and P2FR >= P2TR:
            BETVAL= BETVAL + P2FR
        elif P2SR >= P2FR and P2SR >= P2TR:
            BETVAL= BETVAL + P2SR
        elif P2TR >= P2FR and P2TR >= P2SR:
            BETVAL= BETVAL + P2TR
    else:
        SS= 1
        psg.popup("Le erraste!")
        if P2FR <= P2SR and P2FR <= P2TR:
            BETVAL=  BETVAL + P2FR
        elif P2SR <= P2FR and P2SR <= P2TR:
            BETVAL=  BETVAL + P2SR
        elif P2TR <= P2FR and P2TR <= P2SR:
            BETVAL=  BETVAL + P2TR
elif  BET == 1:
        if VAL % 2 == 0:
            SS= 1
            psg.popup("Le erraste!")
        if P2FR <= P2SR and P2FR <= P2TR:
            BETVAL=  BETVAL + P2FR
        elif P2SR <= P2FR and P2SR <= P2TR:
            BETVAL=  BETVAL + P2SR
        elif P2TR <= P2FR and P2TR <= P2SR:
            BETVAL=  BETVAL + P2TR
        else:
            SS= 0
            psg.popup("Acertaste!")
        if P2FR >= P2SR and P2FR >= P2TR:
            BETVAL=  BETVAL + P2FR
        elif P2SR >= P2FR and P2SR >= P2TR:
            BETVAL=  BETVAL + P2SR
        elif P2TR >= P2FR and P2TR >= P2SR:
            BETVAL=  BETVAL + P2TR
else:
    psg.popup("Disculpeme don comedia,",BET,"no es un valor valido (╬ ಠ益ಠ)")
    SS= 1
if BET == 0 and SS == 0 and P2FR % 2 == 0 and P2SR % 2 == 0 and P2TR % 2 == 0:
    P2Score= ( P2Score + (BETVAL * 2))
    psg.popup("Tus dados tambien son par!")
    psg.popup("Ahora tienes ", P2Score," puntos!")

elif BET == 0 and SS == 0 and P2FR % 2 != 0 and P2SR % 2 != 0 and P2TR % 2 != 0:
    P2Score= (P2Score + BETVAL)
    psg.popup("Ahora tienes ", P2Score," puntos!")

elif BET == 1 and SS == 0 and P2FR % 2 != 0 and P2SR % 2 != 0 and P2TR % 2 != 0:
    P2Score= ( P2Score + (BETVAL * 2))
    psg.popup("Tus dados tambien son impar!")
    psg.popup("Ahora tienes ", P2Score," puntos!")

elif BET == 1 and SS == 0 and P2FR % 2 == 0 and P2SR % 2 == 0 and P2TR % 2 == 0:
    P2Score= (P2Score + BETVAL)
    psg.popup("Ahora tienes ", P2Score," puntos!")

elif SS == 1:
    P2Score= P2Score - BETVAL
    psg.popup("Que mal ",P2," hora tienes ", P2Score," puntos")

else: pass






#RESULTADOS■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
psg.popup("Preparense para los resultados!")
psg.popup(".")
psg.popup("..")
psg.popup("...")
if P1Score > P2Score:
    psg.popup(P1, " es el ganador ☺!")
    psg.popup("Gracias por jugar!")
elif P1Score == P2Score:
    psg.popup("Es un empate!")
    psg.popup("Gracias por jugar!")
else:
    psg.popup(P2, " es el ganador ☺!")
    psg.popup("Gracias por jugar!")



#CODIGO POR:
#ERAD ALEX JEREMÍAS
#(((((((((((((((((((((((((((,..............,(((((((((((((((((((((((,..................,,.,,,,....,...
#((((((((((((((((((((((((((((....................,(((((((((((((((.,............,##((.,..,.,,.,,,,((#/
#((((((((((((((((((((((((((((((........................,((((((.,...........(((......................,
#((((((((((((((((((((((((((((((#...........................,...........*((,,.......(((((((...........
#((((((((((((((((((((((((((((((((,......(((,........................,((............((((((((#,........
#((((((((((((((((((((((((((((((((((......(((((#....................(.,....*,,.......(((((((((,.......
#((((((((((((((((((((((((((((((((((((.....((((((((.,.............(/.....((((((#......,((((((.,......,
#(((((((((((((((((((((((((((((((((((((,....,(((((((((,.........,(......,((((((((,............,,.(((((
#(((((((((((((((((((((((((((((((((((((((....,((((((((((#.....,.(........*((((((((........,.(..(((((((
#(((((((((((((((((((((((((((((((((((((((*,...,((((((((((......(,........,,(((((((......((((((((((((((
#((((((((((((((((((((((((((((((((((............(((((((((......(...............,....((((((((((((((((((
#((((((((((((((((((((((((((((((((((((..,((((((((((((((((,....((...................(((((((((((((((((((
#((((((((((((((((((((((((((((((((((((((../(((((((((((((((,..,((............,((((((((((((((((((((((((.
#((((((((((((((((((((((((((((((((((#,..*/.,((((((((((((((,,..,(..........(((((((((((((((((((((((((...
#((((((((((((((((((((((((((((((((((((((((#..((((((((((((((....(......,.((((((((((((((((((((((((,.....
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((..,((........,#(((((((((((((((#,..........
#(((((((((((((((((((((((((((((((((((((((((((((((((,.,(((((((.,.((,............,.....,................
#(((((((((((((((((((((((((((((((((((((((((((((((......((((((((,,((,..................................
#((((((((((((((((((((((((((((((((((((((*..((((((.......((((((((..*(..................................
#(((((((((((((((((((((((((((((((((((((,......,,((......,(((((((,...((,...............................
#((((((((((((((((((((((((((((((((((((....................,(((((,.....(((,,...........................
#((((((((((((((((((((((((((((((((((((((,........................((,..((((((#.,.,.....................
#(((((((((((((((((((((((((((((((((((((((((((...............................,,,,.,....................
#((((((((((((((((((((((((((((((((((((((#.............................................................
#(((((((((((((((((((((((((((((((((((((...............................................................
#((((((((((((((((((((((((((((((((((((((..............................................................
#(((((((((((((((((((((((((((((((((((((((,.*#(((..............................,,......................
#(((((((((((((((((((((((((((((((((((((((((((/..........*((((((((((((((((((((((.......................
#((((((((((((((((((((((((((((((((((((((((((#.......,(((((((((((((((((((((((((........................
#((((((((((((((((((((((((((((((((((((((((((((,,.,.(((((((((((((((((((((((((((........................


#HEE-HOO!
