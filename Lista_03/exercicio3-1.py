while True:
    nome = input("Adicione um nome com no minimo letras: ")
    if len(nome) < 3: 
        print ("O tamanho adicionado está incorreto")
        continue
    
    idade = int(input("Digite a idade entre 0 e 150: "))
    if idade < 0 or idade > 150:
        print("Idade adicionada está incorreta")
        continue
    
    salario = float(input("Digite o salário: "))
    if salario <= 0:
        print("Salário adicionado está incorreto")
        continue

    sexo = input("Digite o sexo F para feminino ou M para masculino: ")
    if sexo != 'F' and sexo != 'M':
        print("Sexo adicionado está incorreto")
        continue

    estado_civil = input("Digite o estado civil S para solteiro, C para casado, V para viuvo e D para divorciado: ")
    if estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
        print("Estado civil inválido. Digite novamente.")
        continue
    
    print("Nome:", nome)
    print("Idade:", idade)
    print("Salário:", salario)
    print("Sexo:", sexo)
    print("Estado Civil:", estado_civil)
    
    break