t= (input('Digite o tipo de hospedagem\nS - simples \nD - duplo\nT - triplo: ')).upper()
d= int (input('Digite a quantidade de diária: '))
if t =='S' or t=='D' or t=='T':
    if t =='s':
        print ('Simples - R$',255.50*d)
elif t =='d':
        print ('Duplo - R$',305.50*d)
elif t =='t':
    print ('Triplo - R$',360.50*d)
else:
    print('Tipo invalido')