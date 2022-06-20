# DICCIONARIOS EN PYTHON -> KEY Y VALOR ASOCIADO A LA LLAVE
diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programming",
    "DBMS": "Database Management System"
}
print(diccionario)
# IMPRIMIR EL LARGO
print(len(diccionario))
# ACCEDER A UN ELEMENTO (key)
print(diccionario["IDE"])
# OTRA FORMA DE ACCEDER A UN ELEMENTO
print(diccionario.get("OOP"))
# MODIFICAR ELEMENTOS
diccionario["IDE"] = "integrated development enviroment"
print(diccionario)
print("")
# RECORRER ELEMENTOS DE UN DICCIONARIO
for termino, valor in diccionario.items():
    print(termino, valor)

for termino in diccionario.keys():
    print(termino)

for valor in diccionario.values():
    print(valor)

# COMPROBAR EXISTENCIA DE UN ELEMENTO
print("IDE" in diccionario)
# AGREGAR ELEMENTO A DICCIONARIO
diccionario["PK"] = "Primary Key"
print(diccionario)
# ELIMINAR UN ELEMENTO
diccionario.pop("DBMS")
print(diccionario)
# LIMPIAR ELEMENTOS
diccionario.clear()
print(diccionario)
# ELIMINAR DICCIONARIO POR COMPLETO
del diccionario