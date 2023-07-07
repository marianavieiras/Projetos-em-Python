class Carro:
    def __init__(self, combustivel):
        self.combustivel = combustivel
        self.qnt = 0

    def andar(self, distancia):
        necessario = distancia / self.combustivel

        if necessario <= self.qnt:
            self.qnt -= necessario
        else:
            print("Combustivel não será possivel para a distancia")

    def abastecer(self, quantidade):
        self.qnt += quantidade


consumo = float(input("Adicione o consumo de combustível do carro: "))
carro = Carro(consumo)

distancia = float(input("Adicone a distância: "))
carro.andar(distancia)

abastecer = float(input("Adicione a quantidade que deseja abastecer: "))
carro.abastecer(abastecer)

print("Tanque contém:", carro.qnt)
