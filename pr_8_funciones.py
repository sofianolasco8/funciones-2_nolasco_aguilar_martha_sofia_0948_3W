print("nolasco_aguilar_martha_sofia_0948_3W")
def superposicion(lista1, lista2):#se abre funcion
    for elemento1 in lista1: # Recorre cada elemento de la primera lista
        for elemento2 in lista2:# Compara con cada elemento de la segunda lista
            if elemento1 == elemento2:  # Si hay coincidencia
                return True
    return False  # Si no se encuentra coincidencia

print(superposicion([1, 2, 3], [3, 4, 5]))  # se mostrara un mensaje de "true"
print(superposicion([1, 2, 3], [4, 5, 6]))  # se mostrara mensaje de "false"
