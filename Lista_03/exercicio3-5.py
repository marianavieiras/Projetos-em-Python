numero = int(input("Digite um número inteiro: "))

for i in range(2, int(numero**0.5) + 1):
    if numero % i == 0:
     print("Não é um número primo")
    else:
     print("É um número primo")