nombre = ["Palo", "Escoba", "Pala", "Palita", "Tabla", "Bisturi", "Cuchillo", "Tenedor", "Maquinaria", "Linterna",]

class Equipo:
    def __init__(self, num, nombre, precio, tip_apar, cod_pais):
        self.num = num
        self.nombre = nombre
        self.precio = precio
        self.tip_apar = tip_apar
        self.cod_pais = cod_pais

def to_string(equipo):
    r = ""
    r += "{:<20}".format("Numero de Identificacion: " + str(equipo.num))
    r += "{:<30}".format(" - Nombre: " + equipo.nombre)
    r += "{:<20}".format(" - Precio: " + str(equipo.precio))
    r += "{:<20}".format(" - Tipo de aparato: " + str(equipo.tip_apar))
    r += "{:<20}".format(" - Codigo pais de origen: " + str(equipo.cod_pais))
    return r
