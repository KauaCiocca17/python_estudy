km = int(input('Qual distância da sua viajem: '))
if km <= 200:
    preco = km * 0.50
    print('O valor de uma viajem de {}KMs será de R${:.2f}.'.format(km, preco))

else:
    preco = km * 0.45
    print('O valor de uma viajem de {}KMs será de R${:.2f}.'.format(km, preco))