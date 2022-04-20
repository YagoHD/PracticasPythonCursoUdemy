print("Proporcione los siguientes datos del libro:")
nombre=input("Proporciona el nombre: ")
ID=int(input("Proporciona el ID: "))
precio=float(input("Proporciona el precio: "))
envio=(input("Indica si el envio es gratuito (True/False): "))

if envio == "True":
    envio = True
elif envio == "False":
    envio = False
else:
    envio = "Valor incorrecto, debe escribir True/False"

print(f'''
    Nombre: {nombre}
    Id: {ID}
    Precio: {precio}
    Envio Gratuito?: {envio}
''')