'''Programa para calcular suma de dos angulos con grados, minutos y segundos.'''
print ("-" * 90)
print ("Programa para calcular la suma de dos angulos con grados, minutos y segundos, separando una en a y otra en b.")
print ("-" * 90)
Ag, Am, As = int(input("Ingresar valor grado de A: ""\n")), int(input("Ingresar valor minuto de A: ""\n")), int(input("Ingresar valor segundo de A: ""\n"))
Bg, Bm, Bs = int(input("Ingresar valor grado de B: ""\n")), int(input("Ingresar valor minuto de B: ""\n")), int(input("Ingresar valor segundo de B: ""\n"))
Ast = (Ag * (60 ** 2)) + (Am * 60) + As
Bst = (Bg * (60 ** 2)) + (Bm * 60) + Bs
segTotal = Ast + Bst
Tg = segTotal // (60 ** 2)
Tm = (segTotal % (60 ** 2)) // 60
Ts = (segTotal % (60 ** 2)) % 60
print ("La cantidad de grados son:", Tg, "\n""La cantidad de minutos son:", Tm, "\n""La cantidad de segundos son:", Ts)
Tg = str(Tg)
Tm = str(Tm)
Ts = str(Ts)
print ("\n""El angulo es:", Tg + "°", Tm + "'", Ts + '"')
print (input())
