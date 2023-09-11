a = float(input('Digite o primero segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if (b-c) < a < b+c and (a-c) < b < a+c and (a-b) < c < a+b:
    print('Pode formar um triangulo!')
else:
    print('Não pode formar um triangulo')