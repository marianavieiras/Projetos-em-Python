while True:
    print("----- Menu -----")
    print("G - gasolina")
    print("A - Alcool")
    print("3. Sair")
    op = input("Escolha uma opção: ")
  
    if op == "G":
        litros = float(input("Quantos litros deseja de gasolina: "))
        if litros <= 20:
            total = float(litros*4.20-((4.20*litros)*0.04))
        elif litros > 20:
            total = float(litros*4.20-((4.20*litros)*0.06))
        
        print("Valor total:", total)
               
    elif op == "A": 
        litros = float(input("Quantos litros deseja de alcool: "))
        if litros <= 20:
            total = float(litros*2.80-((2.80*litros)*0.03))
        elif litros > 20:
            total = float(litros*2.80-((2.80*litros)*0.05))
        print("Valor total:", total)
        
    elif op == "3":
     print("Saindo...")
     
     break
    else:
      print("Opção inválida. Tente novamente.")
