
# Lê a idade do comprador
idade = int(input("Digite a idade: "))

# Pergunta se o comprador é estudante
estudante = input("É estudante? (s/n): ").lower()

# Verifica se o ingresso é gratuito
if idade < 6:
    print("Gratuito — R$ 0.0")

else:
    # Verifica se tem direito à meia-entrada
    if idade <= 17 or idade >= 60 or estudante == "s":
        tipo = "Meia-entrada"
        valor = 20.0
    else:
        # Se não tiver direito à meia, paga inteira
        tipo = "Inteira"
        valor = 40.0

    # Lê a forma de pagamento
    pagamento = int(input("Pagamento (1-PIX, 2-Débito, 3-Crédito): "))

    # PIX: aplica 5% de desconto
    if pagamento == 1:
        forma = "PIX"
        valor = valor * 0.95

    # Débito: mantém o valor original
    elif pagamento == 2:
        forma = "Débito"

    # Crédito: aplica 5% de acréscimo
    elif pagamento == 3:
        forma = "Crédito"
        valor = valor * 1.05

    # Se o código for inválido, mostra uma mensagem
    else:
        print("Forma de pagamento inválida")
        exit()

    # Mostra o resumo da compra
    print(f"{tipo} — {forma} — R$ {valor:.1f}")
