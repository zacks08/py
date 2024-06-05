def calcular_fatorial(n):
    if n < 0 or n >= 16:
        return "Número fora do limite permitido (0 a 15)"
    else:
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
    print(f"O fatorial de {num} é: {resultado}")


n = int(input("\nQuantas pessoas? "))
idades = []
for i in range(n):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)


maior_dezoito = False
for idade in idades:
    if idade >= 18:
        maior_dezoito = True
        break

if maior_dezoito:
    print("Pelo menos uma pessoa tem 18 anos ou mais.")
else:
    print("Nenhuma pessoa tem 18 anos ou mais.")
#essa aq tbm viu savio foi o ca pra mim fazer essa desgraca aq