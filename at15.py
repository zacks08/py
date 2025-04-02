temperaturas = []



while True:

    temperatura = input("Digite uma temperatura (ou 'sair' para encerrar): ")
    
    if temperatura.lower() == 'sair':
        break
    
    try:
        temperatura = float(temperatura)
        temperaturas.append(temperatura)
    except ValueError:
        print("Por favor, digite um número válido.")

if temperaturas:

    menor_temperatura = min(temperaturas)
    maior_temperatura = max(temperaturas)
    media_temperaturas = sum(temperaturas) / len(temperaturas)


    print(f"A menor temperatura informada é: {menor_temperatura}")
    print(f"A maior temperatura informada é: {maior_temperatura}")
    print(f"A média das temperaturas informadas é: {media_temperaturas:.2f}")
else:
    print("Nenhuma temperatura foi inserida.")
