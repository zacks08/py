populacao_A = 80000
taxa_crescimento_A = 0.03

populacao_B = 200000
taxa_crescimento_B = 0.015

anos = 0
while populacao_A <= populacao_B:
    populacao_A *= (1 + taxa_crescimento_A)
    populacao_B *= (1 + taxa_crescimento_B)
    anos += 1

print(f"Serão necessários {anos} anos para que a população do pais 'A' ultrapasse ou seja igual à população do país 'B'.")
