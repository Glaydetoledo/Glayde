# conversor de temperatura...
Grau = int(input("Digite a temperatura: "))
Sistema = input("Celssius / Kelvin /Fahrenheit? ")

if Sistema == "Celsius":
   Kelvin = Grau + 273.15
   Fahrenheit =  (9/5 * Grau) - 32
   print("O valor em Celsius:" , Grau)
   print("A conversão para Kelvin: ", Kelvin)
   print("A conversão para Fahrenheit: ", Fahrenheit)
elif Sistema == "Kelvin":
    Celsius = Grau - 273.15
    Fahrenheit = 1.8 - (Grau - 273.15) + 32
    print("O valor em Kelvin:", Grau)
    print("A conversão para Celsius: ", Celsius)
    print("A conversão para Fahrenheit: ", Fahrenheit)   
elif Sistema == "Fahrenheit":
    Celsius = 5/9 * (Grau - 32)
    Kelvin = (Grau -32) / 1.8 + 273.15
    print("O valor em Fahrenheit:", Grau)
    print("A conversão para Celsius: ", Celsius)
    print("A conversão para Kelvin: ", Kelvin) 
else:
    print("Sistema inexistente...")        