import Funciones

#Función principal.
def main():
    op = 0
    vec = []
    matriz = []
    while op != 8:
        op = int(input("\nLibreria Musical Digital\n"
                       "Elija entre las siguientes opciones:\n"
                       "1- Cargar datos desde el archivo ordenando por titulo.\n"
                       "2- Generar lista de n temas para un idioma i.\n"
                       "3- Cantidad de temas por género e idioma.\n"
                       "4- Cantidad de temas para un género g.\n"
                       "5- Búsqueda por nombre.\n"
                       "6- Generar archivo binario por idioma\n"
                       "7- Verificar existencia de archivo binario\n"
                       "8- Salir del programa\n"
                       "Ingrese su opción: "))
        if op == 1:
            vec = Funciones.carg_arreglo_in_order()
        elif op == 2:
            new_vec = Funciones.temaeidioma(vec)
        elif op == 3:
            matriz = Funciones.matriz_conteo(vec)
        elif op == 4:
            Funciones.busc_gen(matriz)
        elif op == 5:
            Funciones.busc_title(vec)
        elif op == 6:
            Funciones.gen_bin_arch(vec)
        elif op == 7:
            Funciones.comp_arch(vec)
        elif op == 8:
            pass

    input("Programa finalizado. Enter para cerrar")

if __name__ == '__main__':
    main()
