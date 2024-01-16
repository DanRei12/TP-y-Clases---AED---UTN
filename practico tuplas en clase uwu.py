import random
Saludos = "Hola", "Holi", "Cómo estas", "Te veo", "I see you", "Qué pasa"
Insultos = "Puto", "Trolo", "Gay", "Gei", "Putita", "Perra", "Nenita"
print (random.choice(Saludos), random.choice(Insultos))
print (input())

a = float(input("Favor de ingresar el primer número: "))
b = float(input("Favor de ingresar el segundo número: "))
c = float(input("Favor de ingresar el tercer número: "))

may = max(a, b, c)
men = min(a, b, c)
print ("El número mayor es", may)
print ("Mientras que el menor es", men)
print (input())
