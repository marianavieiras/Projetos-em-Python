def contar_vogal(string):
    cont = 0
    for i in range(len(string)):
        if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'u' or string[i] == 'A' or string[i] == 'E' or string[i] == 'I' or string[i] == 'U':
            cont += 1
    return cont

palavra = input("Adicione uma palavra: ")
print(contar_vogal(palavra))