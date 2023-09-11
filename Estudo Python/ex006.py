import math

n1 = int(input('Insira um número = '))
dob = n1 * 2
trip = n1 * 3
raiz = math.sqrt(n1)
#raiz = n1 **(1/2)

print('O dobro de {} é de = {}'.format(n1, dob))
print('O triblo de {} é de = {}'.format(n1, trip))
print('A raiz de {} é de = {.2f}'.format(n1,raiz))