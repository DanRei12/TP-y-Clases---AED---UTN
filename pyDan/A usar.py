# un recorrido por filas
for f in range(len(m2)):
 for c in range(len(m2[f])):
  m2[f][c] = f * c

# recorrido por columnas – matriz regular
filas = 3
columnas = 4
for c in range(columnas):
 for f in range(filas):
  m3[f][c] = f * c

# carga por teclado... recorrido por filas en orden creciente...
filas, columnas = 3, 4
m4 = [[0] * columnas for f in range(filas)]
for f in range(filas):
 for c in range(columnas):
  m4[f][c] = int(input('Valor: '))
print('Matriz 4 leida:', m4)
