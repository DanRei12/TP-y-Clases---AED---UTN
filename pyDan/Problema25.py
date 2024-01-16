# Empieza el programa.
print("Bienvenido a este nuevo programa.")

# Empezamos a definir la función. (La salida del menor es 'nd', el cuadrado es 'ndCuad' y el cubo es 'ndCubo'.)


def numbers(n1, n2, n3):
    # Aquí buscamos el menor entre 3 números.
    if n1 <= n2 and n1 <= n3:
        nd = n1
    elif n2 <= n3:
        nd = n2
    else:
        nd = n3

    ndCuad = pow(nd, 2)
    ndCubo = nd**3
    return nd, ndCuad, ndCubo

# El usuario introduce los numeros a procesar.


a = float(input("Introduzca aquí su primer número: "))
b = float(input("Introduzca aquí su segundo número: "))
c = float(input("Introduzca aquí su tercer número: "))

# Asignamos a las variables sus respectivos valores.
nd, ndCuad, ndCubo = numbers(a, b, c)

# Imprimimos para comprobar nuestros resultados..
print("El menor número es", nd, "; su cuadrado es", ndCuad, "y su cubo sería", ndCubo)

# Finaliza el programa.
exit()
