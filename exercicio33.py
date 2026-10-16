i = int(input("Digite a idade: ")) # Lendo a idade e informando a situação dela nas eleições brasileiras
if i < 16: # Se a idade for menor que 16, a pessoa não pode votar.
    print("Você não pode votar.")
elif i >= 16 and i < 18: # Se a idade for maior ou igual a 16 e menor que 18, a pessoa pode votar com autorização.
    print("Voto facultativo.")
elif i >= 18 and i <= 70: # Se a idade for maior ou igual a 18 e menor ou igual a 70, a pessoa pode votar.
    print("Voto obrigatorio.")
else: # Se a idade for maior que 70, a pessoa pode votar.
    print("Voto facultativo.")