dias = int(input('Por quantos dias o carro foi alugado ? '))
km = float(input('Quantos Km foram percorrido com o carro ? '))

cdia = dias*60
ckm = km*0.15

total = cdia + ckm

print('O aluguel do carro ficará em R${:.2f}'.format(total))
