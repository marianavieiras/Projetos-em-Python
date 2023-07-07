salario = float(input("Adicione o salário do funcionário: "))
if salario <= 1903.98:
    print("Insento do Importo de  Renda")
elif salario >= 1903.99 and salario <= 2826.65:
    imposto = salario * 0.075 - 142.80
    print ("Imposto a ser pago: ", imposto)
elif salario >= 2826.66 and salario <= 3751.05:
    imposto = salario * 0.15 - 354.80
    print ("Imposto a ser pago: ", imposto)
elif salario >= 3751.06 and salario <= 4664.68:
    imposto = salario * 0.225 - 636.13
    print ("Imposto a ser pago: ", imposto)
elif salario >= 4664.69:
    imposto = salario * 0.275 - 869.36
    print ("Imposto a ser pago: ", imposto)


