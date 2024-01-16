__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random


def generar_archivo_csv():
    fd = 'series.csv'
    titulos = ('Friends', 'Lost', 'House of Cards', 'Mad Men', 'Vis a Vis',
               'La casa de papel', 'Breaking Bad', 'Dexter', 'This is us', 'The Crown',
               'House', 'Los Simpsons', 'Cobra Kai', 'Narcos', 'Stranger Things')
    m = open(fd, 'wt')
    for tit in titulos:
        genero = random.randint(0, 5)
        idioma = random.randint(0, 4)
        temporadas = random.randint(1, 10)
        duracion = random.randint(60, 600)
        linea = '{},{},{},{},{}\n'.format(tit, genero, idioma, temporadas, duracion)
        m.write(linea)
    m.close()
    print('Archivo',fd,'generado.')


if __name__ == '__main__':
    generar_archivo_csv()
