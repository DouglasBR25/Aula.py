a=int(input('Digite o valor de A: '))
b=int(input('Digite o valor de B: '))
c=int(input('Digite o valor de C: '))
delta= b**2 -4*a*c
raizdelta= delta**0.5
yp= (-b + raizdelta) / (2*a)
yn= (-b - raizdelta) / (2*a)

if a ==0:
    print('Não é equação de segundo grau')
elif delta >=0:
    print('Primeira raiz:',yp,'\nSegunda raiz:',yn)
else:
    print('Não há raízes reais')