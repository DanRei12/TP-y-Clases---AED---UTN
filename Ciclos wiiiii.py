'''Programa para calcular la cantidad de negativos ue haya introducido el usuario.'''
cont = 0
n = int(input("Ingresar un número: "))
while n != 0:
    if n < 0:
        cont = cont + 1
        n = int(input("Ingresar un númeraso: "))
    else: n = int(input("Ingresar un númerito: "))


print ("La cantidad de negativos que ingresaste es:", cont)
input()
