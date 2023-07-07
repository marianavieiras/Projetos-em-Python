numero = int(input("Digite um número inteiro: "))
div = []

for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
        div.append(i)
    if len(div) == 0:
        print(numero, "É um número primo")
    else:
        print(numero, "Não é um número primo. É divisível por:", div)
