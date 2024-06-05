n_pares = 0
n_impares = 0
quantidade_n = 10

for i in range(quantidade_n):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    if numero % 2 == 0:
        n_pares += 1
    else:
        n_impares += 1

print(f"Quantidade de números pares: {n_pares}")
print(f"Quantidade de números ímpares: {n_impares}")
