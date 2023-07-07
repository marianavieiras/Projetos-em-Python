while True:
    print("----- Menu -----")
    print("1- Adicionar nota")
    print("-1 - Sair")
    op = input("Escolha uma opção: ")
  
    conjA= []
    conjB = []
    conjC = []
    conjD = []
    conjE = []
    if op == "1":
        valor = float(input("Adicione o valor da nota entre 0 e 10: "))
        if valor > 9 and valor <= 10:
           conjA.append(valor)
        elif valor > 8 and valor <= 9:
            conjB.append(valor)
        elif valor > 7 and valor <= 8:
            conjC.append(valor)
        elif valor > 6 and valor <=7:
            conjD.append(valor)
        elif valor > 0 and valor <=6:
            conjE.append(valor) 
      
    elif op == "-1":
     print("Saindo...")
     
     break
    else:
      print("Opção inválida. Tente novamente.")
