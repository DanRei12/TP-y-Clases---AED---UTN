import math
import os.path
import pickle
class Point:
    def __init__(self, cx, cy, desc='p'):
        self.x = cx
        self.y = cy
        self.descripcion = desc


def to_string(point):
    r = str(point.descripcion) + ' (' + str(point.x) + ', ' + str(point.y) + ')'
    return r

def carg_arreglo_in_order():
    vec1 = []
    tbm = os.path.getsize("puntos.df4")
    m = open("puntos.df4", "rb+")

    '''for point in m:
        point = point[:-1]
        token = point.split(",")
        point = Point(int(token[0]), int(token[1]), token[2])'''

    while m.tell() < tbm:
        art = pickle.load(m)
        print(to_string(art))
        vec1.append(art)

    print("\nCarga generada correctamente.\n")
    m.close()
    return vec1

def distance_between(p1, p2):
    # calcular "delta y" y "delta x"
    dy = p2.y - p1.y
    dx = p2.x - p1.x

    # Distancia entre ellos... Pitágoras...
    return math.sqrt(pow(dx, 2) + pow(dy, 2))

def main():
    vec1 = carg_arreglo_in_order()
    dmax = 0
    dmin = -1
    n = 5000

    #Mayor diferencia
    for i in range(0, n-1):
        for j in range(i+1, n):
            d = distance_between(vec1[i], vec1[j])
            if dmin < 0:
                dmin = d
            if d < dmin:
                dmin = d
            if d > dmax:
                dmax = d

    print("La distancia mínima fue de", dmin)
    print("La distancia maxima fue de", round(dmax))



# Script principal...
if __name__ == '__main__':
    main()
