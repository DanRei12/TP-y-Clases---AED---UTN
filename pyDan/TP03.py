__Author__ = 'G184'

    # Enunciado...
'''
Una tienda de libros electrónicos nos solicita ayuda para desarrollar un sistema de gestión de sus productos. De cada libro se conoce:

- Código de identificación o ISBN (cadena de caracteres).
- Título.
- Género (0: Autoayuda, 1:Arte, 2: Ficción, 3: Computación, 4: Economía, 5: Escolar, 6: Sociedad, 7: - - -   - - Gastronomía, 8: Infantil , 9: Otros).
- Idioma (1: español, 2: inglés, 3: francés, 4:italiano, 5:otros).
- Precio.

Se solicita un programa controlado por menú de opciones que permita lo siguiente:

1.) Generación y Carga: Generar un arreglo unidimensional con los n libros que ofrece la librería (n es un valor que se ingresa por teclado). Para el presente práctico se solicita que el usuario pueda optar por una carga manual (validando los datos de entrada) o por una carga automática de los datos de cada libro.
Se debe tener en cuenta que el International Standard Book Number (ISBN) es un identificador único para libros creado para uso comercial. Se creó en 1966 en el Reino Unido y alcanzó el rango de estándar internacional en 1970. Todas las ediciones y variaciones de un libro reciben un ISBN de 10 dígitos dividido en los cuatro grupos que se indican a continuación (sin longitud fija por cada grupo) separados por guiones ("-"):

- Código de país o lengua de origen.
- Código del editor (asignado por la agencia nacional del ISBN).
- Número del artículo (elegido por el editor).
- Dígito de control.

2.) Mostrar: Mostrar el vector generado en el punto anterior de tal manera que se muestre el género y el idioma del libro en lugar de los números que los representan y se listen ordenados por título en forma ascendente. Cada libro debe mostrarse a razón de una línea por registro.

3.) Conteo y género más popular: Determinar la cantidad de libros ofrecidos por género. Mostrar dichas cantidades y el género al que corresponde mostrando su nombre y no su código. Determinar el género con mayor cantidad de libros ofrecidos, indicando su nombre. Si hubiera más de un género con la misma cantidad, informar uno solo.

4.) Búsqueda del mayor: Determinar y mostrar el libro de mayor precio para un idioma i, siendo i un valor que se ingresa por teclado. Si existiera más de un libro con el mismo mayor precio mostrar sólo uno.

5.) Búsqueda por ISBN: Buscar si en el vector existe un libro con el ISBN x, siendo x un valor que se ingrese por teclado. Si existe mostrar sus datos y aumentar su precio un 10%. Si no existe, mostrar un mensaje por pantalla.

6.) Consulta de un género: Mostrar los datos de los libros del género con mayor cantidad de libros identificado en el punto 3. Dicho listado debe mostrarse ordenado por precio de mayor a menor.

7.) Consulta de precio por grupo: Esta funcionalidad permite a los alumnos secundarios cargar el listado de los ISBN correspondientes a los libros que el colegio les exige para el año escolar. El sistema debe buscar cuáles de estos libros se encuentran en su catálogo e indicar:

- Los libros que no se encontraron en el catálogo.
- Los libros que sí se encontraron en el catálogo con su precio.
El precio total que el estudiante debería pagar para comprar aquellos libros que la librería vende.

'''
    # Imports...
import random
import time

    # Variables para el título...

Adjetivos = ['Salado', 'Grande', 'Juvenil', 'Dulce', 'Pequeño', 'Comunista', 'Amargo', 'Diminuto', 'Infantil', 'Ácido', 'Seco','Capitalista', 'Rojo', 'Caro', 'Renacentista', 'Verde', 'Inteligente', 'Fotográfico', 'Rubio', 'Divertido', 'Fuerte', 'Fiel', 'Poco', 'Débil', 'Agradable', 'Demasiado', 'Flexible', 'Sucio', 'Suficiente', 'Tostado', 'Limpio', 'Rojo', 'Ronco', 'Amable', 'Varios', 'Nítido','Nuevo', 'Áspero', 'Valiente', 'Suave', 'Hermoso', 'Rugoso', 'Largo', 'Esponjoso', 'Cruel', 'Flojo', 'Perfecto', 'Cierto', 'Redondo', 'Culto', 'Cuadrado', 'Ancho', 'Universitario', 'Musical', 'Semejante', 'Institucional', 'Democrático', 'Artístico', 'Individual', 'Religioso', 'Nacional', 'Cultural', 'Regional', 'Cualquiera', 'Estructural', 'Mundial', 'Policial', 'Económico', 'Mensual',  'Político','Diario', 'Histórico', 'Solar', 'Civil', 'Militar', 'Familiar', 'Nuestro', 'Navideño', 'Industrial', 'Laboral', 'Naval', 'Vuestro', 'Mercantil', 'Agrícola', 'Vanguardista', 'Colorado', 'Dental', 'Energético', 'Quirúrgico', 'Petrolero', 'Segundo', 'Primero', 'Ambiguo', 'Marinero', 'm̸̿̏å̷̄l̴̂̊d̵͑͘ǐ̷́ṫ̶͛o̵̎̿']

