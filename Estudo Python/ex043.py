peso = float(input('Qual o seu peso: (Kg) '))
alt = float(input('Qual a sua altura: (m ) '))
imc = peso / (alt * alt)

if imc < 18.5:
    print('O seu IMC é de {:.2f}, você está ABAIXO DO PESO!'.format(imc))
elif imc > 18.5 and imc < 25:
    print('O seu IMC está em {:.2f}, você está no PESO IDEAL!'.format(imc))
elif imc > 25 and imc < 30:
    print(' O seu IMC está em {:.2f}, você está com SOBREPESO !'.format(imc))
elif imc > 30 and imc < 40:
    print('O seu IMC está em {:.2f}, você está com OBESIDADE !'.format(imc))
else:
    print('O seu IMC está em {:.2f}, você está com OBESIDADE MÓRBIDA, cuidado!'.format(imc))