#hola como están yo y pablo somos unos buenos tipos makata lataka tamara tatata.
texto = input("Ingrese su texto:")
texto = texto.lower()
palabras = 0
cant_de_p = 0
letra_ant = None
cant_de_ta = 0
cant_de_punt = 0
tiene_ta = False

if texto[0] == "p":
    cant_de_p = 1

for letra in texto:
    if letra == " " or letra == ".":
        palabras += 1
        if tiene_ta == True:
            cant_de_ta += 1
            tiene_ta = False

    if letra_ant == " " and letra == "p":
        cant_de_p +=1

    if letra_ant == "t" and letra == "a":
        tiene_ta = True

    if letra == ".":
        cant_de_punt += 1
    letra_ant = letra



print("Las cantidades de palabras introducidas fueron", palabras)
print("La cantidad de palabras que comienzan con 'p' son", cant_de_p)
print("La cantidad de palbras con 'ta' son", cant_de_ta)
print("Y por ultimo tenemos", cant_de_punt, "puntos.")
print(texto)

