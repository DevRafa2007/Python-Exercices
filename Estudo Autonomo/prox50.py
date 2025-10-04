v = int(input("Digite um valor: "))
soma = 0
for i in range(v, v+51):
    soma += i
print(f"A soma de {v} com os próximos 50 números é: {soma}")