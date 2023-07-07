def contar_caractere(string, caractere):
    cont = 0
    for i in range(len(string)):
        if string[i] == caractere:
            cont += 1
    return cont

palavra = input("Adicione uma palavra: ")
car = input("Adicione um caractere: ")
print(contar_caractere(palavra, car))
