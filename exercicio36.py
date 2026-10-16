jogador1 = input("Jogador 1, digite sua jogada (pedra, papel ou tesoura): ") #lendo as jogadas
jogador2 = input("Jogador 2, digite sua jogada (pedra, papel ou tesoura): ")

if jogador1 not in ["pedra", "papel", "tesoura"] or jogador2 not in ["pedra", "papel", "tesoura"]: # se a jogada do jogador 1 ou do jogador 2 não estiver entre pedra, papel ou tesoura, ele é uma jogada inválida.
    print("Jogada inválida")
elif jogador1 == jogador2: # se a jogada do jogador 1 for igual a jogada do jogador 2, ele é um empate.
    print("Empate")
elif (jogador1 == "pedra" and jogador2 == "tesoura") or (jogador1 == "tesoura" and jogador2 == "papel") or (jogador1 == "papel" and jogador2 == "pedra"): # se a jogada do jogador 1 for pedra e a jogada do jogador 2 for tesoura, ou se a jogada do jogador 1 for tesoura e a jogada do jogador 2 for papel, ou se a jogada do jogador 1 for papel e a jogada do jogador 2 for pedra, ele é o vencedor.
    print("Jogador 1 venceu")
else:
    print("Jogador 2 venceu")