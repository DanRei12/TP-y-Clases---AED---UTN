'''n = 20
v = n * [0]
for i in range(n):
    v[i] = 3*i
'''

def selection_sort(v):
    # ordenamiento por seleccion directa
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] < v[j]:
                v[i], v[j] = v[j], v[i]
    print(v)

selection_sort()
