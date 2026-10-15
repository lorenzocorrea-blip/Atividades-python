i = float(input("Digite o seu primeiro número:"))# lê o primeiro número digitado pelo usuário
j = float(input("Digite o seu segundo número:"))# lê o segundo número digitado pelo usuario
if i > j: # se o primeiro número for maior que o segundo ele é o maior e se os dois são iguais, eles são iguais
    print("O maior número é:", i)
elif j > i:
    print("O maior número é:", j)
else:
    print("Os números são iguais.")