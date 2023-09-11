import math
ang = int(input('Digite o ângulo: '))
rad = math.radians(ang)
seno = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)

print('Pra um ângulo de {}°, o seno será de {:.2f}, o cosseno será de {:.2f}, e atngente será de {:.2f}'.format(ang, seno, cos, tang))
