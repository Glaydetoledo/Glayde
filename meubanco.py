# Demostração  de uso de diferentes operadores...
print("Qual o saldo atual da sua conta bancária?")
print("Obs.: utilize o ponto para representar os centavos...")
Saldo = float(input())

if Saldo < 0:
    print("Putz! Você esta devendo o banco!")
elif Saldo == 0:
    print("Impossivel! Deve ter ai alguns centavos...")
elif Saldo < 1:
    print("Putz! Só miseros centavinhos na conta?") 
elif Saldo <= 9:
    print("Opa! Já da para comprar umas balinhas...")
elif Saldo >= 1000000:
    print("Eita, você tem mais de um milhão!")

if Saldo != 0:
    print("Ao menos, você esta movimentando a conta...")             
    