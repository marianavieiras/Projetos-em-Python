valor = int(input("Digite o valor do saque: "))

if valor < 10 or valor > 1000 or valor % 10 != 0:
    print("Valor de saque inválido.")
else:
    notas_200 = 0
    notas_100 = 0
    notas_50 = 0
    notas_10 = 0
    while valor >= 200:
        valor -= 200
        notas_200 += 1
    while valor >= 100:
        valor -= 100
        notas_100 += 1
    while valor >= 50:
        valor -= 50
        notas_50 += 1
    while valor >= 10:
        valor -= 10
        notas_10 += 1
        
    print("Notas de:")
    if notas_200 > 0:
        print(notas_200, "nota(s) de R$200")
    if notas_100 > 0:
        print(notas_100, "nota(s) de R$100")
    if notas_50 > 0:
        print(notas_50, "nota(s) de R$50")
    if notas_10 > 0:
        print(notas_10, "nota(s) de R$10")