Sustantivos = ['Vaca Lola', 'Sangre', 'Fantásma', 'Tendencia', 'Batalla', 'Polvo', 'Estrella', 'Crusada', 'Diamante', 'Irrompible', 'Viento', 'Oro', 'Piedra', 'Oceano', 'Acero', 'Pelota', 'Carrera', 'León', 'Tierra', 'Parte', 'Ambiente', 'Castillo', 'Espada', 'Abrelatas', 'Jonathan', 'Disposición', 'Parlante', 'Aire', 'Mesa', 'Respiración', 'PC', 'Libros', 'Escuela', 'Pelusa', 'Andrés', 'William', 'Esfera', 'Periférico', 'Animal', 'Esquina', 'Perro', 'Casco', 'Caesar', 'Felipe', 'Piscinas', 'Pasto', 'Cuaderno', 'Planta', 'Argentina', 'Silvio', 'Átomo', 'Paris', 'Joseph', 'Posavasos', 'Jorge', 'Belén', 'Capital', 'Interior', 'Galleta', 'Programa', 'Valerio', 'Candela', 'Puerta', 'Botón', 'Guitarra', 'Química', 'Brasil', 'Hoja', 'Rectángulo', 'Japón', 'Idea', 'Ropa', 'Cable', 'Milton', 'Silla', 'Calculadora', 'Juguete', 'Sonido', 'Carpeta', 'Julio', 'Algoritmo', 'Cartera', 'Esmeralda', 'Suciedad', 'Celular', 'JoJo', 'Loros', 'Sustancia', 'Cerradura', 'Cañaveral', 'Televidente', 'Césped', 'Manantial', 'Televisor', 'Inglaterra', 'Daniel', 'Tierra', 'Notebook', 'Mausoleo', 'Tigre', 'Círculo', 'Mesa', 'Nikolás', 'Ciudad', 'EEUU', 'Trabajador', 'Ciruela', 'Molécula', 'Trabajo', 'Claridad', 'Ratón', 'Triángulo', 'Clavel', 'Mueble', 'Tulipán', 'Competencia', 'Máscara', 'Alex', 'Utensilio', 'Computadora', 'Notas', 'Vaso', 'Cuerda', 'Nueva York', 'Ventana', 'Manicomio', 'Teléfono', 'Vidrio', 'Asiento', 'Pantalla', 'Violín', 'Batería', 'Vigilante', 'Visita', 'Manhattan', 'Gato']

Genero = ['Autoayuda', 'Arte', 'Ficción', 'Computación', 'Economía', 'Escolar', 'Sociedad', 'Gastronomía', 'Infantil', 'Otros']
Idioma = ['None', 'Español','Inglés', 'Francés', 'Italiano', 'Otros']

# FUNCIONES.

    # Función precios...
def gen_presio():
    precio = random.randint(200, 10000)
    return precio

    # Función para ordenar títulos...
def titlesort(tit, lang, gend):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(tit) - 1):
            if tit[i] > tit[i+1]:
                tit[i], tit[i+1] = tit[i+1], tit[i]
                gend[i], gend[i+1] = gend[i+1], gend[i]
                lang[i], lang[i+1] = lang[i+1], lang[i]
                sorted = False

    # Función para ordenar precios...
def pricesort(isbn, tit, gend, lang, pric, n):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(pric) - 1):
            if pric[i] < pric[i+1]:
                isbn[i], isbn[i+1] = isbn[i+1], isbn[i]
                tit[i], tit[i+1] = tit[i+1], tit[i]
                gend[i], gend[i+1] = gend[i+1], gend[i]
                lang[i], lang[i+1] = lang[i+1], lang[i]
                pric[i], pric[i+1] = pric[i+1], pric[i]
                sorted = False

    # Función para implementar en la función verif...
