print("nolasco_aguilar_martha_sofia_0948_3W")
#abre la funcion 
def my_function(a):
    try:
        int(a)
    except:
        return False;
    return True;
#cuenta el numero de variables 
def length(a):
    i = 0
    if not (my_function(a)):
        for i in range(len(a)):
            i = i + 1
    elif(my_function(a)):
        return(a)
    return(i)
print(length("hola prof"))
print(length(["1","2","3","4"]))