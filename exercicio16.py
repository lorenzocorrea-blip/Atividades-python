saldo = float(input("Digite o saldo da sua conta: "))# lê o saldo da conta
valor_saque = float(input("Digite o valor que deseja sacar: "))# lê o valor que deseja sacar
if saldo >= valor_saque: # se o saldo for maior ou igual ao valor do saque, ele faz o saque     
    print("Saque realizado com sucesso!")
    print("Saldo atual: ", saldo - valor_saque) 
else: # se o saldo for menor que o valor do saque, ele não faz o saque
    print("Saldo insuficiente para realizar o saque.")
    print("Novo saldo: ", saldo) # exibe o saldo atual