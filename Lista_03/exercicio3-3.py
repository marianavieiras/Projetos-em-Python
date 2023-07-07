num = []
soma = 0
media = 0
for _ in range(5):
    valor = int(input("Adicione o valor desejado: "))
    num.append(valor)
    soma += valor
    if valor > maior:
        maior = valor
    media = soma/5