X = int(input("Digite o valor de x:"))
Y = int(input("Digitr o valor de y"))
Z = int(input("Digite o valor de z"))

if X < Y and Y < Z:
    print("Em ordem crescente")
elif X > Y and Y > Z:
    print("Em ordem descrescente")
else:    
    print("Todos misturados")        