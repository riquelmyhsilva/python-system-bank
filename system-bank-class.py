def menu_login():
    menu = """\n
    ================ LOGIN ================
    [e]\tEntrar
    [c]\tCriar Conta

    [q]\tSair
    => """
    return input(menu)

def menu_principal(nome, numero, agencia):

    menu = f"""\n
    ================ MENU ================
    Nome: {nome}
    Numero da Conta: {numero}
    Agência: {agencia}

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato

    [q]\tSair da Conta
    => """
    return input(menu)

# classes

class Conta:

    def __init__(self, numero, agencia, cliente, limite = 500, limite_saques = 3,
                 saques_feitos = 0):
        self._saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self._extrato = ""
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_feitos = saques_feitos

    @property
    def saldo(self):
        return self._saldo

    @property
    def extrato(self):
        print("\n    =============== EXTRATO ===============")
        print("\tNão foram realizadas movimentações." if not self._extrato else self._extrato)
        print(f"\n\tSaldo:\t\tR$ {self._saldo:.2f}")
        print("    ========================================")
        return True

    def sacar(self, valor):

        if valor > self.saldo:
            print("    Você não tem saldo suficiente.")
            return False

        elif valor > self.limite:
            print("    Limite excedido.")
            return False

        elif self.saques_feitos == self.limite_saques:
            print("    Limite de saques diarios atingido.")
            return False
        
        else:
            self._saldo -= valor
            self._extrato += f"\tSaque:\t\t- R$ {valor:.2f}\n"
            self.saques_feitos += 1
            return True
    
    def depositar(self, valor):

        if valor < 0:
            print("Valor Inválido.")
            return False
        
        else:
            self._saldo += valor
            self._extrato += f"\tDeposito:\t+ R$ {valor:.2f}\n"
            return True

# funções

def criar_conta(contas,numero):

    cpf = input("Informe seu CPF: ")
    nome = input("Informe seu nome: ")

    contas[cpf] = Conta(numero = numero, agencia = "XYZ", cliente = nome)

    numero += 1

    return contas, numero

# função principal

def main():

    contas = {}
    numero = 0

    while True:

        opcao = menu_login()

        if opcao == 'e':

            cpf = input("    Informe seu CPF: ")
            if cpf in contas:

                while True:

                    opcao = menu_principal(nome= contas[cpf].cliente,
                                           numero= contas[cpf].numero,
                                            agencia= contas[cpf].agencia)

                    if opcao == 'd':
                        contas[cpf].depositar(valor = float(input("\n    Valor: ")))

                    elif opcao == 's':
                        pass
                        contas[cpf].sacar(valor = float(input("\n    Valor: ")))

                    elif opcao == 'e':
                        pass
                        contas[cpf].extrato

                    elif opcao == 'q':

                        break

                    else:
                        print("\n    Opção Inválida.")

            else:
                print("\n    Conta não encontrada")

        elif opcao == 'c':
            contas, numero = criar_conta(contas, numero)

        elif opcao == 'q':
            quit()

        else:
            print("\n    Opção Inválida.")

# inicializador

main()