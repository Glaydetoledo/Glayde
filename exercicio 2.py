#Demostração dia da semana
print("Digite o dia da semana:")
diadasemana = input()


match diadasemana:
     case "segunda":
         print("Boa semana")
     case "terça":
         print("vamos tomaer um cafe")
     case "quarta":
         print("dia de jogo")
     case "quinta":
         print("já e quase fim de semana")
     case "sexta":
         print("sextouu")
     case "sabado":
         print("Todo mundo espera alguma coisa de um sabado a noite")
     case "domingo":
         print("vamos tomar um chopp")
     case _:
         print("Acorda")
        
