import csv

class Aluno:
    def __init__(self, nascimento, nome, apelido, ocorrencias):
        self.__nascimento = nascimento
        self.__nome = nome
        self.__apelido = apelido
        self.__ocorrencias = ocorrencias

    @property
    def nascimento(self):
        return self.__nascimento
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def apelido(self):
        return self.__apelido
    
    @property
    def ocorrencias(self):
        return self.__ocorrencias

class Escola:
    def __init__(self):
        self.__alunos = self.carregar_alunos()
        self.__senha_acesso = "1234"

    def carregar_alunos(self):
        alunos = []
        try:
            with open('alunos.csv', newline='', encoding='utf-8') as arquivo_csv:
                leitor_csv = csv.reader(arquivo_csv)
                next(leitor_csv)  # Ignorar cabeçalho
                for linha in leitor_csv:
                    nascimento, nome, apelido, ocorrencias = linha
                    alunos.append(Aluno(int(nascimento), nome, apelido, int(ocorrencias)))
        except FileNotFoundError:
            print("Arquivo de alunos não encontrado. Iniciando com lista vazia.")
        return alunos

    def salvar_alunos(self):
        with open('alunos.csv', 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(['Nascimento', 'Nome', 'Apelido', 'Ocorrências'])
            for aluno in self.__alunos:
                escritor_csv.writerow([aluno.nascimento, aluno.nome, aluno.apelido, aluno.ocorrencias])

    def editar_aluno(self, indice):
        if 0 <= indice < len(self.__alunos):
            aluno = self.__alunos[indice]
            nome = input("Novo nome: ")
            apelido = input("Novo apelido: ")
            nascimento = int(input("Nova data de nascimento(apenas numeros juntos sem separação): "))
            ocorrencias = int(input("Novas ocorrências: "))
            aluno._Aluno__nome = nome
            aluno._Aluno__apelido = apelido
            aluno._Aluno__nascimento = nascimento
            aluno._Aluno__ocorrencias = ocorrencias
            print("Aluno editado com sucesso!")
        else:
            print("Índice inválido!")

    def adicionar_aluno(self):
        nome = input("Nome: ")
        apelido = input("Apelido: ")
        nascimento = int(input("Nascimento (Apenas números ): "))
        ocorrencias = int(input("Ocorrências: "))
        aluno = Aluno(nascimento, nome, apelido, ocorrencias)
        self.__alunos.append(aluno)
        print("Aluno adicionado com sucesso!")

    def excluir_aluno(self, indice):
        if 0 <= indice < len(self.__alunos):
            del self.__alunos[indice]
            print("Aluno excluído com sucesso!")
        else:
            print("Índice inválido!")

    def listar_alunos(self):
        print("Lista de Alunos:")
        for i, aluno in enumerate(self.__alunos):
            print(f"{i+1}. Nome: {aluno.nome}, Apelido: {aluno.apelido}, nascimento: {aluno.nascimento}, Ocorrências: {aluno.ocorrencias}")

    def autenticar(self, senha):
        return senha == self.__senha_acesso

    def menu(self):
        print("1. Listar alunos")
        print("2. Editar aluno")
        print("3. Adicionar aluno")
        print("4. Excluir aluno")
        opcao = input("Escolha uma opção: ")
        return opcao

    def executar_opcao(self, opcao):
        if opcao == '1':
            self.listar_alunos()
        elif opcao == '2':
            indice = int(input("Digite o índice do aluno que deseja editar: ")) - 1
            self.editar_aluno(indice)
        elif opcao == '3':
            self.adicionar_aluno()
        elif opcao == '4':
            indice = int(input("Digite o índice do aluno que deseja excluir: ")) - 1
            self.excluir_aluno(indice)
        else:
            print("Opção inválida.")

    def run(self):
        while True:
            senha = input("Digite a senha de acesso: ")
            if self.autenticar(senha):
                break
            else:
                print("Senha incorreta. Tente novamente.")
        while True:
            opcao = self.menu()
            self.executar_opcao(opcao)
            if input("Deseja sair? (s/n): ").lower() == 's':
                self.salvar_alunos()
                print("Dados dos alunos salvos no arquivo alunos.csv")
                break

if __name__ == "__main__":
    escola = Escola()
    escola.run()
