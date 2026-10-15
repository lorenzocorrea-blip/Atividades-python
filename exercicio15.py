i=float(input("digite o valor da compra:"))
if i >= 100:    
    print("O valor da compra é:", i - (i * 0.10)) # Calcula e exibe o valor da compra com desconto de 10%
else:
    print("não tem desconto") # se não tiver desconto, não tem desconto