idade = int(input("Digite a idade da pessoa: ")) # lendo a idade digitada pelo usuário
if idade < 0: # se a idade for menor que 0, ela é inválida, se for entre 0 e 12, ela é criança, se for entre 13 e 17, ela é adolescente, se for entre 18 e 59, ela é adulto e se for maior ou igual a 60, ela é idoso.
    print("Idade inválida.")
elif idade <= 12:
    print("Criança.")
elif idade <= 17:
    print("Adolescente.")
elif idade <= 59:
    print("Adulto.")
else:
    print("Idoso.")