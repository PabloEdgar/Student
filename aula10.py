#tempo = int(input('Quantos anos tem seu carro? '))
#if tempo <= 3:
#    print('carro novo.')
#else:
#    print('Carro velho')
#print('--fim--')
n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Dgigte sua segunda nota:'))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
#if m >= 6.0:
#    print('Sua média foi boa, Parabéns')
#else:
#    print('Sua média foi ruim, Estude Mais!!!')

print('Parabéns' if m >=6 else 'Estude Mais!')