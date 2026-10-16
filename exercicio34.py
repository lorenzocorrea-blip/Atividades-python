N= float(input("Digite a primeira nota: ")) # lê a primeira nota digitada pelo usuário
N2= float(input("Digite a segunda nota: ")) # lê a segunda nota digitada pelo usuário
F= float(input("Digite a frequência (em %): ")) # lê a frequência digitada pelo usuário

M= (N + N2) / 2 # calcula a média

if F < 75:
    print("Reprovado por falta.")
elif M < 7:
    print("Reprovado por nota.")
else:
    print("Aprovado.")