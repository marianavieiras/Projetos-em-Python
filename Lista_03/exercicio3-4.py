par = 0
impar = 0
for _ in range(10):
    valor = int(input("Adicione o valor desejado: "))
    if valor%2 == 0:
        par += 1
    elif valor%2 != 0:
        impar += 1

print("Quantidade de numeros pares: " , par)
print("Quantidade de numeros impares: " , impar)
