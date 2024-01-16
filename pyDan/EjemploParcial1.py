'''1)	Desarrollar un programa completo en Python, que, a través de un menú de opciones, ejecute los siguientes puntos:

1) Ingresar el nombre de tres atletas, además ingrese también los tiempos
que esos lograron en su actividad deportiva (expresados en segundos),
informe cual fue el nombre del atleta que gano la competición, además
indicar con un mensaje que si el tiempo del ganador
es menor a 850 segundos batió el récord de la actividad.

2) Ingresar un texto, el mismo termina con punto, recorrer el texto
carácter a carácter y determinar cuántas letras 'p' hay en el texto,
cuantas letras 'j' hay en el texto. Además indique cual es el porcentaje
que cada conteo representa sobre el total de caracteres del texto.

3)Terminar el Programa
'''

#Empieza el programa
print("Bienvenido a este nuevo programa.\n")
prog = 1
while prog:
    # Elección de nuestras opciones.
    prog = int(input("Selecciona una de las siguientes opciones ingresando el número correspondiente:"
                     "\n""1- Competición de atletismo""\n""2- Texto(analisis de 'p' y 'j') "
                     "\n""3- Terminar programa\n"
                     "\n""Numerito aqui: "))


    # Opción para el programa 1.
    if prog == 1:
        print("A continuación ingresara el nombre y la cantidad recorrida por 3 atletas, posteriormente, le mostraremos el ganador.")

        atleta1 = input("¿Cómo se llama el primer competidor?\n")
        atleta2 = input("\n¿Cual es el nombre del segundo competidor?\n")
        atleta3 = input("\nIngresar el nombre del tercer competidor.\n")

        record = 850

        print("A continuacion ingresara el tiempo (en segundos) que logró cada corredor, tener en cuenta que el record es de 860 segundos")

        tAtl1 = int(input("Ingresar el tiempo logrado por", atleta1 + ":"))
        tAtl2 = int(input("Ingresar el tiempo logrado por", atleta2 + ":"))
        tAtl3 = int(input("Ingresar el tiempo logrado por", atleta3 + ":"))

        if tAtl1 < tAtl2 and tAtl1 < tAtl3:
            winner = tAtl1
            nomwinner = atleta1

        if tAtl2 < tAtl3:
            winner = tAtl2
            nomwinner = atleta2

        else:
            winner = tAtl3
            nomwinner = atleta3

        print("¡¡FELICIDADES", nomwinner + "!! Ganaste, con un tiempo de", winner, "segundos.")

        if winner < record:
            print("Ademas, has batido un nuevo record, tu tiempo de", winner, "segundos es mejor que el record anterior de", record, "segundos.")

    elif prog == 2:
        print("Hola")

    elif prog == 3:
        print("Seleccionaste finalizar este programa :c")
        input("Presiona enter para finalizar.")
        exit()

    else:
        print("Error, ingresar su opción nuevamente.")
