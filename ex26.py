fr = str(input('Digite uma frase :').strip().upper())
print('A letra A aparece {} na frase.'.format(fr.count('A')))
print('A primeira letra A aparece {} na frase.'.format(fr.find('A')+1))
print('A última letra A aparece {} na frase.'.format(fr.rfind('A')+1))
