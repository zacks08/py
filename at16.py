
def eh_primo(n):
    if n<= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro: "))

numeros_primos = [num for num in range(2, numero + 1) if eh_primo(num)]

print(f"Números primos entre 1 e {numero}:")
print(numeros_primos)
