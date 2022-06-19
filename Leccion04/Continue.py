# for i in range(6):
#     if i % 2 == 0:
#         print(f"Valor: {i}")

for i in range(6):
    if i % 2 != 0:
        continue  # Si se cumple lo de arriba, se saltan las operaciones en este caso imprimir
    print(f"Valor: {i}")
