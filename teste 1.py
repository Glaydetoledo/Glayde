#Demostração de uso da moeda...
print("Digite o numero referente ao estado da moeda:")
print("a. Flor de cunho")
print("b. soberba")
print("c. Muito bem conservada")
print("d. Bem conservada")
print("e. outros estados")
Estado = input()

match Estado:
     case "a":
         print("Perfeita! Vou pagar R$1.000.000,00!")
     case "b":
         print("Quase perfeita! Ofereço R$250.000,00!")
     case "c":
         print("Que otimo! Posso dar uns R$100.000,00!")
     case "d":
         print("Que bom! Aceitaria R$30.000,00?")
     case "e":
         print("Desculpe, não aceito nesse estado.")
     case _:
         print("Opção não reconhecida")
        

