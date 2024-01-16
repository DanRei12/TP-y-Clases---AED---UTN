print ("Programa para calcular el precio de un boleto de colectivo. (Nota: Por km se calculara un adicionado de $0.30)")
cons = 0.30
prec = float(input("\n""Ingrese el precio éstandar de un boleto, sin tener en cuenta la distancia (sin el signo o palabra pesos): "))
dist = float(input("Ingrese la distancia a recorrer en km: "))
Precio_del_boleto = (cons * dist) + prec
Precio_del_boleto = str(Precio_del_boleto)
print ("\n""Su boleto vale", "$" + Precio_del_boleto)
print(input())
