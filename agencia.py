import locale
from random import  randint
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
            print("Caixa abaixo do nível recomentado. Caixa Atual: {}".format(locale.currency(self.caixa, grouping=True)))
        else:
            print("O valor do caixa esta ok. Caixa Atual: {}".format(locale.currency(self.caixa, grouping=True)))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print("Empréstimo não é possível. Dinheiro não disponível em caixa.")


    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000

class AgengiaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 15000000


agencia1 = Agencia(31975081605, 1230123485, 4356)

agencia_virtual = AgenciaVirtual("www.agenciavirtua.com",112351500, 4533)
agencia_virtual.verificar_caixa()
print(agencia_virtual.site)

agencia_comum = AgengiaComum(32851530, 112351531000113)
agencia_comum.verificar_caixa()

agencia_premium = AgenciaPremium(33850350, 3331110000115)
agencia_premium.verificar_caixa()