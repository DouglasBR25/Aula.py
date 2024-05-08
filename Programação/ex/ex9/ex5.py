resp = 's'
contF = 0
contM = 0
mediaM = 0
mediaF = 0
mediaf = 0
mediam = 0
while resp == 's' or resp == 'S':

  h = float(input('Digite sua altura: '))
  sexo = input('Digite a letra do seu sexo (M-masculino/ F-feminino): ')

  if sexo == 'M' or sexo == 'm':
    contM = contM + 1
    mediaM = h + mediaM
    mediam = mediaM / contM

  elif sexo == 'F' or sexo == 'f':
    contF = contF + 1
    mediaF = h + mediaF
    mediaf = mediaF / contF

  else:
    print('Invalido')

    #atualização da variavel de controle

  resp = input('Deseja continuar? (s/n)')

  if resp == 'n' or resp == 'N':
    print('Media de altura feminina= ', mediaf)
    print('Media de altura masculina= ', mediam)
