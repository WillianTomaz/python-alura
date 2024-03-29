from conta_salario import ContaSalario


# Conta 1
print("-----------------------------------")
conta1 = ContaSalario(11)
conta1.deposita(500)
print(f"Conta1 => {conta1}")
# Conta 2
conta2 = ContaSalario(22)
conta2.deposita(500)
print(f"Conta2 => {conta2}")
# Conta 3
conta3 = ContaSalario(33)
conta3.deposita(500)
print(f"Conta3 => {conta3}")

print("-----------------------------------")
print(f"As contas são iguais? \n{conta1 == conta2}")

print("-----------------------------------")
print(f"São da mesma familia de classe (hierarquia)? \n{isinstance(conta1, ContaSalario)}")

print("-----------------------------------")
print(f"Conta1 é 'menor ou igual' que Conta3? \n{conta1 <= conta3}")

print("-----------------------------------")
contas = [conta1, conta2, conta3] 
for conta in sorted(contas):
  print(conta)