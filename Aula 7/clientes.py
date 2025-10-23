fem = {}
masc = {}
print("Cadastro de Clientes")
while True:
    nome = input("Informe o Nome ou sair: ")
    if nome == "sair":
        break
    sexo = input("Sexo (M/F): ").upper()
    idade = int(input("Idade: "))
    if sexo == "F":
        fem[nome] = [idade]
    elif sexo == "M":
        masc[nome] = [idade]
    else:
        print("Sexo inválido. Tente novamente.")
        continue
print("\nClientes Femininos:")
for nome, idade in fem.items():
    print(f"Nome: {nome}, Idade: {idade[0]}")
print("\nClientes Masculinos:")
for nome, idade in masc.items():
    print(f"Nome: {nome}, Idade: {idade[0]}")