n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

if n1 > n2 and n1 > n3:
    may = n1
    print ("El número mayor es:", may)
elif n2 > n3:
    may = n2
    print ("El número mayor es:", may)

else:
    may = n3
    print ("El número mayor es:", may)
print (input())
