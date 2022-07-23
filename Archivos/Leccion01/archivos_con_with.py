#Con with ya se abre y se cierra el archivo, por lo que no es necesario añadir un try finally
# with open("prueba.txt","r",encoding="utf8") as archivo:
from ManejoArchivos import ManejoArchivos

with ManejoArchivos("prueba.txt") as archivo:
    print(archivo.read())

