num= int(input('Digite um número com 3 digitos: '))
#Primeiro digito

d1= num // 100


print('Primeiro digito: ', d1)# // Parte inteira da divisão

#Segundo digito
d2= num % 100 //10
print('Segundo digito: ', d2)# % Resto da divisão

#Terceiro digito
d3= num % 10
print('Terceiro digito: ', d3)# % Resto da divisão

inverso = d3 *100 + d2 * 10 + d1
print('Numero Invertido: ', inverso)