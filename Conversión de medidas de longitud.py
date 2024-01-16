print ("Este programa servira para convertir una unidad a pies, pulgadas, yardas, centímetros y metros.")
print ("_" * 90)
print ("Programa realizado por Daniel Reinoso")
print ("-" * 90)
unid = str(input("Ingrese que tipo de unidad quiere convertir: "))
while (unid != "pie") or (unid != "pies") or (unid != "pulgada") or (unid != "pulgadas") or (unid != "yarda") or (unid != "yardas") or (unid != "centimetro") or (unid != "centímetro") or (unid != "centimetros") or (unid != "centímetros") or (unid != "metro") or (unid != "metros"):
    if (unid == "pie") or (unid == "pies") or (unid == "pulgada") or (unid == "pulgadas") or (unid == "yarda") or (unid == "yardas") or (unid == "centimetro") or (unid == "centímetro") or (unid == "centimetros") or (unid == "centímetros") or (unid == "metro") or (unid == "metros"):
        break
    else:
         print ("\n""Error, nombre de unidad incorrecto o no soportado por este programa.""\n")
    unid = str(input("Por favor, ingresar la unidad a convertir nuevamente: "))
a = float(input("\n""Ingrese el valor a convertir: "))

unid2 = str(input("\n""Ingrese el tipo de unidad que desea recibir: "))
while (unid2 != "pie") or (unid2 != "pies") or (unid2 != "pulgada") or (unid2 != "pulgadas") or (unid2 != "yarda") or (unid2 != "yardas") or (unid2 != "centimetro") or (unid2 != "centímetro") or (unid2 != "centimetros") or (unid2 != "centímetros") or (unid2 != "metro") or (unid2 != "metros"):
    if (unid2 == "pie") or (unid2 == "pies") or (unid2 == "pulgada") or (unid2 == "pulgadas") or (unid2 == "yarda") or (unid2 == "yardas") or (unid2 == "centimetro") or (unid2 == "centímetro") or (unid2 == "centimetros") or (unid2 == "centímetros") or (unid2 == "metro") or (unid2 == "metros"):
        break
    else:
         print ("\n""Error, nombre de unidad incorrecto o no soportado por este programa.""\n")
    unid = str(input("Por favor, ingresar la unidad a convertir nuevamente: "))
if ((unid == "centimetro") or (unid == "centímetro") or (unid == "centimetros") or (unid == "centímetros")) and ((unid2 == "centimetro") or (unid2 == "centímetro") or (unid2 == "centimetros") or (unid2 == "centímetros")):
    r = a * 1
elif ((unid == "centimetro") or (unid == "centímetro") or (unid == "centimetros") or (unid == "centímetros")) and ((unid2 == "metro") or (unid2 == "metros")):
    r = a * 0.01
elif ((unid == "centimetro") or (unid == "centímetro") or (unid == "centimetros") or (unid == "centímetros")) and ((unid2 == "yarda") or (unid2 == "yardas")):
    r = a * 0.0109361
elif ((unid == "centimetro") or (unid == "centímetro") or (unid == "centimetros") or (unid == "centímetros")) and ((unid2 == "pie") or (unid2 == "pies")):
    r = a * 0.0328084
elif ((unid == "centimetro") or (unid == "centímetro") or (unid == "centimetros") or (unid == "centímetros")) and ((unid2 == "pulgada") or (unid2 == "pulgadas")):
    r = a * 0.393701
elif ((unid == "metros") or (unid == "metro")) and ((unid2 == "metro") or (unid2 == "metros")):
    r = a * 1
elif ((unid == "metros") or (unid == "metro")) and ((unid2 == "centimetro") or (unid2 == "centímetro") or (unid2 == "centimetros") or (unid2 == "centímetros")):
    r = a * 100
elif ((unid == "metros") or (unid == "metro")) and ((unid2 == "yarda") or (unid2 == "yardas")):
    r = a * 1.09361
