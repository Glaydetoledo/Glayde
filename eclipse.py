# Eclipse Solar...
Hora = input("qual a hora da chegada? ")
Estado = input("Qual é  o estado (RJ/SP/MG/ES)? ")
Dia = input("O dia está claro (S/N)? ")  

if Hora == "15:25h" and Estado == "RJ" and Dia == "S":
    print("Eclipse Total")
elif Hora > "15:28h" and Hora > "15:38h":
    if Estado == "RJ" or Estado == "SP" or Estado == "MG" or Estado == "ES":  
        if Dia == "S":
            print("Eclipse Parcial") 

else:
    Print("Não deu para ver o eclipse")               
