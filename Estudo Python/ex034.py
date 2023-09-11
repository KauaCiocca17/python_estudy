sal = float(input('Qual o sálario do funcionário? R$ '))

if sal > 1250.00:
    porce = sal * 10/100
    aumento = porce + sal

else:
    sal <= 1250.00
    porce = sal * 15/100
    aumento = sal + porce

print('O aumento de sálerio de será de R${:.2f} para R${:.2f}.'.format(sal, aumento))