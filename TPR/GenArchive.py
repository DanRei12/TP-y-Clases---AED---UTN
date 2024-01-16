import Funciones
import random

#Titulos para generación aleatoria.
titulos = ["Stairway to Heaven", "Don't Answer Me", "Ammonia Avenue", "Bones", "All Things That I've Done", "Pumped Up Kicks",
           "Jeremy", "Dead Man's Party", "Eye in the Sky", "Poker Face", "T.N.T.", "The Man Who Sold the World", "Space Oddity",
           "The Wanderer", "That's Life", "Fly Me to the Moon", "Just Breathe", "A Day in the Life", "Storm Front", "Piano Man",
           "Never Gonna Give You Up", "Renegade", "Haruka Kanata", "Kaikai Kitan", "Give a Little Bit", "With a Little Luck",
           "Yesterday", "Ballroom Blitz", "Come With Me Now", "Kids These Days",  "Forever Afternoon", "Mr. Blue Sky",
           "Tyson Vs Douglas", "Breakthru", "Bohemian Rhapsody", "Pegasus Fantasy", "Roundabout", "Song 2", "Pyramania",
           "Mr. Roboto", "Blue Collar Man", "Queenie Eye", "Barbie Girl", "Stone Cold Crazy", "Stayin' Alive",
           "Smooth Criminal", "Billie Jean", "Invisible Touch", "Magoo", "English Sunset", "Rasputin", "Games People Play",
           "Live and Let Die", "Soiree Fantastique", "Chillax", "Kura Kura", "Konami Kode", "Techno Syndrome", "Mull of Kintyre",
           "In the Lap of the Gods", "Celtic Sonant", "Ji Ji Ji", "Prophet's Song", "Peggy Sue", "Get Back",
           "Walk Like an Egyptian", "99 Luftballons", "Püree", "Libertango", "Shallow", "Waiting So Long",
           "A Dream Within a Dream", "The Cask of Amontillado", "Fermín", "The Forgotten Kingdom",
           "Baker Street", "Sultans of Swing", "21st Century Schizoid Man", "Wish You Were Here", "Comfortably Numb",
           "Another Brick in the Wall", "Wahre Helden", "Denk an Mich", "Euch Zum Geleit", "Helter Skelter",
           "Revolution 9", "Junk", "Purple Rain", "Blackbird"]

FD = "musica.csv"

#Función primaria para generación del archivo a utilizar.
def gen_archive():
    m = open(FD, mode="w+t", encoding="utf8")
    n = int(input("Ingrese la cantidad de temas a generar para el archivo: "))

    for i in range(n):
        titulo = random.choice(titulos)
        gen = random.randrange(6)
        lang = random.randrange(5)
        tema = Funciones.Tema(titulo, gen, lang)
        cad = to_linea(tema)
        m.write(cad)
        #m.write(tema.Titulo + ", " + str(tema.Genero) + ", " + str(tema.Idioma) + "\n")


    m.close()
    print("\nArchivo generado correctamente\n")
    print("\nLa cantidad de registros generados fueron", n, "\n")
    input()

#Función para poder ingresar una linea de registro al archivo.
def to_linea(tema):
    cad = '{},{},{}\n'
    return cad.format(tema.Titulo, tema.Genero, tema.Idioma)

print("Se realiza la generación del archivo...\n")
gen_archive()
