#podia ter usado função mas fiz direto e me toquei depois, adoro função
salarios = {
    "Gerente": 8500.00,
    "Analista":5000.00,
    "Suporte":3000.00,
}
percentuais = {
    "Gerente": 0.12,
    "Analista": 0.12,
    "Suporte": 0.15,
}   

print("Salários atuais:")
for cargo, salario in salarios.items():
    print(f"{cargo}: R$ {salario:.2f}")


opcao = input("Decida o tipo de reajuste do salário dos funcionarios(mais/menos):").lower().strip()


for cargo, salario in salarios.items():
    percentual = percentuais[cargo]
    if opcao == "mais":
        novoSalario = salario * (1 + percentual)
        print(f"O novo salário do {cargo} é: R$ {novoSalario:.2f}")
    elif opcao == "menos":
        novoSalario = salario * (1 - percentual)
        print(f"O novo salário do {cargo} é: R$ {novoSalario:.2f}")
    else:
        print("Opção inválida.")
        novoSalario = salario
        
    salarios[cargo] = novoSalario 