def is_numb(car):
    return car in '0123456789'

    # Función para verificar código...
def verif():
    isbn_m = ()
    n = []
    o = 0
    pol = 0
    while o == 0:
        isbn_m = str(input('Ingrese el ISBN del libro: '))
        isbn_m.lower()
        if len(isbn_m) == 13:
            o = 1
            for car in isbn_m:
                n.append(car)
                if car in 'abcdefghijklmnñopqrstuvwxyz':
                    pol = 1
                else:
                    continue
            if pol == 1:
                o = 0
                print('ISBN contiene letras y/o espacios.\n'
                'Por favor, introduzca el ISBN nuevamente.')
            elif pol == 0:
                if n[2] == '-' and n[7] == '-' and n[11] == '-':
                    n.remove(n[2])
                    n.remove(n[6])
                    n.remove(n[9])
                    if is_numb(car):
                        for i in range(0, len(n)):
                            n[i] = int(n[i])
                        if (10*n[0] + 9*n[1] + 8*n[2] + 7*n[3] + 6*n[4] + 5*n[5] + 4*n[6] + 3*n[7] + 2*n[8] + n[9]) % 11 == 0:
                            return('Verificado.', isbn_m)
                        else:
                            o = 0
                            print('No contiene caracteres soportados.\n'
                            'Por favor, introduzca el ISBN nuevamente.')
                else:
                    o = 0
                    print('No contiene los separadores o no se separó correctamente.\n'
                    'Por favor, introduzca el ISBN nuevamente.')
        else:
            print('El ISBN no contiene caracteres suficientes o contiene caracteres de más.\n'
            'Por favor, introduzca el ISBN nuevamente.')

    # Función para generar ISBN automáticamente...
def ISBN_gen():
    a = 0
    n = 10
    m = 0
    digitos = list()
    while a == 0:
        for i in range(n):
            digitos.append(random.randrange(9))
            m += digitos[i] * (10-i)
        if m % 11 == 0:
            a = 1
            for i in range(n):
                digitos[i] = str(digitos[i])
            ISBN = digitos[0] + digitos[1] + "-" + digitos[2] + digitos[3] + digitos[4] + digitos[5] + "-" +    digitos[6] + digitos[7] + digitos[8] + "-" + digitos[9]
            return ISBN
        else:
            a = 0

# MENÚ DE OPCIÓNES.
    # Función principal, donde se ejecutan las demás funciones...
