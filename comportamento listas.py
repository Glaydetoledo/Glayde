# Demostração de comportamento de listas...
print("Vou almoçar em um restaurante a quilo!")

Original = ["arroz", "feijão", "batata", "alface", "frango"]
print("eis, a minha comida:0, Original")
Derivada = Original[:]
print("Meu amigo irá comer também:", Derivada)

print("Vou alterar as opções sem ele ver...")
Original.remove("arroz")
Original.remove("feijão")
Original.remove("alface")
Original.append("picanha")
Original.append("linguiça")

print("Amiguinho, me mostre o que você vai comer?")
print("Claro! Dá uma conferida", Derivada)
