#Comenzamos visualizando y aprendiendo la funcion tuple.
t = tuple("Hola mundo")
print(t)

t = (25, 10, 35)
print("\n", t)

t = "Ricardo", "Mariano", "Mamarracho"
print("\n", t[1])

f = 30, "Marzo", 2021
print("\n""La fecha actual es:", f)
print("\n""La fecha tiene", len(f), "partes.")

#Aqui visualizamos una manera facil de cambiar valores de una función tuple.
g = 28, f[1], f[2]
print ("\n""La fecha ahora es", g)

#Ahora el ejercicio se vuelve mas confuso ya que utilizamos la misma variable para cambiar su propia secuencia.
f = 20, f[1], f[2]
print ("\n""Viajamos al tiempo y la fecha ahora es", f)


# Lo siguiente esta mal.
#f[0] = 28
#print("El dia de hoy es:", f[0])

#Asignación
a = 3
x, y = 2 * a, 4 * a
print ("\n""Valor de x:", x)
print ("Valor de y:", y)

#Empaquetar
sec = 5, 8, 10
print ("\n""Secuencias", sec)

#Desempaquetar
a, b, c = sec
print ("\n""Valor de a:", a)
print ("Valor de b:", b)
print ("Valor de c:", c)

#Aqui podemos ejecutar las "reglas" al reves, pudiendo asignar mas rapidamente valores a nuestras variables.
x, y = input("\n""Ingrese un valor para x: "), input("Ingrese un valor para y: ")
print ("\n""Valor de X:", x)
print ("Valor de Y:", y)

#Aqui aprendemos la funcion aux y la manera de intercambiar valores entre distintas variables.
a = 5
b = 4
c = 8
print ("\n""Datos", a,",", b, "y", c)
aux = a
a = b
b = aux
print ("\n""Intercambio de valores", a, "y", b)

a, b, c = c, a, b
print ("\n""Intercambio con tuplas", a, ",", b, "y", c)
