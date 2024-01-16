#Empieza el programa
n = int(input("Ingrese la cantidad de numeros que desea ingresar: "))
print (n)
input()
may = None
for i in range(n):
    number = float(input("Ingrese un valor:"))
    if i == 0 or number >= may:
        may = number

print ("El mayor número es", may)
