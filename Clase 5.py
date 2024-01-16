n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercero número: "))
if n1 > n2 and n1 > n3:
    mensaje ="El número mayor es el primero:", n1
elif n1 < n2 and n2 > n3:
    mensaje = "El número mayor es el segundo:", n2
else:
    mensaje = "El numero mayor es el tercero:", n3
print (mensaje)
print (input())
