# Aquí visualizamos la diferencia de la comilla (') y entre comillas (")
nombre = "Ricardo"
apellido = "Melecotroso"
print("Usted es", nombre, "cuyo apellido es", apellido)
apellido = "O'ak"
propiedad = '"Mama" de Ash'
print("Al señor", apellido, "le corresponde la", propiedad)

# Caracteres de escape
print ("_" * 90)
print('Supermercado \'BUENOS DIAS\'')
print ("-" * 90)
print('\tGalletas')
print('\tLeche')
print("\tAzucar \"Serenisima\"")
print("\n\n*** GRACIAS POR COMPRAR ***")
print ("=" * 90)

# Aquí vemos como podemos aumentar el número de algún caracter no numerico
nombre = "Diego"
apellido = "Maradona"
print("\n¡¡Felicidades!!", nombre, apellido + ".", "Su usuario ha sido generado con éxito!")
print("Usuario", nombre[0] + ".", apellido, "ha ingresado")
print("Clave:", "*" * 10)

# La siguiente función sirve para redondear el número o limitar la cantidad de decimales.
print(round(28.938))
print(round(28.938, 2))
