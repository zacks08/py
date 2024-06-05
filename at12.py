def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

while True:
    num = int(input("Digite um número para calcular o fatorial (ou digite -1 para sair): "))
    
    if num == -1:
        print("Encerrando o programa.")
        break
    
    resultado = calcular_fatorial(num)
    print(f"{num}! = {resultado}")
