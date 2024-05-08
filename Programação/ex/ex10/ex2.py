resp='s'
while resp =='s' or resp=='S':
    h=float (input('Digite sua altura: '))
    sexo= input('Digite a letra do seu sexo (M-masculino/ F-feminino): ')
  
    if sexo=='M' or sexo=='m':
        peso_ideal= (72.7*h)-58
        print('Peso ideal= ',peso_ideal)
    elif sexo=='F' or sexo=='f':
        peso_ideal= (62.1*h)-44.7
        print('Peso ideal= ',peso_ideal)
    else:
         print('Invalido')
    
    #atualização da variavel de controle
    resp= input('Deseja continuar? (s/n)')


