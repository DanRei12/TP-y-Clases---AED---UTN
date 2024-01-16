import time
#Empieza el programa
print("Bienvenido a este nuevo programa.\n")
prog = 1
while prog:
    # Elección de nuestras opciones.
    prog = int(input("Selecciona una de las siguientes opciones ingresando el número correspondiente:"
                     "\n""1- Temperatura en las provincias""\n""2- Carrera "
                     "\n""3- Contar pares en cadena de caracteres"
                     "\n""4- Terminar programa\n"
                     "\n""Numerito aqui: "))

    time.sleep(2)

    # Opción para el programa 1.
    if prog == 1:
        print("A continuacion ingresara la informacion de \n3 localidades provinciales, sus nombres y temperaturas (en grados Celsius).")

        # Ingresamos nombre de las localidades.
        nombloc1 = input("Ingresar nombre de la primera localidad: ")
        time.sleep(1)
        nombloc2 = input("\nIngresar nombre de la segunda localidad: ")
        time.sleep(1)
        nombloc3 = input("\nIngresar nombre de la tercera localidad: ")
        time.sleep(2)

        # Ingresamos temperatura de las localidades.
        temploc1 = int(input("\nIngresar temperatura de la primera localidad: "))
        temploc2 = int(input("\nIngresar temperatura de la segunda localidad: "))
        temploc3 = int(input("\nIngresar temperatura de la tercera localidad: "))
        time.sleep(1)

        # Pregunta para conocer la temperatura mas baja historicamente.
        quest = int(input("\nPreguntita ¿Cual es la menor temperatura historica en la provincia?\n- "))

        time.sleep(1)
        print("...")
        time.sleep(2)

        # Condicionales para conocer resultados
        if temploc1 <= temploc2 and temploc1 <= temploc3:
            nombmin = nombloc1
            menortemp = temploc1

        elif temploc2 <= temploc3:
            nombmin = nombloc2
            menortemp = temploc2

        else:
            nombmin = nombloc3
            menortemp = temploc3

        # Mostramos los resultados
        print("\nLa menor temperatura fue en", nombmin, "con una temperatura de", menortemp, "°")
        time.sleep(2)

        # Condicional para conocer si hay record.
        if menortemp < quest:
            print("Encontramos un frío record en", nombmin, "con una nueva temperatura record de", menortemp, "°")

    # Opción 2 para el programa.
    elif prog == 2:
        print("A continuación ingresara el tiempo(segundos) que demoraron los corredores.")
        time.sleep(1)

        # Definimos e introducimos nuestras variables.
        n = int(input("\nIngrese la cantidad de corredores: "))
        time.sleep(1)
        menor = 0
        mayor = 0
        suma = 0

        # Ciclo vital.
        for i in range(1, n+1):
            i2 = str(i)
            tiempo = int(input("\nIngrese la velocidad del corredor " + i2 +":"))
            suma += tiempo

            # Condicionales para establecer menores y mayores.
            if i == 1:
                menor = mayor = tiempo

            if tiempo < menor:
                menor = tiempo
            if tiempo > mayor:
                mayor = tiempo
            time.sleep(1)

        # Resolvemos nuestras variables fundamentales.
        d = int(input("\nIngresar la diferencia record que deberia tener el mejor corredor conforme al promedio \npara lograr establecer un record:"))
        prom = suma / n
        dif = prom - menor
        time.sleep(1)

        # Mostramos los resultados.
        print("\nEl menor tiempo fue de", menor, "segundos; el "
                                               "ultimo en llegar tardó", mayor, "segundos.\nEl promedio fue de", prom)
        time.sleep(1)

        # Calculamos si existe el record
        if dif > d:
            print("\n¡¡INCREIBLE!! Tiempo sobresaliente de diferencia", dif, "segundos con el promedio.")

    # Opción 3 para el programa.
    elif prog == 3:

        # Establecemos texto y contador.
        text = input("Ingrese abajo su texto a analizar.\n")
        cont = 0

        # Ciclo del programa.
        for i in text[text]:
            i = int(i)
            if i % 2 == 0:
                cont += i

        time.sleep(2)
        # Damos nuestros resultados.
        print("La suma numerica entre los digitos pares es de", cont)

    # Opción 4 (Terminar el programa)
    elif prog == 4:
        print("Usted selecciono terminar el programa :c")
        time.sleep(1)
        input("Press Start for exit")
        exit()

    # MEnsaje de error.
    else:
        print("¡¡ERROR!! Volver a ingresar su opción.")
        time.sleep(2)
    time.sleep(3)
    print("\n")
