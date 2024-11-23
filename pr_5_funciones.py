print("nolasco_aguilar-martha_sofia_0948_3W")
def suma(a):#se abre la funcion suma  
    total = 0#se inicia un todal de 0 
    for i in range(len(a)):
        total += a[i]#se hace una suma  
    return total#muestra el total
def mult(a):#se abre la funcion muultiplicacion
    total = 1 #se iguala a uno 
    for i in range(len(a)):
        total *= a[i]
    return total# se muestra el total 
print(suma([2,3,4,5]))#se le da valor a la funcion suma 
print(mult([2,3,4,3]))#se da valor a la funcion multiplicacion 