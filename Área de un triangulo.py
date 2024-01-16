'''Este programa servira para el calculo de un area de un triangulo :D
Aquí tendra que introducir la base y se tomara el valor de la altura como B al cuadrado.'''
print ("Este programa servira para el calculo del área de un triangulo, teniendo en cuenta el valor de la altura como la base al cuadrado.")
base = float(input("Ingrese un valor para la base: "))
a = str(input("¿Quiere ingresar el valor de la altura? (En caso de que la respuesta sea no, se tomara por valor el mencionado anteriormente.)""\n"))
if a == ("si"):
    h = float(input("Ingrese un valor para la altura: "))
else: h = (base ** 2)
Atriang = (base * h) / 2
print ("El área del triangúlo será igual a:", Atriang)
print (input())
 # Programa completo.
