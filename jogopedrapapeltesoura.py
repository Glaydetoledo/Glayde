jogador1 = input("jogador 1: ")
jogador2 = input("jogador 2: ")

if jogador1 == jogador2:
    print("O resulta deu empate")
elif jogador1 == "tesoura" and jogador2 == "papel":
    print("jogador 1 venceu")
elif jogador1 == "papel" and jogador2 == "pedra":
    print("jogador 1 venceu") 
elif jogador1 == "pedra" and jogador2 == "tesoura":
    print("jogador 1 venceu")    
else:
    print("jogador 2 venceu")           