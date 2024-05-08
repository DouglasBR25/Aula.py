produto= int(input(': '))
compra= float (input(': '))
desconto70= compra + (compra*0.70)
desconto50= compra + (compra*0.50)
desconto40= compra + (compra*0.40)
desconto30= compra + (compra*0.30)

if compra < 10:
    print ('Produto:',produto, '\nValor da venda:',desconto70)
elif compra <= 10 and compra<30:
    print ('Produto:',produto, '\nValor da venda:',desconto50)
elif compra <= 30 and compra<50:
    print ('Produto:',produto, '\nValor da venda:',desconto40)
else:
    print('Produto:',produto, '\nValor da venda:',desconto30)