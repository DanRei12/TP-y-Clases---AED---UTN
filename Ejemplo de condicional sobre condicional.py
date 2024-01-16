import random
t = random.randrange(1, 7)
print(t)
print (input())
f = input("Introducir un saludo:")
e = input("Introducir un sustantivo:")
if f == "Hola":
    if e == "mundo":
        print(f, e)
    else: print ("Ese saludo no me gusta :(")
else: print ("Decime hola, soretin")
print(input())

