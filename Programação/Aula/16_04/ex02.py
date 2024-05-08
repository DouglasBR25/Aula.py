#função range - gera sequencias
for i in range(10): # de 0 a 9
    print(i, end=' ')
print('\n')

seq=range(10)
print(seq)
for i in seq:
    print(i, end=' ')
    valor= i + 10
    print(valor, end=' ')
print('\n')

for i in range(3, 8): #de 3 a 7
    print(i, end=' ')
print('\n')

for i in range(0, 21, 2):#de 0 a 20 de 2 em 2
    print(i, end=' ')
print('\n')

for i in range(5, 20, 3):
    print(i, end=' ')