# Exercício 1, pasta 1:
# Verificar a temperatura de um sistema

# Faixa segura 15°C
# Faixa de manutenção 15°C a 25°C
# Acima de 25°C desligar imediatamente

TEMPERATURA_IDEAL = 15

temperatura = int(input('Informe a temperatura: '))

if temperatura < TEMPERATURA_IDEAL:
    print('Equipamento dentro da normalidade')

elif temperatura <= 25:
    print('Enviar Equipamento para manutenção')

else:
    print('Desligar o Equipamento Imediatamente')

