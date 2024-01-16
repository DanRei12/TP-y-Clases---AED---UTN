import time
n = int(input("Ingrese el primer valor"))
p = 9000
while n:
    for i in range(p):
        l = int(input("Ingrese otro valor: "))
        n = max(l, n)
        print(n, "es el número mayor.")
        if l == 0:
            print("Proceso finalizado por ingreso de 0")
            time.sleep(2)
            exit()

