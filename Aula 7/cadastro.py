funcionarios = {}

n = int(input("Quantos funcionários deseja cadastrar? "))
for i in range(n):
    nome = input("Digite o nome do funcionário: ")
    idade = int(input("Digite a idade do funcionário: "))
    cargo = input("Digite o cargo do funcionário: ")
    funcionarios[nome] = {"idade": idade, "cargo": cargo}
    print(f"Funcionário {nome} cadastrado com sucesso!")


for nome, info in funcionarios.items():
    print(f"Nome: {nome}, Idade: {info['idade']}, Cargo: {info['cargo']}")

