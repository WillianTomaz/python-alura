from conta_salario import ContaSalario


# Conta 1
print("-----------------------------------")
conta1 = ContaSalario(37)
print(f"Conta1 => {conta1}")
# Conta 2
conta2 = ContaSalario(37)
print(f"Conta2 => {conta2}")


print("-----------------------------------")
print(f"As contas são iguais? \n{conta1 == conta2}")

print("-----------------------------------")
print(f"São da mesma familia de classe (hierarquia)? \n{isinstance(conta1, ContaSalario)}")