alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g' 'h' 'i' 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

vogais = []

for letra in alfabeto:
    if letra in ['a', 'e', 'i', 'o', 'u']:
        vogais.append(letra)

print("Vogais:", vogais)
