'''Programa para el calculo del dinero a pagar dependiendo de la cantidad de km recorridos'''
exc1 = 300
exc2 = 1000

nom = str(input("Ingrese el nombre del cliente: "))

preg1 = str(input("¿Quiere cambiar los excedentes de kilometraje por defecto? (estos son 300 y 1000)" "\n"))
while (preg1 != "Si") or (preg1 != "Si quiero") or (preg1 != "si") or (preg1 != "si quiero") or (preg1 != "No") or (preg1 != "No quiero") or (preg1 != "no") or (preg1 != "no quiero"):
     if (preg1 == "No") or (preg1 == "No quiero") or (preg1 == "no") or (preg1 == "no quiero"):
        print ("Entones proseguiremos con el programa normalmente.")
        break
     if (preg1 == "Si") or (preg1 == "Si quiero") or (preg1 == "si") or (preg1 == "si quiero"):
        exc1 = int(input("Ingrese el número del primer excedente de kilometraje: "))
        exc2 = int(input("Ingrese el número del segundo excedente de kilometraje: "))
        break
     print ("¡Error! Respuesta no valida")
     preg1 = str(input("¿Quiere cambiar los excedentes de kilometraje por defecto? (estos son 300 y 1000)" "\n"))

km = int(input("Ingrese la cantidad de km que recorrio el cliente: "))


if km < exc1:
    importe = 500
elif km > exc1 and km < exc2:
    importe = 500 + ((km - exc1) * 3)
else:
    importe = 500 + ((km - exc1) * 1.5)
importe = str(importe)
print ("La cantidad a pagar del señor", nom + ",", "es de", "$" + importe)
print (input())
