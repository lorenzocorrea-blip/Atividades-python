peso = float(input("Digite o peso da pessoa em kg: ")) # lê o peso digitado pelo usuário
altura = float(input("Digite a altura da pessoa em metros: ")) # lê a altura digitada pelo usuário
imc = peso / (altura * altura) # calcula o IMC

if imc < 18.5: # se o IMC for menor que 18.5, a pessoa está abaixo do peso, se for entre 18.5 e 24.9, ela está com peso normal, se for entre 25 e 29.9, ela está com sobrepeso e se for maior ou igual a 30, ela está com obesidade.
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Classificação: Peso normal e imc é:", imc)
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso e imc é:", imc)
else:
    print("Classificação: Obesidade e imc é:", imc)