def main():
    o = 0
    class Libros():
        pass
    while o != 8:
        tit = []
        gend = []
        lang = []
        pric = []
        isbn = []
        print('𝑻𝒊𝒆𝒏𝒅𝒂 𝒅𝒆 𝑳𝒊𝒃𝒓𝒐𝒔 𝑬𝒍𝒆𝒄𝒕𝒓𝒐𝒏𝒊𝒄𝒐𝒔.\n'
        '𝘚𝘦𝘭𝘦𝘤𝘤𝘪𝘰𝘯𝘦 𝘴𝘶 𝘰𝘱𝘤𝘪𝘰́𝘯:\n'
        '1- Carga de libros (manualmente o automáticamente).\n'
        '2- Mostrar libros.\n'
        '3- Ordenar por género.\n'
        '4- Ordernar por precio (Mayor a menor).\n'
        '5- Buscar libro por ISBN.\n'
        '6- Buscar libros por género.\n'
        '7- Verificar si se encuentran los libros a través del ISBN.\n'
        '8 - Salir.')

        o = int(input('Ingrese su elección: '))

        # Opción 1, se genera ISBN...
        if o == 1:
            n = int(input('Ingrese la cantidad de libros a cargar: '))
            l = n * [None]
            op = str(input('Desea cargarlos manualmente (S/N): '))

            for i in range(n):
                l[i] = Libros()

                if op == 'n' or op == 'N':

                    l[i].Title = random.choice(Sustantivos) + " " + random.choice(Adjetivos) + "."
                    l[i].Code = ISBN_gen()
                    l[i].Gender = Genero[random.randrange(9)]
                    l[i].Language = Idioma[random.randrange(1, 5)]
                    l[i].Price = gen_presio()

                elif op == 's' or op == 'S':

                    l[i].Title = str(input('I̲n̲g̲r̲e̲s̲e̲ e̲l̲ t̲i̲t̲u̲l̲o̲ d̲e̲l̲ l̲i̲b̲r̲o̲:̲'))
                    l[i].Code = verif()
                    l[i].Gender = int(input('0 - Autoayuda.\n'
                                        '1 - Arte.\n'
                                        '2 - Ficción.\n'
                                        '3 - Computación.\n'
                                        '4 - Economía.\n'
                                        '5 - Escolar.\n'
                                        '6 - Sociedad\n'
                                        '7 - Gastronomía.\n'
                                        '8 - Infantil.\n'
                                        '9 - Otros.\n'
                                        'Ingrese el género del libro: '))
                    l[i].Language = int(input('1 - Español.\n'
                                        '2 - Inglés. \n'
                                        '3 - Francés. \n'
                                        '4 - Italiano. \n'
                                        '5 - Otros.\n'
                                        'Ingrese el lenguaje del libro: '))
                    while (l[i].Gender > 9) or (l[i].Gender < 0):
                        l[i].Gender = int(input('0 - Autoayuda.\n'
                                            '1 - Arte.\n'
                                            '2 - Ficción.\n'
                                            '3 - Computación.\n'
                                            '4 - Economía.\n'
                                            '5 - Escolar.\n'
                                            '6 - Sociedad\n'
                                            '7 - Gastronomía.\n'
                                            '8 - Infantil.\n'
                                            '9 - Otros.\n'
                                            'Ingrese el género del libro nuevamente: '))
                    while (l[i].Language > 5) or (l[i].Language < 0):
                        l[i].Language = int(input('1 - Español.\n'
                                            '2 - Inglés. \n'
                                            '3 - Francés. \n'
                                            '4 - Italiano. \n'
                                            '5 - Otros.\n'
                                            'Ingrese el lenguaje del libro nuevamente: '))
                    l[i].Price = int(input('Ingrese el valor del libro: '))
                    print(input("\n𝙋𝙧𝙚𝙨𝙞𝙤𝙣𝙚 𝙀𝙉𝙏𝙀𝙍 𝙥𝙖𝙧𝙖 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙖𝙧..."))

        # Opción 2, se muestran los libros...
        if o == 2:
            for i in range(n):
                tit.append(l[i].Title)
                gend.append(l[i].Gender)
                lang.append(l[i].Language)
            sort = titlesort(tit, lang, gend)
            for i in range(len(tit)):
                print('Título:', tit[i], 'Género:', gend[i], 'Idioma:', lang[i], '\n')

            print(input("\n𝙋𝙧𝙚𝙨𝙞𝙤𝙣𝙚 𝙀𝙉𝙏𝙀𝙍 𝙥𝙖𝙧𝙖 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙖𝙧..."))

        # Opción 3, se ordena por género...
        if o == 3:
            cont = [0] * 10
            may = 0
            mayor = 0
            for i in range(10):
                for j in range(n):
                    if l[j].Gender == Genero[i]:
                        cont[i] += 1
                print('El género', Genero[i], 'tiene', cont[i], 'libros.')

            for i in range(10):
                if cont[i] > mayor:
                    may = i
                    mayor = cont[i]
            print('El género con mayor cantidad de libros es el de', Genero[may], 'con una cantidad de', cont[may], 'libros.')
            print(input("\n𝙋𝙧𝙚𝙨𝙞𝙤𝙣𝙚 𝙀𝙉𝙏𝙀𝙍 𝙥𝙖𝙧𝙖 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙖𝙧..."))

        # Opción 4, donde se buscar el libro con mayor precio con respecto a su idioma...
        if o == 4:
            may = 0
            mayor = 0
            LangSelect= int(input('1 - Español.\n'
                                    '2 - Inglés.\n'
                                    '3 - Francés.\n'
                                    '4 - Italiano.\n'
                                    '5 - Otros.\n'
                                    'Ingrese los libros de que género desea mostrar: '))
            for i in range(n):
                pric.append(l[i].Price)
                lang.append(l[i].Language)
                tit.append(l[i].Title)

            for i in range(5):
                if LangSelect == i:
                    LangSelect = Idioma[i]
                    print('Los libros del idioma', LangSelect, 'son los siguientes:')
                    for j in range(n):
                        if l[j].Language == LangSelect:
                            print('Titulo: ', l[j].Title, 'Idioma: ', l[j].Language, 'Precio:', l[j].Price)
                            if l[j].Price > mayor:
                                mayor = l[j].Price
                                may = j
            print('\nEl libro más caro del idioma', LangSelect, 'es el', l[may].Title, 'con un precio de', mayor)
            print(input("\n𝙋𝙧𝙚𝙨𝙞𝙤𝙣𝙚 𝙀𝙉𝙏𝙀𝙍 𝙥𝙖𝙧𝙖 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙖𝙧..."))

        # Opción 5, donde buscamos un libro por su ISBN y le aumentamos un 10% su precio...
        if o == 5:
            isbnb = input('Ingresar el ISBN (con el modelo 00-0000-000-0): ')
            band_isbn = True
            for i in range(n):
                isbn.append(l[i].Code)
                tit.append(l[i].Title)
                gend.append(l[i].Gender)
                lang.append(l[i].Language)
                pric.append(l[i].Price)

            for i in range(n):
                if isbnb == isbn[i]:

                    print('Titulo:', tit[i],'\n' , 'ISBN:', isbn[i], '\n' , 'Género:', gend[i], '\n' ,'Idioma:', lang[i], 'Precio original:', pric[i])
                    pric[i] = (pric[i]) + (10 * pric[i] // 100)
                    print('\nSu precio aumento un 10% por lo que ahora mismo vale', pric[i])
                    band_isbn = False

            if band_isbn:
                print('El libro que esta buscando no se encuentra en la base de datos.')
            print(input("\n𝙋𝙧𝙚𝙨𝙞𝙤𝙣𝙚 𝙀𝙉𝙏𝙀𝙍 𝙥𝙖𝙧𝙖 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙖𝙧..."))

        # Opción 6, consultar por género...
        if o == 6:
            GenSelect= int(input('0 - Autoayuda.\n'
                                    '1 - Arte.\n'
                                    '2 - Ficción.\n'
                                    '3 - Computación.\n'
                                    '4 - Economía.\n'
                                    '5 - Escolar.\n'
                                    '6 - Sociedad\n'
                                    '7 - Gastronomía.\n'
                                    '8 - Infantil.\n'
                                    '9 - Otros.\n'
                                    'Ingrese los libros de que género desea mostrar: '))
            for i in range(n):
                isbn.append(l[i].Code)
                tit.append(l[i].Title)
                gend.append(l[i].Gender)
                lang.append(l[i].Language)
                pric.append(l[i].Price)
            sort = pricesort(isbn, tit, lang, gend, pric, n)
            for i in range(10):
                if GenSelect == i:
                    GenSelect = Genero[i]
                    print('Los libros del género', GenSelect, 'son los siguientes:')
                    for j in range(len(pric)):
                        if gend[j] == GenSelect:
                            print('Titulo: ', tit[j], 'Género: ', gend[j], 'ISBN:', isbn[j], 'Idioma: ', lang[j], 'Precio:', pric[j])

            print(input("\n𝙋𝙧𝙚𝙨𝙞𝙤𝙣𝙚 𝙀𝙉𝙏𝙀𝙍 𝙥𝙖𝙧𝙖 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙖𝙧..."))

        # Opción 7, se ingresan una cierta cantidad de ISBN y se busca en los ISBN cargados anteriormente...
        if o == 7:
            for i in range(n):
                isbn.append(l[i].Code)
                tit.append(l[i].Title)
                pric.append(l[i].Price)

            isbnal = []
            x = int(input('Ingresar la cantidad de ISBN que buscará: '))
            total_price = 0
            band_isbnal = True
            for i in range(x):
                isbna = input('Ingresar el ISBN (con el modelo 00-0000-000-0): ')
                isbnal.append(isbna)
            for i in range(x):
                for j in (range(n)):
                    if isbnal[i] == isbn[j]:
                        band_isbnal = False
                        print('Se encontro', tit[j], 'en el catálogo y su precio es:', pric[j])
                        total_price += pric[i]
                if band_isbnal:
                    print('No se encontró el libro en el catálogo.')

            print('El total a pagar por el estudiante es de', total_price)
            print(input("\n𝙋𝙧𝙚𝙨𝙞𝙤𝙣𝙚 𝙀𝙉𝙏𝙀𝙍 𝙥𝙖𝙧𝙖 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙖𝙧..."))

    # Main script...
if __name__ == "__main__":
    main()
# Messi
