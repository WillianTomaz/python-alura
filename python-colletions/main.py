from conta_corrente import ContaCorrente


# Conta 1
print("-----------------------------------")
conta_do_will = ContaCorrente(15)
conta_do_will.deposita(500)
print(conta_do_will)

# Conta 2
print("-----------------------------------")
conta_da_ana = ContaCorrente(47685)
conta_da_ana.deposita(1000)
print(conta_da_ana)




# Lista com todas as Contas 
print("-----------------------------------")
contas = [conta_do_will, conta_da_ana]
for conta in contas:
  print(conta)