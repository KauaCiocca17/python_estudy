from datetime import date
atual = date.today(). year
ano = int(input('Qual seu ano de nascimento: '))
idade = atual - ano

if idade < 18:
    saldo = 18 - idade
    anoF = atual + saldo
    print('Você ainda é menor de idade e terá que se alistar em {}'.format(anoF))

elif idade > 18:
    saldo = idade - 18
    anoF = atual - saldo
    print('Você passou dos 18 anos e teria que ter se alistado em {}'.format(anoF))
elif idade == 18:
    print('Você tem 18 anos e deverá se alistar IMEDIATAMENTE!')