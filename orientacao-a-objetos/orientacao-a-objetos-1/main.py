from conta import Conta

conta = Conta(123, "titular", 100.0, 1000.0)


print("--------------------------")
print("[INFO] Limite atual: ", conta.limite)

print("[INFO] Alterando conta... (200.0)")
conta.limite = 200.0

print("[INFO] Limite atual: ", conta.limite)