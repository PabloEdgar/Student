vc = float(input('\033[32mValor da casa: '))
sc = float(input('\033[32mSalário do comprador: '))
qa = float(input('\033[32mQuantos anos de finaciamento? '))
prestação = vc / (qa * 12)
mínimo = sc * 30 / 100
print(f'Para pagar uma casa de {vc} em {qa} anos a prestação será de {prestação}')
if prestação <= mínimo:
    print('\033[32mEmpréstimo pode ser CONCEDIDO')
else:
    print('\033[31mEmpréstimo NEGADO')

