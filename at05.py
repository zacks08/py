def calcular_anos(populacao_A, taxa_crescimento_A, populacao_B, taxa_crescimento_B):
    anos = 0
    while populacao_A <= populacao_B:
        populacao_A *= (1 + taxa_crescimento_A)
        populacao_B *= (1 + taxa_crescimento_B)
        anos += 1
    return anos

while True:
    try:
        populacao_A = int(input("Informe a população do país A: "))
        taxa_crescimento_A = float(input("Informe a taxa de crescimento do país A (em decimal): "))
        populacao_B = int(input("Informe a população do país B: "))
        taxa_crescimento_B = float(input("Informe a taxa de crescimento do país B (em decimal): "))

        if populacao_A < 0 or populacao_B < 0 or taxa_crescimento_A < 0 or taxa_crescimento_B < 0:
            print("Por favor, insira valores não negativos para populações e taxas de crescimento.")
        else:
            anos_necessarios = calcular_anos(populacao_A, taxa_crescimento_A, populacao_B, taxa_crescimento_B)
            print(f"Serão necessários {anos_necessarios} anos para que a população do país A ultrapasse ou seja igual à população do país B.")
            break
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

print("Números de 1 a 20:")
for i in range(1, 21):
    print(i)
