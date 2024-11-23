print("nolasco_aguilar_martha_sofia_0948_3W")
def es_palindromo(cadena):#abre la funcion
    return cadena == cadena[::-1]#cambia el texto de manera invertida

print(es_palindromo("radar"))        # indica true 
print(es_palindromo("palabra"))      # indica false

