# Los elementos set no mantienen un orden, no tienen un indice, no se pueden modificar los que estan en el set,
# no permite duplicados, pero si se pueden eliminar o añadir

planetas = {"Mercurio", "Venus", "Tierra"}
print(planetas)
# LARGO DEL SET
print(len(planetas))
# REVISAR SI UN ELEMENTO ESTA PRESENTE TAMBIEN SE PUEDE CON LISTAS Y TUPLAS
print("Tierra" in planetas)
#AGREGAR UN ELEMENTO
planetas.add("Marte")
print(planetas)
planetas.add("Tierra") # NO APARECE POR QUE SERIA DUPLICADO
# ELIMINAR ELEMENTO
planetas.remove("Tierra") # DA ERROR SI ESE ELEMENTO NO ESTA EN EL SET
print(planetas)
planetas.discard("Venus") # NO DA ERROR SI ESE ELEMENTO NO ESTA EN EL SET
print(planetas)
# VACIAR EL SET
planetas.clear()
print(planetas)
# ELIMINAR POR COMPLETO EL SET
del planetas