from datetime import date
ano = int(input('Qual o número que vcê quer analisar? Coloque o 0 para analisar o número atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} É bissexto'.format(ano))
else:
    print('O ano {} NÃO é bissexto'.format(ano))
