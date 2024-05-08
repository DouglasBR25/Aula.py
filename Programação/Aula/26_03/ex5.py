n1= int (input('valor da compra: '))
n2= int (input('código referente: '))
if n2==1:
    print ('Sua compra deu R$',n1-(n1*0.10))
else: 
    print('Sua compra deu R$',n1-(n1*0.05))