elif ((unid == "metros") or (unid == "metro")) and ((unid2 == "pie") or (unid2 == "pies")):
    r = a * 3.28084
elif ((unid == "metros") or (unid == "metro")) and ((unid2 == "pulgada") or (unid2 == "pulgadas")):
    r = a * 39.3701
elif ((unid == "yardas") or (unid == "yarda")) and ((unid2 == "yarda") or (unid2 == "yardas")):
    r = a * 1
elif ((unid == "yardas") or (unid == "yarda")) and ((unid2 == "centimetro") or (unid2 == "centímetro") or (unid2 == "centimetros") or (unid2 == "centímetros")):
    r = a * 91.44
elif ((unid == "yardas") or (unid == "yarda")) and ((unid2 == "metro") or (unid2 == "metros")):
    r = a * 0.9144
elif ((unid == "yardas") or (unid == "yarda")) and ((unid2 == "pie") or (unid2 == "pies")):
    r = a * 3
elif ((unid == "yardas") or (unid == "yarda")) and ((unid2 == "pulgada") or (unid2 == "pulgadas")):
    r = a * 36
elif ((unid == "pies") or (unid == "pie")) and ((unid2 == "pie") or (unid2 == "pies")):
    r = a * 1
elif ((unid == "pies") or (unid == "pie")) and ((unid2 == "centimetro") or (unid2 == "centímetro") or (unid2 == "centimetros") or (unid2 == "centímetros")):
    r = a * 30.48
elif ((unid == "pies") or (unid == "pie")) and ((unid2 == "metro") or (unid2 == "metros")):
    r = a * 0.3048
elif ((unid == "pies") or (unid == "pie")) and ((unid2 == "yarda") or (unid2 == "yardas")):
    r = a * 0.333333
elif ((unid == "pies") or (unid == "pie")) and ((unid2 == "pulgada") or (unid2 == "pulgadas")):
    r = a * 12
elif ((unid == "pulgadas") or (unid == "pulgada")) and ((unid2 == "pulgada") or (unid2 == "pulgadas")):
    r = a * 1
elif ((unid == "pulgadas") or (unid == "pulgada")) and ((unid2 == "centimetro") or (unid2 == "centímetro") or (unid2 == "centimetros") or (unid2 == "centímetros")):
    r = a * 2.54
elif ((unid == "pulgadas") or (unid == "pulgada")) and ((unid2 == "metro") or (unid2 == "metros")):
    r = a * 0.0254
elif ((unid == "pulgadas") or (unid == "pulgada")) and ((unid2 == "yarda") or (unid2 == "yardas")):
    r = a * 0.0277778
elif ((unid == "pulgadas") or (unid == "pulgada")) and ((unid2 == "pie") or (unid2 == "pies")):
    r = a * 0.0833333

dec = int(input("\n""Ingrese la cantidad de decimales que desea recibir (en caso de no querer un limite, ingrese 100): "))

if (unid2 == "centimetro") or (unid2 == "centímetro") or (unid2 == "centimetros") or (unid2 == "centímetros"):
    unid3 = "cm"
elif (unid2 == "metro") or (unid2 == "metros"):
    unid3 = "m"
elif (unid2 == "yardas") or (unid2 == "yarda"):
    unid3 = "yd"
elif (unid2 == "pies") or (unid2 == "pie"):
    unid3 = "ft"
elif (unid2 == "pulgada") or (unid2 == "pulgadas"):
    unid3 = '"'
rF = round(r, dec)
rF = str(rF)
print ("\n""Su resultado es: ", rF + unid3)

des = str(input("\n""¿Desea repetir el programa?""\n"))
if (des == "SI") or (des == "Si") or (des == "si"):
    print ("Lo siento, aún no sé como hacerlo :(")
    print ("Lo vas a tener que ejecutar de vuelta ;)")
    print (input())
else: print (input())
