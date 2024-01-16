'''import time
#Empieza el programa
may = 0
number = float(input("Ingrese el primer valor:"))
while number != 0:
    if number > may:
        may = number
    elif number == 0:
        break
    print ("El mayor número es", may)
    number = float(input("Ingrese otro valor:"))
input()
print ("El mayor número es", may)
time.sleep(1)
print ("Terminamos...")
time.sleep(4)
exit()
'''
Numero = 1984
ContadorParesMay50= 0
Vueltas= 0
x = int(input("seleccione el valor de x \n"))
y = int(input("seleccione el valor de y \n"))

Numero = int(input("ingrese un numero \n"))
while Numero != 0:
    Numero = int(input("ingrese otro numero \n"))
    Vueltas = Vueltas + 1
    if (Numero % 2 == 0) and (Numero > 50) :
        ContadorParesMay50 = ContadorParesMay50 + 1

    Numero = int(input("ingrese otro numero \n"))

Porcentaje= (ContadorParesMay50 * 100) // Vueltas
print("El porcentaje de pares mayores a 50 es: ", Porcentaje)
if Porcentaje > x and Porcentaje < y :
    print("el porcentaje se encuentra en el rango indicado")
else:
    print("el porcentaje no se encuentra en el rango indicado")
