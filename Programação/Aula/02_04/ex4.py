p= float(input('Digite seu peso: '))
a= float(input('Digite sua altura: '))
imc=(p/(a*a))

if imc <20:
    print('%.2f Abaixo do peso' %(imc))
elif imc>=20 and imc<25: 
    print ('%.2f Peso normal' %(imc))
elif imc>=25 and imc<30: 
    print ('%.2f Sobrepeso' %(imc))
elif imc>=30 and imc<40: 
    print ('%.2f Obeso' %(imc))
else: 
    print ('%.2f Obeso mórbido' %(imc))
