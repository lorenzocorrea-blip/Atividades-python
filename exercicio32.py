u = input("Digite o usuário: ") #Lendo o usuário digitado pelo usuário
s = input("Digite a senha: ")

# Primeiro IF: verifica se o usuário está correto
if u == "Usuário":
    # Segundo IF: verifica se a senha ta correta. Da pra resolver com um if só.
    if s == "1234":
        print("Login realizado com sucesso.")
    else:
        print("Senha incorreta.")
else:
    print("Usuário incorreto.")


