dist = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f} Km/h'.format(dist))
if dist <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format((dist * 0.50)))
else: print('E o preço da sua passagem será de R${:.2f}'.format((dist * 0.45)))