#Demostração de uso da moeda...
print("Digite o numero referente ao estado da moeda:")
print("1. Flor de cunho")
print("2. soberba")
print("3. Muito bem conservada")
print("4. Bem conservada")
print("5. outros estados")
Estado = int(input())

match Estado:
     case 1:
         print("Perfeita! Vou pagar R$1.000.000,00!")
     case 2:
         print("Quase perfeita! Ofereço R$250.000,00!")
     case 3:
         print("Que otimo! Posso dar uns R$100.000,00!")
     case 4:
         print("Que bom! Aceitaria R$30.000,00?")
     case 5:
         print("Desculpe, não aceito nesse estado.")
     case _:
         print("Opção não reconhecida")
        

  
