anos = int(input('Idade: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))

anos_dias = anos * 365
meses_dias = meses * 30
qtde_dias = anos_dias + meses_dias + dias

print('Você tem', qtde_dias,' dias')