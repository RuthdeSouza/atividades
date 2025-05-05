# Atividade prática, pasta 2 

# Calacular a média de um estudante.
# Média > 7 Aprovado
# Média entre 5 e 7 Recuperação
# Média < 5 Reprovado


soma = 0.0
for i in range(4):
    soma += float(input('Informe a nota: '))

media = (soma) / 4

print('A média é', media)

if media < 5:
    print('Reprovado')

elif media <= 7:
    print('Recuperação')

else: 
    print('Aprovado')