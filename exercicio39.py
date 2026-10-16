valor = int(input())  # Lê o valor inteiro do usuário

if valor <= 0 or valor % 10 != 0:
    # Se o valor for menor ou igual a zero,
    # ou não for múltiplo de 10
    print("Valor inválido para saque")

else:
    notas = [100, 50, 20, 10]  # Valores das notas que ainda restam 

    for nota in notas:  # Percorre cada valor de nota
        quantidade = valor // nota  # Calculos
        valor = valor % nota  

        if quantidade > 0:  # Só mostra as notas que foram usadas.
            print(f"{quantidade} nota(s) de R$ {nota}")