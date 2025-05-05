# Atividade 2 - Resolver com Math Case, pasta 2

codigo = int(input('Informe o código: '))

match codigo:
    case 1:
        print('Sul')
    case 2:
        print('Norte')
    case 3:
        print('Leste')
    case 4:
        print('Oeste')
    case 5 | 6:
        print('Nordeste')
    case 7 | 8 | 9:
        print('Sudeste')
    case 10:
        print('Centro-Oeste')
    case 11:
        print('Noroeste')
    case _ :
        print('Importado')

# Atividade:

print(float(input('Informe ')))