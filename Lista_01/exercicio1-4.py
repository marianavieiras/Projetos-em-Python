valor = float(input("Adicione o valor recebido por hora:"))
hora = float(input("Adicione o numero de horas trabalhadas no mês: "))

bruto = valor * hora
imposto = bruto * 0.15
inss = bruto * 0.1
sindicado = bruto * 0.02
liquido = bruto - imposto - inss - sindicado

print ("Salario bruto: ", bruto )
print ("Imposto de renda: ", imposto)
print ("INSS: ", inss)
print ("Sindicado: ", sindicado)
print ("Liquido: ", liquido)
