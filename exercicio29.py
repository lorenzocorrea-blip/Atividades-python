n = int(input("Digite um número: ")) # lê os números digitados pelo usuário
i = int(input("Digite seu segundo número: ")) 
f= int (input("Digite seu terceiro número: ")) 
if n > i and n > f: # se n for maior que i e n for maior que f, ele é o maior número.
    print("O maior número é:", n)
elif i > f: # se i for maior que f, ele é o maior número.
    print("O maior número é:", i)
else: # senão f é o maior número.
    print("O maior número é:", f)