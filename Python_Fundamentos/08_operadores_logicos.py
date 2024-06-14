# and :: V se todos forem V
# or :: V se ao menos um for V

saldo = 1000
saque = 250
limite = 200
conta_special = True

print(f"Saldo é maior ou igual ao Saque: {saldo >= saque}")
print(f"Saque é menor ou igual ao Limite: {saque <= limite}")

# Operador E (and) :: V e V = V / V e F = F / F e F = F
print(f"Saldo é maior ou igual ao Saque E Saque é menor ou igual ao Limite: {saldo >= saque and saque <= limite}")

# Operador OU (or) :: V e V = V / V e F = V / F or F = F
print(f"Saldo é maior ou igual ao Saque OU Saque é menor ou igual ao Limite: {saldo >= saque or saque <= limite}")

x = (saldo >= saque and saque <= limite) or (conta_special and saldo >= saque)
print(f"\nÉ possível sacar: {x}\n")