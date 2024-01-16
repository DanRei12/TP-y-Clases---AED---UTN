#Empieza el programa
print("Bienvenido a este nuevo programa.\n")
prog = 1
while prog:
    # Elección de nuestras opciones.
    prog = int(input("\nSelecciona una de las siguientes opciones ingresando el número correspondiente:"
                     "\n""1- Ventas de sucursales""\n""2- Analizar cantidad de pares "
                     "\n""3- Terminar programa\n"
                     "\n""Numerito aqui: "))


    # Opción para el programa 1.
    if prog == 1:

        print("En caso de que el promedio de la sucursal sea mayor a 100, cumplira con la condición dada por el programa.")

        # Ingresaremos las variables a trabajar.
        nombsuc1 = input("\nIngresar el nombre de la sucursal 1: ")
        cantsuc1 = int(input("\nIngresar la cantidad de ventas de esta sucursal: "))

        nombsuc2 = input("\nIngresar el nombre de la sucursal 2: ")
        cantsuc2 = int(input("\nIngresar la cantidad de ventas de esta sucursal: "))

        nombsuc3 = input("\nIngresar el nombre de la sucursal 3: ")
        cantsuc3 = int(input("\nIngresar la cantidad de ventas de esta sucursal: "))

        # Calcular el promedio.
        prom = (cantsuc1 + cantsuc2 + cantsuc3) / 3

        # Condicionales para calcular la menor venta.
        if cantsuc1 < cantsuc2 and cantsuc1 < cantsuc3:
            menorcant = cantsuc1
            nommenor = nombsuc1

        elif cantsuc2 < cantsuc3:
            menorcant = cantsuc2
            nommenor = nombsuc1

        else:
            menorcant = cantsuc3
            nommenor = nombsuc1

        # Imprimir primer resultado.
        print("\nLa menor cantidad de ventas fue de", menorcant, "y son pertenecientes a la sucursal", nommenor)

        # Condicional para calcular si el promedio cumple con la condición.
        if prom > 100:
            print("\nCon promedio de", prom, "se cumplió la condición que planteaba el programa.")

        else:
            print("\nCon promedio de", prom, "no se cumplió la condición que planteaba el programa.")

    # Opción para el programa 2.
    elif prog == 2:

        # Ingresamos el inicio del rango a calcular
        x = int(input("Ingrese aqui el valor de porcentaje de inicio del rango(entre 0 y 100)\n"))

        # Condicional para comprobar que la variable "x" se encuentre dentro del rango de posibles valores
        while x < 0 and x > 99:
            print("\nError, el valor introducido no esta entre lo especificado.")
            x = int(input("\nIngrese aqui nuevamente el valor de porcentaje de inicio del rango(entre 0 y 100)\n"))

        # Ingresamos el final del rango a calcular.
        y = int(input("\nIngrese aqui el valor de porcentaje del final del rango(entre 1 y 100)\n"))

        # Condicional para comprobar que la variable "y" se encuentre dentro del rango de posibles valores.
        while (y < 1 and y > 100) or y <= x:
            print("\nError, el valor introducido no esta entre lo especificado o no se relaciona correctamente con el valor 'x'.")
            y = int(input("\nIngrese aqui nuevamente el valor de porcentaje de final del rango(entre 0 y 100)\n"))

        # Definimos los contadores a utilizar.
        pares = 0
        total = 0

        num = int(input("\nIngrese aquí el número: "))
        xstr = str(x)
        ystr = str(y)

        # Condicional para definir variables
        while num != 0:
            total += 1

            # Contador de pares.
            if (num % 2 == 0) and (num > 50):
                pares += 1

            # Ingresamos nuevamente la variable para reiniciar correctamente el núcleo.
            num = int(input("\nIngrese aquí otro número(la carga finaliza con cero): "))

        print("\nHubieron", pares, "números pares.")

        # Sacamos el porcentaje
        porc = (pares * 100) // total

        print("\nEl porcentaje de numeros pares y mayores a 50 con respecto al total es de", porc, "%")

        print("\nRango: " + xstr + "% hasta " + ystr + "%")
        # Condicionales para comprobar que el porcentaje se encuentre dentro del rango planteado
        if (porc > x) and (porc < y):
            porc = str(porc)

            print("\nEl " + porc + "% dado esta dentro del rango planteado")

        else:
            porc = str(porc)
            print("\nEl " + porc + "% dado NO esta dentro del rango planteado")

    # Opción para el programa 3.
    elif prog == 3:
        s_on = input("¿Seguro?\n")
        if s_on == "Si" or s_on == "si":
            print("Usted selecciono terminar el programa.")
            input("\nPresione enter para finalizar.")
            exit()
        else:
            pass

    # Opción para el error.
    else:
        print("Error, opción invalida, favor de introducirla nuevamente, gracias\n")

# Finaliza el programa.
