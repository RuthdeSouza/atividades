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

f_pag = float(input('Informe a forma de pagamento: '))
vl_compra = float(input('Informe o valor da compra: '))
vl_final = 0.0
invalido = False

match f_pag:
    case 1:
        print('PIX')
        vl_final = vl_compra
    case 2:
        print('À VISTA')
        vl_final = vl_compra * 0.9
    case 3:
        print('DÉBITO')
        vl_final = vl_compra * 1.05
    case 4:
        print('CARTÃO DE CRÉDITO')
        vl_final = vl_compra * 1.08
    case 5:
        print('CHEQUE')
        vl_final = vl_compra * 1.12
    case _:
        print('MODALIDADE INVÁLIDA')
        invalido = True
    
if invalido:
    print('Erro')
else:
    print('O valor original da compra é',vl_compra, 'O valor final da compra é', vl_final)