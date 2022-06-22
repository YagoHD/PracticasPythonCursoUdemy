"""
Ejercicio: Calculadora de Impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""
def calculaImpuestos(pago, impuesto):
    impuesto = pago + pago*(impuesto/100)
    return impuesto

pagoSinImpuesto = float(input("Proporcione el pago sin impuestos: "))
impuesto = float(input("Proporcione el impuesto: "))

total = calculaImpuestos(pagoSinImpuesto, impuesto)
print(f"El pago total es de {total}€, para un prodcucto que cuesta {pagoSinImpuesto}€ y tiene un {impuesto}% de impuestos")