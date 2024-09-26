# Desmostração de diferentes operadores...
print("Times no campeonato brasileiro")
Times = input()
print("classificação do campeonato")
Classificacao = int (input("Digite a posição"))

if Classificacao == 1:
    print("Campeão")
elif Classificacao > 1 and Classificacao <= 6:
    print("Libertadores")
elif Classificacao > 7 and Classificacao <=12:
    print("Sul-americana")    
elif Classificacao >=  16:
    print("Rebaixado")     
else:
    print("Não dizer")       