v1= float(input('Valor 1: '))
v2= float (input('valor 2: '))
c= (input('Digite o numero referente as operações abaixo: \n1)Soma \n2)Subtração \n3)Multiplicar \n4)Dividir: '))
somar= v1 + v2
subtrair= v1 - v2
multiplicar= v1 * v2
dividir= v1 / v2


if c==1:
        print (somar)
elif c==2:
    print (subtrair)
elif c==3:
    print (multiplicar)
elif c==4:
    print (dividir)
else:
    print ('Numero das operações selecionada invalida')