limite = float(input("Digite o limite de velocidade da via em km/h: "))
velocidade = float(input("Digite a velocidade medida do carro em km/h: "))

percentual_acima = (velocidade - limite) / limite * 100

if percentual_acima < 20:
    print("Sem infração ")
elif 20 <= percentual_acima < 50:
    print("Infração média")
elif 50 <= percentual_acima < 100:
    print("Infração grave")
else:
    print("Infração gravíssima")