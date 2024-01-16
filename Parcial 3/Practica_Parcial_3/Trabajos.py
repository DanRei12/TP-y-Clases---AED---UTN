import random
titulos = ["Abogacia", "Ingenieria", "Medicina", "Arquitectura", "Psicologia", "Profesorado"]
areas = ["Inteligencia Artificial", "Informatica", "Lenguajes de programación", "Ayudante", "Gestión", "Contaduria", "Derechos", "Area de compra", "Secretaría", "Limpieza"]

class Trabajos:
    def __init__(self, numero, titulo, area, cant_pag, cant_aut):
        self.numero = numero
        self.titulo = titulo
        self.area = area
        self.cant_pag = cant_pag
        self.cant_aut = cant_aut

def to_string(tra):
    cadena = ''
    cadena = "Número: " + str(tra.numero)
    cadena += " Titulo: " + tra.titulo
    cadena += " Area: " + areas[tra.area]
    cadena += " Cantidad de paginas: " + str(tra.cant_pag)
    cadena += " Cantidad de autores: " + str(tra.cant_aut)
    return cadena

def carga_automatica(n):
    vec = []
    for i in range(n):
        numero = random.randrange(1, 99)
        titulo = random.choice(titulos)
        area = random.randrange(10)
        cant_pag = random.randrange(101)
        cant_aut = random.randrange(11)
        tra = Trabajos(numero, titulo, area, cant_pag, cant_aut)
        vec.append(tra)
    return vec

def validar_con_rango(desde, hasta, message):
    num = int(input(message))
    while num <= desde or num >= hasta:
        print("Valor no válido. Ingresar otro valor entre", desde, "y", hasta)
        num = int(input(message))
    return num
