m1 = float(input('Digite distância em metros: '))
km = m1/1000
het = m1/100
dec = m1/10
decm = m1*10
cent = m1*100
mil = m1*1000

print('A média de {}m corresponde a: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(m1, km, het, dec, decm, cent, mil))
