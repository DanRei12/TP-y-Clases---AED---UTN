'''Programa para calcular suma de dos angulos con grados, minutos y segundos.'''
print ("-" * 90)
print ("Programa para calcular la suma de dos angulos con grados, minutos y segundos, separando una en a y otra en b.")
print ("-" * 90)
Ag, Am, As = int(input("Ingresar angulo A: ""\n""\t""Grado: ")), int(input("\t""Minutos: ")), int(input("\t""Segundos: "))
Bg, Bm, Bs = int(input("\n""Ingresar angulo B: ""\n""\t""Grado: ")), int(input("\t""Minutos: ")), int(input("\t""Segundos: "))
Ts = As + Bs
Tm = Am + Bm
Tg = Ag + Bg
if Ts > 60:
    Ts = Ts - 60
    Tm = Tm + 1
if Tm > 60:
    Tm = Tm - 60
    Tg = Tg + 1
print ("\n""La cantidad de grados son:", Tg, "\n""La cantidad de minutos son:", Tm, "\n""La cantidad de segundos son:", Ts)
Tg = str(Tg)
Tm = str(Tm)
Ts = str(Ts)
print ("\n", "-" * 90, "\n""\t""El angulo es:", Tg + "°", Tm + "'", Ts + '"'"\n", "-" * 90)
print (input())
