
print("escolha o produto que deseja comprar:" \
"\n1 - Pão de queijo 4,50 "  \
"\n2 - coxinha 6,00" \
"\n3 - Pastel 7,50" \
"\n4 - Suco 5,00" \
"\n5 - Café 3,00")

produto=int(input("Digite o código do produto: ")) # lê o código do produto digitado pelo usuário
quantidade=int(input("Digite a quantidade do produto: ")) # lê a quantidade do produto digitado pelo usuário

if produto == 1: # se o código for igual a 1, ele é pão de queijo, se for igual a 2, ele é coxinha, se for igual a 3, ele é pastel, se for igual a 4, ele é suco e se for igual a 5, ele é café. Se o código não estiver entre 1 e 5, ele é inválido.
    total = quantidade * 4.50
    print("O total da compra é: R$", total)
elif produto == 2:
    total = quantidade * 6.00
    print("O total da compra é: R$", total)
elif produto == 3:
    total = quantidade * 7.50
    print("O total da compra é: R$", total)
elif produto == 4:
    total = quantidade * 5.00
    print("O total da compra é: R$", total)
elif produto == 5:
    total = quantidade * 3.00
    print("O total da compra é: R$", total)
else:
    print("Código do produto inválido.")