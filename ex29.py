v = float(input('Qual a sua velocidade? '))
if v <= 80:
    print('Tenha um bom dia! Dirija com segurança')
else:
    print('Multado você excedeu o limite permitido que é de 80 km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format((v-80)*7))
    print('Tenha um bom dia! Dirija com segurança')
