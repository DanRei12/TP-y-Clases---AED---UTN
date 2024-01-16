'''Programa para calcular el promedio entre 3 temperaturas'''
question = input('¿Quiere usar temperaturas con decimales o solo con numeros enteros? Responder con "enteros" o con "decimales"'"\n")
if (question == "enteros") or (question == "Enteros") or (question == "Entero") or (question == "entero"):
    v1 = int(input("Ingresar el valor 1: "))
    v2 = int(input("Ingresar el valor 2: "))
    v3 = int(input("Ingresar el valor 3: "))
    vF = (v1 + v2 + v3) // 3
else:
    v1, v2, v3 = float(input("Ingresar el valor 1: ")), float(input("Ingresar el valor 2: ")), float(input("Ingresar el valor 3: "))
    vN = (v1 + v2 + v3) / 3
    vF = round(vN, 1)

print ("El valor promedio es:", vF)
print (input())
