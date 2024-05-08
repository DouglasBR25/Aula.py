h = float(input('Altura: '))
Bmaior = float(input('Base maior: '))
Bmenor = float(input('Base menor: '))
volume = (h/3* (Bmaior **2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5))

print('O volume é ', volume)