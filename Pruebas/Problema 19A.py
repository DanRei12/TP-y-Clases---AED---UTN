may = int(input("Ingrese el primer valor"))
p = int(input("Ingrese la cantidad de numeros que va a ingresar en el programa:"))
for i in range(p):
    l = int(input("Ingrese otro valor: "))
    may = max(l, may)
    print(may, "es el número mayor.")
