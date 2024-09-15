import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

class Agencia:
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print("O valor do caixa está ok. Caixa Atual: {}".format(locale.currency(self.caixa, grouping=True)))
        else:
            print("O valor do caixa esta ok. Caixa Atual: {}".format(locale.currency(self.caixa, grouping=True)))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print("Empréstimo não é possível. Dinheiro não disponível em caixa.")


    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


agencia1 = Agencia(31975081605, 1230123485, 4356)
agencia1.caixa = 1000000
agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(2500, 88571231002, 0.02)
print(agencia1.emprestimos)

agencia1.adicionar_cliente("Torezone", 11352600152, 15000)
print(agencia1.clientes)