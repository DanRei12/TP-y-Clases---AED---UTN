# Enunciado
'''Turno 03 – Enunciado 02 [T3E2]:

Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes opciones:

1.)    Ingrese las tres notas obtenidas por un alumno en sus trabajos prácticos. Calcular y mostrar el promedio. Además, mostrar su calificación final, teniendo en cuenta que si el promedio es menor a 4 su calificación es "Insuficiente"; si el promedio es un valor mayor o igual a 4 pero menor a 7 su calificación es "Aprobado", y si el promedio es mayor o igual a 7 entonces su calificación es “Sobresaliente”.

2.)    Ingresar una secuencia de números, a razón de un número por vuelta de ciclo. La carga de dicha secuencia finaliza cuando se ingresa un cero. Se deberá determinar y mostrar la cantidad de números comprendidos entre 10 y 30 inclusive, y además el valor promedio de los números comprendidos en el intervalo ya mencionado.

3.)    Terminar el programa.
'''

__author__ = "Daniel_Reinoso_96264_1k3"

# Empieza el programa
print("Bienvenido a este nuevo programa.\n")
prog = 1
while prog:

    # Elección de nuestras opciones.
    prog = int(input("\nSelecciona una de las siguientes opciones ingresando el número correspondiente:"
                     "\n""1- Notas de un alumno""\n""2- Secuencia de números "
                     "\n""3- Terminar programa\n"
                     "\n""Ingresar su número de opción aquí: "))


    # Condicional para opción 1.
    if prog == 1:

        # Mostramos al usuario como funciona el programa.
        print("\nEsta opción le pedira tres notas, las promediara y le mostrara la calificación del alumno.")
        input("\nPresione enter para empezar.")

        # Ingreso de variables (notas) por teclado.
        nota1 = int(input("\nIngrese aquí la primera nota: "))
        nota2 = int(input("\nIngrese aquí la segunda nota: "))
        nota3 = int(input("\nIngrese aquí la tercera nota: "))

        # Promediamos las notas.
        prom = (nota1 + nota2 + nota3) / 3
        prom = round(prom, 2)

        # Mostramos el promedio
        print("\nEl promedio de las notas es de", prom, "\n")

        # Condicionales para poder dar una calificación.
        if prom < 4:
            print("Calificación: Insuficiente")
            print("Lo sentimos, a esforzarse mas.")

        elif prom >= 7:
            print("Calificación: Sobresaliente")
            print("Felicidades")

        # Nota (El "else" se presenta en caso de que la nota promediada sea igual o mayor a 4 y menor a 7)
        else:
            print("Calificación: Aprobado")
            print("Bien hecho, intentemos mejorar aún mas.")

    # Condicional para opción 2.
    elif prog == 2:

        # Explicamos el funcionamiento del programa al usuario.
        print("\nA continuación, ingresara una secuencia de números, la misma finalizara la misma cuando \nusted "
              "ingrese un 0, este programa determinara la cantidad de valores \nubicados entre el número 10 y el"
              " 30 inclusive, promediando estos al mismo tiempo.")
        input("\nPresione enter para empezar.")

        # Ingreso de número por teclado
        num = int(input("\nIngrese aquí el número: "))

        # Creamos los contadores.
        nums_en_interv = 0
        total = 0

        # Ciclo para definir variables.
        while num != 0:

            # Contador de números entre el intervalo y cantidad total de la suma de estos..
            if (num >= 10) and (num <= 30):
                nums_en_interv += 1
                total += num


            # Ingresamos nuevamente la variable para reiniciar correctamente el ciclo.
            num = int(input("\nIngrese aquí otro número(la carga finaliza con cero): "))

        # Calculamos el promedio de los números dentro del intervalo.
        prom = total // nums_en_interv

        # Mostramos los resultados.
        print("\nLa cantidad de números en el intervalo son", nums_en_interv, "y el promedio entre estos fue de", prom)

    # Condicional para opción 3 (Terminar programa)
    elif prog == 3:
        print("\nUsted decidió terminar este programa.")
        input("Pulse enter para terminar.")
        exit()

    # Opción en caso de que la opción seleccionada sea erronea.
    else:
        print("\nError, por favor, ingresar su opción nuevamente.")
