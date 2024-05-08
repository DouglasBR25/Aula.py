vt= float(input('Digite o valor da compra: '))
p= int(input('Digite o numero de parcelas disponiveis abaixo:\n2 parecelas \n4 parecelas \n6 parcelas \n8 parcelas: '))
p2= (vt*0.03 + vt) /2
p4= (vt*0.07 + vt) /4
p6= (vt*0.09 + vt) /6
p8= (vt*0.12 + vt) /8

if  p==2 or p==4 or p==6 or p==8:
    if p == 2:
        print ('São 2 parcelas de', p2) 
    elif p == 4:
        print ('São 4 parcelas de', p4) 
    elif p == 6:
        print ('São 6 parcelas de', p6) 
    elif p == 8:
        print ('São 8 parcelas de', p8) 
    else:
        print('Parcela inserida inválida')

