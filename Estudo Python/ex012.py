preco = float(input('Qual o valor do produto ? R$'))
desc = preco - (preco*5/100)
print('O protudo que custa R${:.2f}, com o desconto de 5% fica R${:.2f}'.format(preco, desc))
