while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("O nome deve ter mais que 3 caracteres. Tente novamente.")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break
        else:
            print("A idade deve estar entre 0 e 150 anos. Tente novamente.")
    except ValueError:
        print("Digite uma idade válida.")

while True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario > 0:
            break
        else:
            print("O salário deve ser maior que zero. Tente novamente.")
    except ValueError:
        print("Digite um valor numérico válido para o salário.")

while True:
    sexo = input("Digite seu sexo (f/m): ").lower()
    if sexo == 'f' or sexo == 'm':
        break
    else:
        print("Digite 'f' para feminino ou 'm' para masculino.")

while True:
    estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Digite 's' para solteiro, 'c' para casado")
      
