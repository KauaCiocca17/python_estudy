sala = float(input('Qual o salário do funcionario ? R$'))

aument = sala + (sala*15/100)

print('O salário de R${:.2f} do funcionario com 15% de aumento vai para R${:.2f}'.format(sala, aument))
