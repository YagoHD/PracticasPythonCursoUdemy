from NumerosIdenticosException import NumerosIdenticosException
resultado = None
#EL RESULTADO SE PONE FUERA DEL TRY POR QUE SE UTILIZA MAS ADELANTE FUERA DEL TRY
try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    if a == b:
        #con raise lanzamos la excepcion que queramos
        raise NumerosIdenticosException("Numeros identicos")
    resultado = a/b
except ZeroDivisionError as e:#DIFERENTES TIPOS DE EXCEPCIONES
    print(f"ZeroDivisionError - Ocurrio un error: {e}, {type(e)}")
except TypeError as e:
    print(f"TypeError - Ocurrio un error: {e}, {type(e)}")
except Exception as e:
    print(f"Exception - Ocurrio un error: {e}, {type(e)}")
else:#SE EJECUTA SI NO HAY NINGUNA EXEPCION
    print("No hay ninguna excepcion, codigo correcto")
finally:#SE EJECUTA SIEMPRE
    print("Ejecucion finally")

print(f"Resultado: {resultado}")
print("Continuamos...")