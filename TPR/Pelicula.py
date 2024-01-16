class Pelicula:
    def __init__(self, identificacion, titulo, tipo, calificacion, costo):
        self.identificacion = identificacion
        self.titulo = titulo
        self.tipo = tipo
        self.calificacion = calificacion
        self.costo = costo

def to_string(peli):
    r = ""
    r += "{:<20}".format("Numero de Identificacion: " + str(peli.identificacion))
    r += "{:<30}".format(" - Nombre: " + peli.titulo)
    r += "{:<20}".format(" - Tipo de pelicula: " + str(peli.tipo))
    r += "{:<20}".format(" - Calificación: " + str(peli.calificacion))
    r += "{:<20}".format(" - Costo de Producción: " + str(peli.costo))
    return r
