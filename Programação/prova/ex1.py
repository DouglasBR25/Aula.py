import math
x1= float (input('Digite o valor de x1: '))#0
x2= float (input('Digite o valor de x2: '))#4
y1= float (input('Digite o valor de y1: '))#0
y2= float (input('Digite o valor de y2: '))#4
D= (((x2 - x1)**2) + ((y2 - y1)**2))
raizD= math.sqrt((math.fabs(D)))

print('A distancia entre os dois pontos são:', raizD, D)
