frase = input("digite a frase para saber se é um palindromo: ")

final = len(frase) -1 
começo = 0

palindromo = True

while(começo < final):
    if frase[começo] != frase[final]:
        palindromo = False
    começo += 1
    final -= 1

if palindromo:
    print("É palindromo")
else:
    print("Não é um palindromo")