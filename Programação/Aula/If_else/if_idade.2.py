idade= int (input('Digite sua idade: '))
if idade >= 18:
    print ('Você pode ter CNH')
    print('Basta realizar os testes')
else:
    print('Você não pode ter CNH')
    print('Faltam',18 - idade , 'anos')

print('Palmeiras não tem mundial')