class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

nome= input("Digite o nome: ")
salario = float(input("Digite o salário: "))

funcionario = Funcionario(nome, salario)

print("Nome:", funcionario.nome)
print("Salário:", funcionario.salario)
