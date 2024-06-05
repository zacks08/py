while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if senha != usuario:
        print("Usuário e senha válidos. Registro concluído.")
        break
    else:
        print("A senha não pode ser igual ao nome de usuário. Por favor, tente novamente.")

