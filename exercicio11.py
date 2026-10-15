n1=float(input("digite seu primeiro número :")) # Lê os dois números digitados pelo usuario 
n2=float(input("digite seu segundo número :"))
if(n1 > n2): # se o primeiro número for maior que o segundo ele é o maior
    print("O maior número é:", n1)
elif(n2 > n1):
    print("O maior número é:", n2)
else:
    print("Os números são iguais")