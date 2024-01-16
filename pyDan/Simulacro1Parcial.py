#Programa con menu de opciones para 4 diferentes programas.
import time
prog = 1
while prog:

    prog = int(input("Elija una de las siguientes opciones ingresando el numero correspondiente:"
                     "\n""1- Carrera de 3 barcos""\n""2- Secuencia de numeros enteros"
                     "\n""3- Contar cadena de caracteres"
                     "\n""4- Terminar programa"
                     "\n""Numerito aqui: "))
    print("\n")
    if prog == 1:
        print("A continuacion ingresaras el tiempo, en segundos, de 3 barcos, en base a esto el programa deducira al ganador.")
        time.sleep(2)

        barco1 = int(input("\n""Ingresar la cantidad de segundos que tardó el primer barco: "))
        time.sleep(2)

        barco2 = int(input("\n""Ingresar la cantidad de segundos que tardó el segundo barco: "))
        time.sleep(2)

        barco3 = int(input("\n""Ingresar la cantidad de segundos que tardó el tercer barco: "))
        time.sleep(3)
        print("\n")

        if (barco1 < barco2) and (barco1 < barco3):
            print("El barco número 1 fue el ganador con un tiempo record de", barco1,
                  "segundos, y una diferencia de", (barco2 - barco1),
                  "segundos con el segundo barco; y", (barco3 - barco1), "segundos con el tercero.")

        elif (barco2 < barco1) and (barco2 < barco3):
            print("El barco número 2 fue el ganador con un tiempo record de",
                  barco2, "segundos, y una diferencia de", (barco1 - barco2), "segundos con el primer barco; y",
                  (barco3 - barco2), "segundos con el tercero.")

        elif (barco3 < barco1) and (barco3 < barco2):
            print("El barco número 3 fue el ganador con un tiempo record de",
                  barco3, "segundos, y una diferencia de", (barco1 - barco3), "segundos con el primer barco; y",
                  (barco2 - barco3), "segundos con el segundo.")

        else:
            print("¡¡EMPATEEEE!! una lástima chavales.")

            print("\n")

    elif prog == 2:
        acum_multiplo_3 = acum_total = contador_multiplos_3 = 0

        n = int(input("Ingrese la cantidad de numeros a ingresar: "))

        for i in range(n):
            numero = int(input("Ingrese un número: "))
            if (numero % 3) == 0:
                acum_multiplo_3 += numero
                contador_multiplos_3 += 1
            acum_total += numero

        if n > 0:
            promedio_general = acum_total / n
            if contador_multiplos_3 > 0:
                promedio_multiplos_3 = acum_multiplo_3 / contador_multiplos_3
            else:
                promedio_multiplos_3 = 0

#Dividido en 3, si el resto es 0, es multiplo.

    elif prog == 3:

        print("A continuacion ingresara una cadena de digitos (oracion o frase) y el programa contara la cantidad de digitos.")
        suma = 0
        cadena = input("Ingrese la cadena para sumar los digitos: ")

        for digito in cadena:
            if digito >= "0" and digito <= "9":
                numero_repr_elcaract = int(digito)
                suma += numero_repr_elcaract
        print("La suma de los digitos es: ", suma)

    elif prog == 4:
        print("Gracias por participar")
        time.sleep(2)
        exit()

#Programa detecta error y vuelve.
    else:
        print("Error, ingresar nuevamente el número.")
        prog = input()
