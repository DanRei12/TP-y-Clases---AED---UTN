__Author__ = 'Cardoso Candela 1k3'

'''
Turno 03 – Enunciado 03 [T3E3]:

Desarrolle un programa completo en Python, controlado por menú de opciones, que incluya las siguientes opciones:

1.)    Ingrese desde teclado el nombre y edad de tres personas. Determine y muestre la edad promedio.
 Finalmente, muestre el nombre de cada una las personas cuya edad sea mayor a la edad promedio.

2.)    Ingrese por teclado una secuencia de n números enteros, a razón de uno por vuelta de ciclo 
(el número n se carga también por teclado). Determine y muestre cuántos de todos los números cargados 
eran mayores que un valor x (que se carga por teclado) pero que NO eran múltiplos de 3. 
Finalmente, muestre el porcentaje que ese conteo representa en el total de números cargados.

3.)    Terminar el programa.

'''

#Inicia el programa.

opt = None
num = 0
cont_num = 0

#Bienvendia al programa.

print('!!!Bienvendio al programa!!!')

while opt := int(input('\n1) Edad promedio y mayor. ' 
        '\n2) Secuencia de números enteros.' 
        '\n3) Terminar el programa.' 
        '\nIngrese su opción elegida del menú de opciones: ')):

    if opt == 1:

        #Se inicia el primer programa.

        print('\nBienvenido al programa donde se determina y muestra la edad promedio de 3 personas.'
              'En éste programa deben ingresar nombre de tres personas y sus respectivas edades, \nel programa calculará el'
              'promedio entre los tres y luego dirá \nel mayor que supere el promedio.')

        #Se ingresan las edades y los nombres.

        nom1 = input('Ingrese nombre de la primera persona: ')
        age1 = int(input('Ingrese edad de la primera persona: '))

        nom2 = input('Ingrese nombre de la primera persona: ')
        age2 = int(input('Ingrese edad de la primera persona: '))

        nom3 = input('Ingrese nombre de la primera persona: ')
        age3 = int(input('Ingrese edad de la primera persona: '))

        #Se calcula el promedio.

        prom_ages = (age1 + age2 + age3) // 3
        print('El promedio de edades entre los tres es: ', prom_ages)

        #Se calcula el mayor de los 3.
        if prom_ages < age1 and age1 > age2 and age1 > age3:
            print('El mayor a la edad promedio es:', nom1)


        elif prom_ages < age2 and age2 > age3:
            print('El mayor a la edad promedio es: ', nom2)

        else:
            print('El mayor a la edad promedio es: ', nom3)






    elif opt == 2:
        #Se inicia el segundo programa.
        print('\nElegiste la opción 2.'
              '\nBienvenido al programa. En este programa usted deberá cargar una secuencia de números enteros. '
              '\nEl programa lo que hará será mostrar un porcentaje de los números cargados.')


        n = int(input('Ingrese la cantidad de numeros a analizar: '))
        x = int(input("Ingrese la cantidad por la que tienen que ser mayor los numeros a ingresar: "))

        contador_del_condicional = 0

        for num in range(n):
            numero = int(input("Ingrese su número: "))
            if (numero > x) and (numero % 3 != 0):
                contador_del_condicional += 1

        porc = (contador_del_condicional * 100) // n
        porc = str(porc)

        print("La cantidad de números que cumplen la condición son", contador_del_condicional)
        print("Representa un porcentaje del " + porc + "% con respecto al total.")



    elif opt == 3:
        #Se produce la salida del programa y se termina.
        print('\nElegiste la opción 3.'
              '\n"Salir"'
              '\n Que le vaya bien, saludos.')
        quit()

