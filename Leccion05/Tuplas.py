# Una lista/Array que no se puede modificar no es mutable
# Definir tupla
frutas = ("Naranja", "Plátano", "Guayaba")
print(frutas)
# Saber el largo
print(len(frutas))
# Acceder a cada elemento
print(frutas[0])
# Navegacion inversa
print(frutas[-1])
# Accerder a un rango de valores
print(frutas[0:1])  # Sin incluir el indice
# Recorrer elementos
for fruta in frutas:
    print(fruta, end=" ")  # Hacer que un print no tenga salto de linea -> end = ""
# Cambiar valor de tupla se puede hacer de manera indirecta -> modificar la tupla a una lista, modificarla y pasarla a tupla
frutasLista = list(frutas)
frutasLista[0] = "Pera"
frutas = tuple(frutasLista)
print("\n",frutas)