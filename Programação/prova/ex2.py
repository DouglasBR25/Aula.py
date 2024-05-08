m= int (input('Digite o número do mês(entre 1 e 12 meses): '))
p= int (input('Digite a quantidade de passagens: '))
c1= 350.99 * p
c2= 520.50 * p
c3= 450.75 * p

if p<0:
    print('Quantidade de passagens iválida')

elif m>12 or m<=0:
    print('Mês invalido')

elif m==2 or m==3 or m==4 or m==5:
    print ('O valor da passagem é:',c1)

elif m==1 or m==6 or m==7 or m==12:
    print ('O valor da passagem é:',c2)

elif m==8 or m==9 or m==10 or m==11:
    print ('O valor da passagem é:',c3)

