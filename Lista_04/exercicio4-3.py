def coverte (string):
    reserva = ''
    for char in string:
        reserva = char + reserva
    return reserva
    

palavra = input("Digite uma palavra: ")
convertida = coverte(palavra)
print(convertida)