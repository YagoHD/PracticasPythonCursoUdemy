# TIPOS DE VARIABLES

# TIPO INT
x = 10
print('IMPRIME LA VARIABLE          ', x)
print("IMPRIME LA CELDA DE MEMORIA  ", id(x))
print("IMPRIME LE TIPO DE VARIABLE  ", type(x))
print()

# TIPO STRING
x = "HOLA"
print('IMPRIME LA VARIABLE          ', x)
print("IMPRIME LA CELDA DE MEMORIA  ", id(x))
print("IMPRIME LE TIPO DE VARIABLE  ", type(x))
print()

# TIPO FLOAT (AQUI SE LO PUSE A MANO PARA OBSERVAR QUE ES POSIBLE HACERLO EN PYTHON)
x: float = 4.3
print('IMPRIME LA VARIABLE          ', x)
print("IMPRIME LA CELDA DE MEMORIA  ", id(x))
print("IMPRIME LE TIPO DE VARIABLE  ", type(x))
print()

# TIPO BOOLEAN
x = False
print('IMPRIME LA VARIABLE          ', x)
print("IMPRIME LA CELDA DE MEMORIA  ", id(x))
print("IMPRIME LE TIPO DE VARIABLE  ", type(x))
print()

# CADENA (STRING)
miGrupoFavorito = "CamelPhat" + " " + " Musica Electronica"
print("Mi grupo favorito es: " + miGrupoFavorito)

# IMPRIMIR SUMA de STRINGS
numero1 = "20"
numero2 = "30"
print(numero1 + numero2)  # IMPRIME LOS DOS NUMEROS TAL CUAL
print(int(numero1) + int(numero2))  # IMPRIME LA SUMA
