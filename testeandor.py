# Demostração de operadores logicos em condicionais...
print("O que você vai fazer amanhã de manhã?")
print("dormir / estudar /planejar")
Manha = input()
print("O que você vai fazer amanhã  de tarde?")
print("jogar / treinar / trabalhar")
Tarde = input()

if not Manha or not Tarde:
    print("Você precisa dizer o que vai fazer!")
else:
    if Manha == "dormir" or Tarde == "jogar":
        print("Você esta desperdiando o seu dia!")
    elif Manha == "estudar" or Tarde == "treinar":
        print("Que bom! você irá se aperfeiçoar!")
    elif Manha == "planejar" and Tarde == "trabalhar":
        print("Para trabalhar melhor, devo planejar!")
    else:
        print("Não combinamos essas ações...")

print("Tenha um bom dia!")                    