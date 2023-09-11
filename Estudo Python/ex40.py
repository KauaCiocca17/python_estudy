pri = float(input('Qual a primeira nota: '))
seg = float(input('Qual a segunda nota: '))
med = (pri + seg) / 2

if med >= 6:
    print('Tirando {:.1f} e {:.1f} a média do aluno é de {:.1f}'.format(pri, seg, med))
    print('O aluno está APROVADO!')
elif med <= 5:
    print('Tirando {:.1f} e {:.1f} a média do aluno é de {:.1f}'.format(pri, seg, med))
    print('O aluno está REPROVADO!')
else:
    print('Tirando {:.1f} e {:.1f} a média do aluno é de {:.1f}'.format(pri, seg, med))
    print('O aluno ficou de RECUPERAÇÃO!')