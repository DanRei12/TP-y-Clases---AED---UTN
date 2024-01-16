import random
autores =["Michellin", "Ricardinho", "Silvatore", "Lautinho", "Messi i", "Agüita", "PapuGómez", "Papachotón", "Reinaldo Lenis"]
titulos = ["La Mole", "Spiderman", "Daredevil", "Batman", "The Robin's", "Venom", "The Punisher", "Constantine", "Justice League", "Crisis on Infinite Earths"]
class Libros:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor

def to_string(lib):
    cadena = ''
    cadena = "ISBN: " + str(lib.isbn)
    cadena += " - Titulo: " + lib.titulo
    cadena += " - Autor: " + lib.autor
    return cadena

def carga_automatica(n):
    vec = []
    for i in range(n):
        isbn = random.randrange(1000, 9999)
        titulo = random.choice(titulos)
        autor = random.choice(autores)
        lib = Libros(isbn, titulo, autor)
        vec.append(lib)
    return vec
