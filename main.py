from ContasBanco import ContaCorrente, CartaoCredito

#Programa
conta_torezone = ContaCorrente("Torezone", "088.577.666-00", "1234", "456321")
conta_torezone.depositar(1000)
conta_torezone.consultar_saldo()

cartao_torezone = CartaoCredito("Torezone", conta_torezone)
print(cartao_torezone.conta_corrente.num_conta)

print(cartao_torezone.numero)

print(cartao_torezone.validade)

cartao_torezone.senha = "1245"
print(cartao_torezone.senha)

print(conta_torezone.__dict__)
print(cartao_torezone.__dict__)