#Empieza el programa
print("Bienvenido a este nuevo programa.\n")
prog = 1
while prog:
    # Elección de nuestras opciones.
    prog = int(input("Selecciona una de las siguientes opciones ingresando el número correspondiente:"
                     "\n""1- Ventas de sucursales""\n""2- Texto(analisis de 'p' y 'j') "
                     "\n""3- Terminar programa\n"
                     "\n""Numerito aqui: "))


    # Opción para el programa 1.
    if prog == 1:
        NLocal1 = input("Ingrese el nombre de la primera sucursal")
        VLocal1 = input("Ingrese la cantidad de ventas primera sucursal")

        NLocal2 = input("Ingrese el nombre de la segunda sucursal")
        VLocal2 = input("Ingrese la cantidad de ventas segunda sucursal")

        NLocal3 = input("Ingrese el nombre de la tercer sucursal")
        VLocal3 = input("Ingrese la cantidad de ventas tercer sucursal")


        print(NLocal1,VLocal1,NLocal2,VLocal2,NLocal3,VLocal3)
