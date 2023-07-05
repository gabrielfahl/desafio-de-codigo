frase = input('Digite a frase para ser retornada sem caracteres repetidos: ')
frase_nova = ''

for c in frase:
    if c not in frase_nova:
        frase_nova += c

print(frase_nova)