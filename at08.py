soma = 0
quantidade = 5

for i in range(quantidade):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / quantidade

print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")
