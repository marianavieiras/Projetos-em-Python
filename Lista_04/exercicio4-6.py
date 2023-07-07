def segundos (dia, hora, minutos, segundos):
    dia = dia * 86400
    hora = hora * 3600
    minutos = minutos * 60
    total = dia + hora + minutos + segundos
    return total

dias = int(input("Adicione a quantidade de dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundo = int(input("Segundos: "))
print ("Total de segundos adicionado: ", segundos(dias, horas, minutos, segundo))