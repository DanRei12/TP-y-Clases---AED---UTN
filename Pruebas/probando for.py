import time
import random

nombres = ("Ricky", "Mariano", "Lalo Landa")
apellidos = ("Miguelez", "Queen", "Coon")
print (nombres)
for nom in random.choices(nombres):
    for ape in random.choices(apellidos):
        print (nom, ape)

ciudad = "Córdoba"
for c in ciudad:
    print (c)

for i in range (1, 6):
    print (i)
for e in range (6):
    print (e)
input()

n = int(input("¿Cuantos números pares desea mostrar?:"))
for par in range (0, 2*n, 2):
    print (par)
input()

a = 0
n = int(input("Ingrese la cantidad de números a ingresar: "))
for i in range (n):
    num = int(input("Ingrese un número: "))
    if num < 0:
        a += 1
    print ("Cantidad de negativos cargados:", a)
