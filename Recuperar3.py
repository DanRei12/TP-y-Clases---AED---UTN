G = 6.673 * pow(10, -8) #Esta se llama constante de gravitación universal.
print("=" * 90)
print("Este programa calculara la fuerza, tomando referencia la constante gravitacional universal.")
print("=" * 90)
m1 = float(input("Ingrese la primera masa: "))
m2 = float(input("Ingrese la segunda masa: "))
d = float(input("Ingrese la distancia: "))
F = (G * m1 * m2) / d ** 2
print ("La intensidad de la fuerza sera igual a", F)


