import math
c1 = float(input('Digite o valor do primeiro cateto = '))
c2 = float(input('Digite o valor do segundo cateto = '))


h = math.sqrt(((c1**2) + (c2**2)))

print('O valor da hipotenusa é de {:.2f}'.format(h))
