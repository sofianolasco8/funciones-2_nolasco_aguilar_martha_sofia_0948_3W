print("nolasco_aguilar_martha_sofia_0948_3W")
def mayor(a,b,c):#abre la funcion 
    if((a > b) and (a > c)):#si a es mayor que b y mayor que c
        return a#muestra "a"
    if((b > a) and (b > c)):#si b es mayor que a y c 
        return b #muestra "B"
    if((c > a) and (c > b)):#si c es mayor que a y b 
        return c #muestra "c"
print(mayor(100,200,300))#le da valor a "a","b","c"