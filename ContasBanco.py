from datetime import  datetime
import pytz
from random import  randint



class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone("Brazil/East")
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime("%d/%m/%y %H:%M:%S")

    def __init__(self, nome, cpf,  agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []
        self.cartoes = []


    def consultar_saldo(self):
        print(f"Seu saldo atual é de R${self._saldo:,.2f}")

    def depositar(self, valor):
        self._saldo += valor
        self.transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo -valor  < self._limite_conta():
            print("Você tem saldo insuficiente para sacar o valor desejado")
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self.transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_chequespecial(self):
        print("Seu limite de cheque Especial é de R${:,.2f}".format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print("Histórico de transaões:")
        print("Valor, Saldo, Data e Hora")
        for transacao in self.transacoes:
            print(transacao)

class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone("Brazil/East")
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f"{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}"
        self.cod_seguranca = f"{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}"
        self.limite = 1000
        self._senha = "020658"
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha inválidada")


