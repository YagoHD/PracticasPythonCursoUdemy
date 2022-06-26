def multiplicarValores(*args):
    resultado = 1
    #ITERAMOS CADA ELEMENTO
    for elemento in args:
        #resultado = resultado * valor
        resultado *= elemento
    return resultado

# LLAMADA FUNCION
print("Multiplicación:", multiplicarValores(3,5,3,15))