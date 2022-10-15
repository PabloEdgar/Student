nome = str(input('Qual é seu nome? ')).strip().title()
if nome == 'Pablo':
    print(f'Seu nome é lindo {nome} !!')

elif nome == 'Morgana' or nome == 'Luan' or nome == 'Lorena':
    print(f'Seu nome é bem incomun {nome}')

else:
    print(f'Seu nome é bem comun {nome}')


print(f'\033[32m Tenha um bom dia, {nome}!')