d1 = float(input("digite o seu dividendo:")) # lê o dividendo e o divisor digitados pelo usuario 
d2 = float(input("digite o seu divisor:"))
if(d2 == 0): # se o divisor for igual a 0 ele não é possivel fazer a divisão, senão ele faz a divisão
    print("Não é possivel dividir por 0")
else:
    i = d1 / d2
    print("O resultado da divisão é:", i)