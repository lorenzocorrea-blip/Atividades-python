i=int(input("Digite seu primeiro número: ")) # lê os números digitados pelo usuário e os mostra em ordem crescente
j=int(input("Digite seu segundo número: "))
n=int(input("Digite seu terceiro número: ")) 

if i <= j and i <= n: # se o primeiro número for menor ou igual ao segundo e ao terceiro, ele é o menor
    print(i)
    if j <= n:
        print(j)
        print(n)
    else:
        print(n)
        print(j)
elif j <= i and j <= n: # se o segundo número for menor ou igual ao primeiro e ao terceiro, ele é o menor
    print(j)
    if i <= n:
        print(i)
        print(n)
    else:
        print(n)
        print(i)
else:
    print(n) # se o terceiro número for menor ou igual aos outros dois, ele é o menor
    if i <= j:
        print(i)
        print(j)
    else:
        print(j)
        print(i)