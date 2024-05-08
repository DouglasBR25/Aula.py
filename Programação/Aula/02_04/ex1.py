f= int (input('Digite seu percentual de frequência: '))
media= float (input('Digite sua média: '))
if f <75:
    print ('Reprovado por falta')
elif media < 6: 
    print ('Repovado por nota')
else:
    print('Aprovado')