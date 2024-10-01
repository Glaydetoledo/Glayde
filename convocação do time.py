# Demostrativo de convocação de time...
Jogadores = []
Numeros = []

for X in range(0, 11):
    Nome = input("Digite o nome do jagador:")
    Jogadores.append(Nome)
    Camisa = input("Digite o numero da camisa:")
    Numeros.append(Camisa)

print("Lista dos jogadores cadastrados:")
for X in range(0, 11):
    print(f"{Numeros[Y]}, {Jogadores[Y]}")    

    Troca = input("Você quer fazer substituições S/N?")
    if Troca == "S":
        for X in range(0, 3):
            Nome = input("Digite o nome do jogador substituido: ")
            Camisa = input("digite o seu respctivo numero: ")
            Jogadores.remove(Nome)
            Numeros.remove(Camisa)
            Nome = input("Digite o nome do jogador Substituido: ")
            Camisa = input("Digite o seu respectivo numero: ")
            Jogadores.append(Nome)
            Numeros.append(Camisa) 

        print("lista dos jogadores atualizada:")
        for Y in range(0, 11):
            print(f"{Numeros[Y]}. {Jogadores[Y]}")
