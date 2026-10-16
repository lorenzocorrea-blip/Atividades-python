n = int(input("Digite um ano: ")) # lendo o ano digitado pelo usuário
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0: # se o ano for divisível por 4 e não for divisível por 100 ou se o ano for divisível por 400, ele é bissexto. senão ele não é bissexto.
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")