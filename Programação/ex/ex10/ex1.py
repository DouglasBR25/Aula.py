qtdeEleitores = 0 #contador de item a
soma = 0 #acumulador para calcular a media - item b
qtdeNEleitores = 0 # contador para calcular a média - item b
for i in range(5):
    #para cada eleitor
    idade=int(input('Digite sua idade: '))
    if idade>=16: #aluno eleitor
        qtdeEleitores= qtdeEleitores + 1
    else: #item b
        qtdeNEleitores=qtdeNEleitores + 1
        soma = soma + idade

media= soma/qtdeNEleitores
#saída
print('Quantidade de alunos eleitores: ',qtdeEleitores)
print('Media da idade de alunos não eleitores: ', media)