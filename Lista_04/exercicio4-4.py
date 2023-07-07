def verifica(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return verifica(string[1:-1])
    else:
        return False
    
palavra = input("Digite para conferir se é palindromo: ")
print (verifica(palavra))
