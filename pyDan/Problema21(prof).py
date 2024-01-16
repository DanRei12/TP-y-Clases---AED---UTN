texto = input("Ingrese su texto (en minusculas finalizado con punto final):")
palabras = 0
cant_de_letras = -1
cant_de_p = 0
cant_de_ta = 0
cant_de_punt = 0
tiene_ta = False
for letra in texto:
    cant_de_letras += 1
    if letra == " " or letra == ".":
        palabras += 1
        if tiene_ta == True:
            cant_de_ta += 1
            tiene_ta = False
    if letra == ".":
        cant_de_punt += 1
    if letra == "p" and (cant_de_letras == 0 or texto[cant_de_letras - 1] == " "):
        cant_de_p += 1
    if letra == "a" and (cant_de_letras > 0 and texto[cant_de_letras - 1] == "t"):
        tiene_ta = True




print("Las cantidades de palabras introducidas fueron", palabras)
print("La cantidad de palabras que comienzan con 'p' son", cant_de_p)
print("La cantidad de expresiones 'ta' son", cant_de_ta)
print("Y por ultimo tenemos", cant_de_punt, "puntos.")
