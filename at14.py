def classificar_faixa_etaria(media_idades):
    if media_idades <= 25:
        return "jovem"
    elif media_idades <= 60:
        return "adulta"
    else:
        return "idosa"


n = int(input("Digite o número de pessoas: "))

idades = []

for i in range(n):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    idades.append(idade)


media_idades = sum(idades) / n


faixaetaria = classificar_faixa_etaria(media_idades)

print(f"A média de idade da turma é: {media_idades:.2f}")
print(f"A turma é classificada como {faixaetaria}.")
