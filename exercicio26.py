i=float(input("Digite o valor da sua compra:"))# lê o valor da compra e aplica o desconto da faixa correspondente.
if i < 50:# de 50 a menos ele não aplica desconto,
    valor_final = i
    print("Não tem desconto:", valor_final)
elif i < 100:# se o valor da compra for menor que 100, ele aplica o desconto de 5%
    desconto = i * 0.05
    valor_final = i - desconto
    print("O valor final da compra com desconto é:", valor_final)
elif i < 200:# se o valor da compra for maior que 100, ele aplica o desconto de 10%
    desconto = i * 0.1  
    valor_final = i - desconto
    print("O valor final da compra com desconto é:", valor_final)
else:# se o valor da compra for maior que 200, ele aplica o desconto de 15%
    desconto = i * 0.15
    valor_final = i - desconto
    print("O valor final da compra com desconto é:", valor_final)
    