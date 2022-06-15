print("Proporcione los siguientes datos del libro: ")
ID = int(input("Proporcione la id (4 numeros): "))
nombre = input("Proporcione el nombre: ")
precio = float(input("Proporciona el precio: "))
envio = input("El envio es gratuito (True/False)")

# TENEMOS QUE COMPROBAR SI EL ENVIO ES GRATUITO O NO YA QUE DIRECTAMENTE
# POR TECLADO NO PODEMOS RECIBIR UN BOOLEANO
if envio == "True":
    envio = True
elif envio == "False":
    envio = False
else:
    envio = "Valor incorrecto, debe escribir True/False"

print(f'''
Nombre: {nombre}
ID: {ID}
Precio: {precio}
Envio Gratuito: {envio}''')