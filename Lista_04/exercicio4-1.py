def potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado
base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = potencia(base, expoente)
print("O resultado da potência é:", resultado)


