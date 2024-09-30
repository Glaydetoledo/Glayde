# Demostração de métodos em listas...
INSS = ["Maria", "Manoel", "José", "Isabela"]
print("Eis, a fila do inss:", INSS)

Novo =  input("Insira mais uma pessoa: ")
INSS.append(Novo)
print("Conferindo a nova lista:", INSS)

print("Vou tirar a última pessoa desta lista...")
Especial = INSS.pop()

print("Agora vou coloca-la na frente de todos!")
INSS.insert(0, Especial)
print("conferindo a lista: ", INSS)

print("Maria não gostou e reclamou...")
INSS.remove("Maria")
print("E agora, ela saiu 'Pê da vida'", INSS)

print("Para não ter mais reclamação, vamos atender...")
INSS.sort()
print("... em ordem alfabetica:", INSS)

print("Onde está  nova pessoa chamada", Especial, "?")
print("ela agora ficou na posição", INSS.index(Especial)+1, "!")