class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf  # Apenas números
        self.endereco = endereco

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data_nascimento}, Endereço: {self.endereco}"


class Conta:
    numero_conta_sequencial = 1 

    def __init__(self, usuario):
        self.agencia = "0001"  # Agência fixa
        self.numero_conta = Conta.numero_conta_sequencial
        Conta.numero_conta_sequencial += 1 
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0

    def __str__(self):
        return f"Agência: {self.agencia}, Conta: {self.numero_conta}, Usuário: {self.usuario.nome}"

    def depositar(self, /, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, *, valor):
        if self.numero_saques >= 3:
            print("Erro: Limite de saques diários atingido.")
            return self.saldo, self.extrato

        if valor > 500:
            print(f"Erro: O valor máximo por saque é de R$ 500,00.")
            return self.saldo, self.extrato

        if valor > self.saldo:
            print("Erro: Saldo insuficiente.")
            return self.saldo, self.extrato

        self.saldo -= valor
        self.numero_saques += 1
        self.extrato += f"Saque: R$ {valor:.2f}\n"
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        return self.saldo, self.extrato

    def exibir_extrato(self, /, *, extrato):
        print("\nExtrato Bancário:")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")

def verificar_cpf_existente(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return True
    return False


def cadastrar_usuario(nome, data_nascimento, cpf, endereco, usuarios):
    cpf_formatado = formatar_cpf(cpf)

    if verificar_cpf_existente(cpf_formatado, usuarios):
        print("Erro: Já existe um usuário com esse CPF.")
        return None

    novo_usuario = Usuario(nome, data_nascimento, cpf_formatado, endereco)
    usuarios.append(novo_usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")
    return novo_usuario


def buscar_usuario_por_cpf(cpf, usuarios):
    cpf_formatado = formatar_cpf(cpf)
    for usuario in usuarios:
        if usuario.cpf == cpf_formatado:
            return usuario
    print(f"Usuário com CPF {cpf_formatado} não encontrado.")
    return None


def criar_conta_por_cpf(cpf, usuarios, contas):
    usuario = buscar_usuario_por_cpf(cpf, usuarios)
    if usuario:
        nova_conta = Conta(usuario)
        contas.append(nova_conta)
        print(f"Conta {nova_conta.numero_conta} criada para o usuário {usuario.nome}.")
        return nova_conta
    return None


def menu(usuarios, contas):
    while True:
        print("\n=== Menu do Banco ===")
        print("1. Cadastrar Usuário")
        print("2. Criar Conta")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Exibir Extrato")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
            cpf = input("CPF: ")
            endereco = input("Endereço (logradouro, nro ; bairro - cidade/sigla estado): ")
            cadastrar_usuario(nome, data_nascimento, cpf, endereco, usuarios)

        elif opcao == "2":
            cpf = input("Informe o CPF do usuário para criar a conta: ")
            criar_conta_por_cpf(cpf, usuarios, contas)

        elif opcao == "3":
            cpf = input("Informe o CPF do usuário: ")
            conta = buscar_usuario_por_cpf(cpf, usuarios)
            if conta:
                valor = float(input("Valor do depósito: R$ "))
                conta.depositar(valor)

        elif opcao == "4":
            cpf = input("Informe o CPF do usuário: ")
            conta = buscar_usuario_por_cpf(cpf, usuarios)
            if conta:
                valor = float(input("Valor do saque: R$ "))
                conta.sacar(valor=valor)

        elif opcao == "5":
            cpf = input("Informe o CPF do usuário: ")
            conta = buscar_usuario_por_cpf(cpf, usuarios)
            if conta:
                conta.exibir_extrato(extrato=conta.extrato)

        elif opcao == "6":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


usuarios = []
contas = []

menu(usuarios, contas)
