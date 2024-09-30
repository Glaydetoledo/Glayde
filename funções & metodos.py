# Demostração de funções em listas...
print("eis os meus maiores sonhos...")
Sonhos = ["1. Me diverti na disaney",
          "2. Me banhar na praia de sepetiba",
          "3. Tirar as festas em Paris",
          "4. Fazer compras no Westshopping",
          "5. Ver as pirâmedes do Egito"]
for X in Sonhos:
    print(X)

print("Ops, não quero Sepetiba!")
del(Sonhos[1])
print("E nem Westshopping...")
del(Sonhos[3])

print("Conferindo os Sonhos...")
for X in Sonhos:
    print(X)