'''Enunciado:
Se pide desarrollar un programa en Python que permita cargar por teclado un texto completo en una
variable de tipo cadena de caracteres. El texto finaliza con ‘.’ y se supone que el usuario cargará el punto para
indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco.
El programa debe incluir al menos una función simple con parámetros y retorno de resultado, debe procesar el texto
caracter a caracter (a razón de uno por vuelta de ciclo), y debe hacer lo siguiente sin usar un menú de opciones:

- Turno 03 – Enunciado 01 [T3E1] -

1- Determinar la cantidad de palabras que contienen el primer caracter de todo el texto (minúscula o mayúscula si es
letra) en la segunda posición de dicha palabra. Por ejemplo, en el texto "Al manso caballo le gusta pastar." hay 3
palabras que cumplen el criterio ("manso", "caballo" y "pastar").

2- Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que contienen una vocal
(minúscula o mayúscula) en la tercera posición y una consolante (minúscula o mayúscula) en la cuarta. Por ejemplo, en
el texto "La mentalidad sobre los peajes es enervante." hay 7 palabras en total y 2 palabras que cumplen con el criterio
 ("peajes" y "enervante"). Por lo tanto el porcentaje seria 28.57%.

3- Determinar la cantidad de palabras que contienen mas de 5 caracteres y que NO COMIENCEN con el ultimo caracter de la
primera palabra del texto. Por ejemplo, en el texto "Comenzamos a silenciar los micrófonos en el parcial." hay 2
palabras que cumplen el criterio ("micrófonos" y "parcial"). Por "caracteres", se entiende "cualquier tipo de símbolo,
sea este un dígito, una letra, o cualquier otro que pueda aparecer".

4- Determinar la cantidad de palabras que contienen la secuencia "t" seguida de una vocal cualquiera (con cualquiera de
sus letras en minúscula o en mayúscula) pero de forma tal que la secuencia esté presente en las primeras cuatro letras
de la palabra. Por ejemplo, en el texto "La atenta mirada de la tia explota de amor." hay 2 palabras que cumplen con el
criterio ("atenta" y "tia"). La palabra "explota" tiene una secuencia t+vocal, pero no entre las primeras cuatro letras,
por lo que no debe ser contada.'''

#Programa principal.
def principal():
    #Función primera letra del texto.
    def Primera_Letra_Texto(texto):
        band_1let = False
        primera_letra = None
        for letra in texto:
            if band_1let == False:
                primera_letra = letra
                band_1let = True
        return primera_letra

    #Función si es vocal.
    def es_vocal(letra):
        return letra in 'aeiouAEIOUáéíóúÁÉÍÓÚüÜ'

    #Función si esconsonante.
    def es_consonante(letra):
        resultado = False
        vocales = 'bcdfghjklmnpqrstvwxyz'
        if letra in vocales:
            resultado = True
        return resultado

    #Función cantidad de palabras.
    def CantPal(text):
        cant_palabras = 0

        for letra in text:
            if letra == "." or letra == " ":
                cant_palabras += 1
            if cant_palabras == 0 and letra != ",":
                ult_let_primer_palabra = letra
        return cant_palabras, ult_let_primer_palabra

    #Ingreso del texto.
    texto = input("Ingresar el texto a analizar: ")

    #Convertir a minusculas.
    texto = texto.lower()

    #Variables.
    cont_car = 0
    cant_pal_1car = 0

    band_let3pos = False
    band_cons4pos = False
    cant_pal_punto2 = 0
    porc_punto2 = 0

    cant_pal_punto3 = 0
    band_punto3 = False
    band_primpalabra = False

    cant_pal_punto4 = 0
    band_t = False
    secuencia_tvoc = False

    #Variables asignadas por funciones.
    prim_letra = Primera_Letra_Texto(texto)
    cant_pal, ultlet_primpal = CantPal(texto)

    #Ciclo general.
    for car in texto:
        #Contador de caracteres principal.
        if car != " " and car != "." and car != ",":
            cont_car += 1
            #Condicional para contador del primer punto.
            if cont_car == 2 and car == prim_letra:
                cant_pal_1car += 1

        #Reinicio de banderas y variables.
        elif car == " ":
            cont_car = 0
            band_cons4pos = False
            band_let3pos = False
            band_punto3 = False
            band_t = False
            secuencia_tvoc = False

        #Realización del punto 2.
        if cont_car == 3 and es_vocal(car):
            band_let3pos = True
        if cont_car == 4 and es_consonante(car):
            band_cons4pos = True
        if band_let3pos and band_cons4pos:
            cant_pal_punto2 += 1
            band_let3pos = False
            band_cons4pos = False
            band_punto3 = False

        #Realizacion del punto 3.
        if car == " ":
                band_primpalabra = True
        if cont_car == 1:
            if car != ultlet_primpal and band_primpalabra:
                band_punto3 = True
            else:
                band_punto3 = False
        if cont_car > 5 and band_punto3:
            cant_pal_punto3 += 1
            band_punto3 = False

        #Realización del punto 4.
        if es_vocal(car) and band_t:
            secuencia_tvoc = True
            band_t = False
        if car == "t":
            band_t = True
        else:
            band_t = False
        if cont_car <= 4 and secuencia_tvoc:
            cant_pal_punto4 += 1
            secuencia_tvoc = False
            band_t = False

    #Calculo de porcentaje para punto 2.
    if cant_pal_punto2 != 0:
        porc_punto2 = cant_pal_punto2 * 100 / cant_pal

    #Mostrar resultados.
    print(f"Punto 1: {cant_pal_1car}")
    print(f"Punto 2: {porc_punto2}")
    print(f"Punto 3: {cant_pal_punto3}")
    print(f"Punto 4: {cant_pal_punto4}")

#Condicional para la ejecución del programa principal.
if __name__ == '__main__':
    principal()
