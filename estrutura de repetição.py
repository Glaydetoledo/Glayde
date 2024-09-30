# Demostração de acesso as listas...

print("Vou montar a marmita com cinco alimentos!")
Marmita = ["feijão", "arroz", "legumes", "salada", "carne"]
print("Eis, a nossa recomendação:", Marmita)

Resposta = input("Quer montar uma marmita diferente (S/N)?")
if Resposta == "S":
    for X in range(len(Marmita)):
        print(f'Digite o  (X+1)o. item do cardapio:')
        Marmita[X] = input()
    print("A marmita montada foi:", Marmita)
    print("Os tr~es primeiros itens foram:", Marmita[0:3])
    print("O ultimo item da marmita foi:", Marmita[-1])
else:
    print("Ok, você decide...")
             