import random
import time
print ("_" * 120)
print ("\t""\t""                                |Juego de dados|")
print ("-" * 120)
Nombre=input("Ingrese su nombre: ")
print (input("Presione 'enter' para tirar el dado""\n"))
print ("Rodando...")
time.sleep (2)
print ("Rodando...")
time.sleep (2)
print ("Rodando...")
time.sleep (2)
print ("Se está parando y...")
time.sleep (2)
print ("Empezó a rodar de vuelta")
time.sleep (2)
print ("Rodando...")
time.sleep (2)
print ("Rodando...")
time.sleep (2)
t1= random.randint(1, 6)
print ("Sacaste un", t1)
time.sleep (3)
if (t1 % 2) != 0 :
    punt = t1 * 3
    print ("Dado al valor impar de tu número, lo multiplicaremos por 3")
    time.sleep(2)
    print ("No sacaste un 6, no podras tirar por segunda vez :(")
    time.sleep (3)
elif (t1 % 2) == 0 :
    punt = t1 * 2
    print ("Dado al valor par de tu número, lo multiplicaremos por 2")
    time.sleep (3)
    if t1 == 6:
        print ("Sacaste 6, así que tiraras por segunda vez ;)")
        time.sleep (1)
        print ("Presiona 'enter' para tirar por segunda vez")
        print (input())
        t2 = random.randrange(1, 6)
        print ("Sacaste un", t2)
        time.sleep (1)
        if t2 < 6:
            print ("Dado a que tu valor es menor a 6, lo restaremos de tu tirada inicial.")
            time.sleep (2)
            punt = punt - t2
        else:
            print ("¡¡Excelente!! Lo sumaremos a tu primera tirada")
            time.sleep (3)
            punt = punt + t2
    else:
        print ("No sacaste un 6, no poras tirar por segunda vez :(")
        time.sleep(3)
print (input("Terminamos, presiona 'enter' para ver tu resultado."))
feli = "Muy bien,", "Perfecto,", "Excelente", "Increible,", "Awesome,", "Nice,", "He quedado estupefacto"
desp = "Chau", "Nos vemos", "Nos vimos en Cuba", "Hasta la próxima", "Me voy, wiiiii"
print (random.choice(feli), Nombre + ",", "tu puntaje es", punt)
time.sleep(2)
print("...")
time.sleep(1)
print ("Bueno")
time.sleep(1)
print("...")
time.sleep(1)
print (random.choice(desp))
print (input())
