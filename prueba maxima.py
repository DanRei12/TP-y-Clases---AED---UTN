'''ESTE PROGRAMA AUN NO ESTA TERMINADO D:'''
'''ESTE PROGRAMA AUN NO ESTA TERMINADO D:'''
'''ESTE PROGRAMA AUN NO ESTA TERMINADO D:'''
'''ESTE PROGRAMA AUN NO ESTA TERMINADO D:'''
'''ESTE PROGRAMA AUN NO ESTA TERMINADO D:'''

print ("Este programa servira para convertir una unidad a pies, pulgadas, yardas, centímetros y metros.")
print ("_" * 90)
print ("Programa realizado por Daniel Reinoso")
print ("-" * 90)
def main():
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
    elif ((unid == "centimetro") or (unid == "centímetro") or (unid == "centimetros") or (unid == "centímetros")) and ((unid2 == "metro") or (unid2 == "metros")):\
        r = a * 0.01
    elif ((unid == "centimetro") or (unid == "centímetro") or (unid == "centimetros") or (unid == "centímetros")) and ((unid2 == "yarda") or (unid2 == "yardas")):
        r = a * 0.0109361
    elif ((unid == "centimetro") or (unid == "centímetro") or (unid == "centimetros") or (unid == "centímetros")) and ((unid2 == "pie") or (unid2 == "pies")):
        r = a * 0.0328084
    elif ((unid == "centimetro") or (unid == "centímetro") or (unid == "centimetros") or (unid == "centímetros")) and ((unid2 == "pulgada") or (unid2 == "pulgadas")):
        r = a * 0.393701
    dec = int(input("\n""Ingrese la cantidad de decimales que desea recibir (en caso de no querer un limite, responda 'todas'): "))
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
    print ("\n""Su resultado es: ", rF, unid3)
    des = str(input("\n""¿Desea repetir el programa?""\n"))
    if (des == "si") or (des == "Si") or (des == "SI"):
        print("ok")
        return main()
    else: print (input())
main()
