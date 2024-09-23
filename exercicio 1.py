#Demostração de filme e programa de tv...
print("Digite o número referente a nota da ao filme ou serie:")
Nome = input()
print("Avalie o filme")
Filme = int(input())

match Filme:
     case 1:
         print("1.Péssimo Digite o motivo que não gostou")
         input()
     case 2:
         print("2.Ruim porque vc achou ruim")
         input()
     case 3:
         print("3.Razoável o que te fez achar isso")
         input()
     case 4:
         print("Bom")
     case 5:
         print("Ótimo")
     case _:
         print("Você tem certeza que viu o filme")
        
