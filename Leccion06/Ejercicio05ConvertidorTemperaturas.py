"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.
"""
def celsiusToFahrenheit(temperaturaCelsius):
    return (temperaturaCelsius * 9/5) + 32

def fahrenheitToCelsius(temperaturaFahrenheit):
    return (temperaturaFahrenheit - 32) * 5/9


temperatura = int(input("Introduce la temperatura: "))
print(f"{temperatura} grados Celsius son: {celsiusToFahrenheit(5)} grados Fahrenheit")
print(f"{temperatura} grados Fahrenheit son: {fahrenheitToCelsius(5)} grados Celsius")