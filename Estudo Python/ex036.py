casa = float(input('Qual o valor da casa R$'))
sala = float(input('Qual salário do comprador R$'))
anos = int(input('Quantos anos de financiamento? '))

prestação = casa / (anos * 12)
minimo = sala * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end=(''))
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')