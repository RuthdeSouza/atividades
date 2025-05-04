# Exercício 2, pasta 1:
# Desenvolver um sistema para avaliar o desempenho dos vendedores

# Excelente: > = 100 unidades
# Bom: entre 70 e 99 unidades
# Regular: entre 30 e 69 unidades
# Insuficiente: < 30 unidades


qtd_vendida = int(input('Informe a quantidade vendida: '))

if qtd_vendida < 30:
    print('Isuficiente')

elif qtd_vendida < 70:
    print('Regular')

elif qtd_vendida < 100:
    print('Bom')

else:
    print('Excelente')
