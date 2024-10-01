# Demostração de acertos de uma prova...
Gabarito = ["B", "C", "A", "E", "D"]
Respostas = ["", "", "", "", ""]
Acertos = 0

for X in range(len(Gabarito)):
    print(f"Digite a resposta (X+1):")
    Respostas[X] = input()
    if Gabarito[X] == Respostas[X]:
        print("Acertou Mizeravél!")
        Acertos = Acertos + 1
    else:
        print("Errou, mane ")

print("Total de acertos:", Acertos)             

