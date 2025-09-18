def aumento(salario):
    return round(salario * 1.10, 2)

salarios = [1000, 2000, 3000, 4000, 5000]
nSalarios = list(map(aumento, salarios))

print(f"Salarios antigos: {salarios}")
print(f"Novos salarios: {nSalarios}")