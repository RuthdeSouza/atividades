TEMPERATURA_IDEAL = 25

temperatura = int(input('Informe a temperatura: '))

# if temperatura > TEMPERATURA_IDEAL or TEMPERATURA_IDEAL < temperatura:
#     print('Equipamento dentro da normalidade')

if temperatura >= 15 and temperatura <= 25:
    print('Equipamento dentro da normalidade')