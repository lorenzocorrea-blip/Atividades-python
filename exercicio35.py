i = int(input("Digite seu primeiro número: ")) # lendo os números e o operador digitados pelo usuário
j = int(input("Digite seu segundo número: "))
operador = input("Digite o seu operador: ")

if operador == "+": # se o operador digitado for +, ele vai somar os dois números.
    print("Resultado:", i + j)

elif operador == "-": # se o operador digitado for -, ele vai subtrair os dois números.
    print("Resultado:", i - j)

elif operador == "*": # se o operador digitado for *, ele vai multiplicar os dois números.
    print("Resultado:", i * j)

elif operador == "/": # se o operador digitado for /, ele vai dividir os dois números.
    if j == 0: # se a divisão for por zero, ele vai mostrar uma mensagem de erro.
        print("Erro: divisão por zero")
    else:
        print("Resultado:", i / j)

else:
    print("Operador inválido")
