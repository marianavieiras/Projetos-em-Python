def funcao ():
    while True:
        print("----- Menu -----")
        print("1- Adicionar valor")
        print("2- Conferir números positivos")
        print("0 - Sair")
        op = input("Escolha uma opção: ")

        lista = []
        negativos = []

        if op == "1":
            valor = int(input("Adicione o valor: "))
            if valor >= 0:
                lista.append(valor)
            elif valor < 0:
                negativos.append(valor)
        elif op == "2":
            for elemento in lista:
                print(elemento)
        elif op == "0":
            print("Saindo...")
            break
funcao ()
