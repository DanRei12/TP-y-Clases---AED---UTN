
        '''if o == 4:
            may = 0
            mayor = 0
            for i in range(n):
                pric.append(l[i].Price)
                lang.append(l[i].Language)
                tit.append(l[i].Title)
            idiom = pricesort2(tit, lang, pric)
            gen1 = int(input('1 - Español.\n'
                            '2 - Inglés. \n'
                            '3 - Francés. \n'
                            '4 - Italiano. \n'
                            '5 - Otros.\n'
                            'Ingrese el lenguaje del libro que desea buscar: '))
            lang[i] = gen1 +1
            for i in range(len(lang)):
                if pric[i] > mayor:
                    may = i
                    mayor = pric[i]
            for i in range(1):

                    print('El libro más caro del lenguaje', lang[i], 'es:', tit[i], 'con un precio de:', mayor)

            input('𝙋𝙧𝙚𝙨𝙞𝙤𝙣𝙚 𝙀𝙉𝙏𝙀𝙍 𝙥𝙖𝙧𝙖 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙖𝙧...')'''

def pricesort2(isbn, tit, gend, lang, pric, n):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(pric) - 1):
            if pric[i] > pric[i]:
                isbn[i], isbn[i+1] = isbn[i+1], isbn[i]
                tit[i], tit[i+1] = tit[i+1], tit[i]
                gend[i], gend[i+1] = gend[i+1], gend[i]
                lang[i], lang[i+1] = lang[i+1], lang[i]
                pric[i], pric[i+1] = pric[i+1], pric[i]
                sorted = False
