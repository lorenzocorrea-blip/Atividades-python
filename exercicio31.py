n = int(input("Digite o lado do seu triangulo: ")) # lê o primeiro lado do triangulo
i = int(input("Digite o segundo lado do seu triangulo: ")) # lê o segundo lado do triangulo
f = int(input("Digite o terceiro lado do seu triangulo: ")) # lê o terceiro lado do triangulo

if n + i > f and n + f > i and i + f > n: # se a soma de dois lados for maior que o terceiro lado, ele é um triangulo valido. senão ele não é um triangulo valido.
    
    if n == i and n == f: # se os três lados forem iguais, ele é um triangulo equilatero
        print("O triangulo é equilatero.")
    elif n == i or n == f or i == f: # se dois lados forem iguais, ele é um triangulo isosceles
        print("O triangulo é isosceles.")
    else: # senão ele é um triangulo escaleno
        print("O triangulo é escaleno.")
else:
    print("Os lados não formam um triangulo valido.")