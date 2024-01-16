'''Programa para calcular suma de dos angulos con grados, minutos y segundos.'''
print ("-" * 90)
print ("Programa para calcular la suma de dos angulos con grados, minutos y segundos, separando una en a y otra en b.")
print ("-" * 90)
AnguloA = int(input("Ingresar valor grado de A: ""\n")), int(input("Ingresar valor minuto de A: ""\n")), int(input("Ingresar valor segundo de A: ""\n"))
AnguloB = int(input("Ingresar valor grado de B: ""\n")), int(input("Ingresar valor minuto de B: ""\n")), int(input("Ingresar valor segundo de B: ""\n"))
Ast = (AnguloA[0] * (60 ** 2)) + (AnguloA[1] * 60) + AnguloA[2]
Bst = (AnguloB[0] * (60 ** 2)) + (AnguloB[1] * 60) + AnguloB[2]
segTotal = Ast + Bst
res = segTotal % (60 ** 2)
T = segTotal // (60 ** 2), res // 60, res % 60
print ("La cantidad de grados son:", T[0], "\n""La cantidad de minutos son:", T[1], "\n""La cantidad de segundos son:", T[2])
T = str(T[0]), str(T[1]), str(T[2])
print ("\n""El angulo es:", T[0] + "°", T[1] + "'", T[2] + '"')
print (input())
