print('{:=^40}'.format('LOJAS TK CIOCCA'))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À VISTA DINHEIRO/CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opcao = int(input('Qual a sua opção: '))

if opcao == 1:
    desc = preco - (preco/100 * 10)
    print('O valor será de R${:.2f}'.format(desc))
elif opcao == 2:
    desc = preco - (preco/100 * 5)
    print('O valor será de R${:.2f}'.format(desc))
elif opcao == 3:
    print('O valor será de R${:.2f}'.format(preco))
else:
    desc = preco + (preco/100 * 20)
    print('O valor da compra é de R${:.2f}'.format(desc))