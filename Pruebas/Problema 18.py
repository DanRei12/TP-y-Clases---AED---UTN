n = int(input("Ingresar un valor númerico para desarrollar su factorial: "))
f = 1
for i in range(1, n+1):
    f *= i

print("El factorial de", n, "es", f)
