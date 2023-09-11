num = int(input('Digite um número qualquer: '))
resto = num % 2
if resto == 0:
    print('O número {} é PAR.'.format(num))
else :
    print('O número {} é ÍMPAR.'.format(num))