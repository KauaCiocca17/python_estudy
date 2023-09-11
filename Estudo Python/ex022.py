nome = str(input('Digite seu nome: ')).strip()
#Letras Maiúsculas
print('Seu nome em maiúsculas é {}'.format(nome.upper()))

#Letras Minúsculas
print('Seu nome em minúsculo é {}'.format(nome.lower()))

#Quantidades de letras

print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))

#Quantidade de letras no primeiro nome

print(len(nome.split()[0]))