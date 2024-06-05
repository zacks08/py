n = []
for i in range(5):
    while True:
        try:
            numero = float(input(f"Digite o número {i + 1}: "))
            n.append(numero)
            break
        except ValueError:
            print("Por favor, digite um número válido.")

if n: 
    maior_numero = max(n)
    print(f"O maior número digitado é: {maior_numero}")
else:
    print("Nenhum número válido foi inserido.")
