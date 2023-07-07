tam = float(input("Tamanho do arquivo para download (em MB): "))
velocidade = float(input("Velocidade de um link de Internet (em Mbps): "))

tempo = tam / velocidade
min = tempo/60

print ("Tempo aproximado que será gasto em: ", min ,"minutos")
print ("Tempo aproximado que será gasto em: ", tempo ,"segundos")