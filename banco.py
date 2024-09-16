class Banco:
    def __init__(self):
        self.saldo = 0
        self.total_depositos = 0
        self.total_saques = 0
        self.extrato = []
        self.saques_realizados = 0
        self.limite_saques_diarios = 3
        self.limite_saque = 500

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.total_depositos += valor  
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print(f"R${valor:.2f} depositados com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if self.saques_realizados >= self.limite_saques_diarios:
            print("Limite de saques diários atingido.")
        elif valor > self.limite_saque:
            print(f"Valor excede o limite de R${self.limite_saque:.2f} por saque.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor <= 0:
            print("Valor de saque inválido.")
        else:
            self.saldo -= valor
            self.total_saques += valor  
            self.saques_realizados += 1
            self.extrato.append(f"Saque: -R${valor:.2f}")
            print(f"R${valor:.2f} sacados com sucesso!")

    def visualizar_extrato(self):
        print("\n----- Extrato -----")
        if not self.extrato:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.extrato:
                print(transacao)
        
        # Exibir o resumo dos depósitos, saques e saldo
        print(f"\nTotal depositado: R${self.total_depositos:.2f}")
        print(f"Total sacado: R${self.total_saques:.2f}")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"Saques diários realizados: {self.saques_realizados}/{self.limite_saques_diarios}")
        print("-------------------\n")

    def reiniciar_saques_diarios(self):
        """Simula o reinício diário dos saques (resetando o contador de saques)"""
        self.saques_realizados = 0
        print("Limite de saques diários reiniciado.\n")



banco = Banco()

while True:
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Visualizar Extrato")
    print("4 - Reiniciar Saques Diários")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        valor = float(input("Digite o valor para depósito: "))
        banco.depositar(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor para saque (Máximo R$500): "))
        banco.sacar(valor)
    elif opcao == '3':
        banco.visualizar_extrato()
    elif opcao == '4':
        banco.reiniciar_saques_diarios()
    elif opcao == '5':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
