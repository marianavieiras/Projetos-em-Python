peso = float(input("Adicione seu peso:"))
altura = float(input("Adicione sua altura em metros: "))

imc = (peso / (altura*altura))
if imc < 18.5:
    print("Abaixo do peso, IMC: ", imc)
if imc >= 18.5 and imc <= 25.0:
    print("Peso normal, IMC:", imc)
if imc > 25.0:
    print("Sobrepeso, IMC:", imc)
    