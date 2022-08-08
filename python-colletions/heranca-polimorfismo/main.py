from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca


# conta16 = ContaCorrente(16)
# conta16.deposita(1000)
# conta16.passa_o_mes()
# print(conta16)

# conta17 = ContaPoupanca(17)
# conta17.deposita(1000)
# conta17.passa_o_mes()
# print(conta17)


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

for conta in contas:
  conta.passa_o_mes() # duck typing
  print(conta)