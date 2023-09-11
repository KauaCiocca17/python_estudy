velo = int(input('Qual a velocidade que o caaro está: '))
if velo <= 80:
    print('Você estava dentro do limite, diriga com cuidado e boa viajem!! ')
else:
    multa = (velo-80 ) * 7
    print('Você passou do limite, e levou uma multa de R${:.2f}'.format(multa))
