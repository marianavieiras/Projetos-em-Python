area = float(input("Adicione a area em metros quadrados que deseja pintar: "))
qnt = area / 3
latas = qnt / 18

if latas > int(latas):  
    latas_inteiras = int(latas) + 1
else:
    latas_inteiras = int(latas)

valor = latas_inteiras * 80

print("Quantidade de latas de tinta a serem compradas:", latas_inteiras)
print("Preço total: R$", valor)