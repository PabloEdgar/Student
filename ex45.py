from random import randint
from time import sleep
itens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(0, 2)

print("\033[33mSua opções:")
print("""[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

jogador = int(input("Qual é a sua jogada? \033[m"))
print("\033[34mJO\033[m")
sleep(1)
print("\033[35mKEN\033[m")
sleep(1)
print("\033[36mPO!!!\033[m")


print("-=" * 11)
print("\033[30mO computador escolheu {}\033[m".format(itens[computador]))

print("\033[32mJogador jogou {}\033[m".format(itens[jogador]))
print("-=" * 11)

if computador == 0:    # computador jogou pedra
    if jogador == 0:
        print("\033[33MEMPATE!\033[m")

    elif jogador == 1:
        print("\033[32mJOGADOR VENCE!\033[m")

    elif jogador == 2:
        print("\033[31mCOMPUTADOR VENCEU!\033[m")

    else:
        print("\033[31mJogada inválida\033[m")
elif computador == 1:  # computador jogou papel
    if jogador == 1:
        print("\033[33MEMPATE!\033[m")

    elif jogador == 2:
        print("\033[32mJOGADOR VENCE!\033[m")

    elif jogador == 0:
        print("\033[31mCOMPUTADOR VENCEU!\033[m")

    else:
        print("\033[31mJogada inválida\033[m")

elif computador == 2:  # computador jogou tesoura
    if jogador == 2:
        print("\033[33MEMPATE!\033[m")

    elif jogador == 0:
        print("\033[32mJOGADOR VENCE!\033[m")


    elif jogador == 1:
        print("\033[31mCOMPUTADOR VENCEU!\033[m")

    else:
        print("\033[31mJogada inválida\033[m")



