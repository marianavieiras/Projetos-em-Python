def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print("O MDC é:", mdc(num1, num2))

