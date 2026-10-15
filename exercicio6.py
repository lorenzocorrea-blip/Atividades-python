i = float(input("digite o preço do lanche:")) # Lê o preço do lanche digitado pelo usuario
j = float(input("digite a quantidade de lanches:")) # Lê a quantidade de lanches digitada pelo usuario
print("O valor total a ser pago é:", i * j) # Calcula e exibe o valor total a ser pago
k = float(input("digite o valor pago pelo cliente:")) # Lê o valor pago pelo cliente
print("O troco é:", k - (i * j)) # Calcula e exibe o troco