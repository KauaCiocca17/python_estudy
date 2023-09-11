larg = float(input('Qual a largura da parede: '))
alt = float(input('Qual a altura da parede: '))

area = larg*alt
lata = area/2
print('Sua parede tem a dimensão de {:.2f}x{:.2f}, e a sua área é de {:.2f}m²'.format(larg, alt, area))
print('Para pintar essa parede, será nescessário de {:.2f} litros de tinta'.format(lata))
