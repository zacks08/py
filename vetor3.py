alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g' ]

vogais = []

for letra in alfabeto:
    if letra in ['a', 'e', 'i', 'o', 'u']:
        vogais.append(letra)

print("Vogais:", vogais)
