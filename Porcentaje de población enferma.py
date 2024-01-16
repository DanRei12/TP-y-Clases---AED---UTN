'''Programa para calcular el porcentaje de enfermos dentro de una poblacion determinada.'''
pobN = int(input("Ingrese la cantidad de enfermos a nivel nacional: "))
pobC = int(input("\n""Ingrese la cantidad de enfermos en la ciudad: "))
porc = (pobC * 100) / pobN
porc = str(round(porc, 2))
print ("El porcentaje de enfermos que representa la ciudad a nivel nacional son:", porc + "%")
