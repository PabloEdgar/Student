print("{:=^40}".format("\033[32mLojas Gundum\033[m"))
preço = float(input("preço das compras: R$"))
print('''FOrmas DE PAGAMENTO 
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão''')
opção = int(input("Qual é a opção? "))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print("Sua compra será parcelada em 2X de R${:.2f}".format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    parcela = total / 3
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print("Sua compra será parcelada em {}X de R${:.2f}".format(totparc, parcela))

else:
    total = preço
    print("\033[31mOpção invalida de pagamento")

print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preço,total))