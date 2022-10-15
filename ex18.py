import math
a = float(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(a))
print('O angulo de {:.1f} tem o seno de {:.2f}'.format(a, seno))
cosseno = math.cos(math.radians(a))
print('O angulo de {:.1f} tem o cosseno de {:.2f}'.format(a, cosseno))
tangente = math.tan(math.radians(a))
print('O angulo de {:.1f} tem a tangente de {:.2f}'.format(a, tangente))
