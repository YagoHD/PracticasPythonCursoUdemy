def sumarValores(*args):
    resultado = 0
    #ITERAMOS CADA ELEMENTO
    for elemento in args:
        #resultado = resultado + valor
        resultado += elemento
    return resultado

# LLAMADA FUNCION
print(sumarValores(5,7,8,15))