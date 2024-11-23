print("nolasco_aguilar_martha_sofia_0948_3W")
def procedimiento(lista):

    # Recorrer cada número en la lista
    for numero in lista:
        # Multiplicar el carácter '*' por el número actual para generar una línea del histograma
        linea = '*' * numero
        # Imprimir la línea generada
        print(linea)

#imprime la cantidad de numeros que se muestra
procedimiento([4, 9, 7])
