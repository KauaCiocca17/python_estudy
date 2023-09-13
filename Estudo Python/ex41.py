from datetime import date
atual = date.today().year
ano = int(input('Qual o ano do seu nascimento: '))
idade = atual - ano

if idade <= 9:
    print('A idade do atleta é {}, então é de categoria MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('A idade do atleta é de {}, então a cetehoria dele é INFANTIL.'.format(idade))
elif idade > 14 and idade <=19:
    print('A idade do atleta é de {}, então a cetgoria dele é JUNIOR.'.format(idade))
elif idade > 19 and idade <= 25:
    print('A idade do atleta é de {}, então a categoria dele é SÊNIOR.'.format(idade))
else:
    print('A idade do atleta é de {}, então a categoria dele é MASTER.'.format(idade))