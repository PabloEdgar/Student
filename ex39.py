from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
anos = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, anos, atual))
if anos == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif anos < 18:
    saldo = 18 - anos
    print('Faltam {} anos para o alistamento.'.format(saldo))

elif anos > 18:
    saldo = anos - 18
    print('Você deveria ter se alistado há {} anos.'.format(saldo))


