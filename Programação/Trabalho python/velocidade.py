distancia = float ( input('Distância de Acapuco à Belem: '))
horas = float ( input('horas : '))
while True:
    minutos = float ( input('minutos : '))
    if minutos >= 0 and minutos < 60:
        break
    else:
        print("Por favor, insira um numero válido (entre 0 e 59).")
tempo_total = horas + minutos / 60
velocidade = (distancia/ tempo_total)
print('Sua velocidade é de ', velocidade, 'km/h')