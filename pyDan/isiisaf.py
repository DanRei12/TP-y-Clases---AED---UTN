__author__ = 'Cátedra de AED'


class Libro:
    def __init__(self, cod, tit, aut):
        self.isbn = cod
        self.titulo = tit
        self.autor = aut


def test():
    a = Libro(1, 'AAA', 'aaa')
    b = Libro(2, 'BBB', 'bbb')
    c = Libro(3, 'CCC', 'ccc')

    n = 4
    v = n * [None]
    v[0] = a
    v[1] = b
    v[2] = c
    v[3] = v[1]

    a = None
    b = None
    c = None

    for i in range(n-1):
        v[i] = None

    print('Terminado...')
    print(v)


if __name__ == '__main__':
    test()
