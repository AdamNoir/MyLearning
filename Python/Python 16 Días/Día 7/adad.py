repeticiones = 5
numero_mayor = 0

while repeticiones > 0:
    valor_usuario = int(input("Valor: "))
    if valor_usuario > numero_mayor:
        numero_mayor = valor_usuario
    repeticiones = repeticiones - 1

print(numero_mayor)
