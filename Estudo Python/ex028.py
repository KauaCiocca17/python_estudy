import random
al = random.randint(0,5)
resul = int(input('Tente adivinhar o número que estou pensando: '))

if al == resul:
    print('Parabéns você acertou o número!! É o número {} mesmo. Parabéns!'.format(al))
else:
    print('Putz, não é esse número que estou pensando. O número é o {}'.format(al))