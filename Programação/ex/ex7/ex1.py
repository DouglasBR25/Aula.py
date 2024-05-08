idade= int (input('Digite sua idade: '))
if idade < 16:
    print ('não-eleitor')
elif idade>=18 and idade<=60:
    print ('eleitor obrigatório')
else:
    print('eleitor facultativo')