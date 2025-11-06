import os

def limpar_terminal():
    # Se for Windows, usa 'cls', senão usa 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')


veiculos = {}
clientes = {}
colaboradores = {}

while True:
    print("="*30)
    print("***LOCADORA***")
    print("Bem Vindo ao Sistema!")
    print("="*30)
    print("O que gostaria de fazer?")
    print("***OPÇÕES***\n1 - Cadastrar um veículo\n2 - Cadastrar um cliente\n3 - Cadastrar um colaborador\n4 - Fazer uma locação")
    op = input("Digite sua opção: ")
    print("="*30)
    if op == "1":
        codigo = input("Digite o código do veículo: ")
        placa = input("Digite a placa do veículo: ")
        marca = input("Digite a marca do veículo: ")
        modelo = input("Digite o modelo do veículo: ")
        quantidade = int(input("Digite a quantidade de veículos disponíveis: "))
        valor_aluguel = float(input("Digite o valor do aluguel por dia: "))
        veiculos[codigo] = {
            "placa": placa,
            "marca": marca,
            "modelo": modelo,
            "quantidade": quantidade,
            "valor_aluguel": valor_aluguel
        }
        
    elif op == "2":
        codigo = input("Digite o código do cliente: ")
        nome = input("Digite o nome do cliente: ")
        clientes[codigo] = {
            "nome": nome
        }
        
    elif op == "3":
        codigo = input("Digite o código do colaborador: ")
        nome = input("Digite o nome do colaborador: ")
        colaboradores[codigo]={
            "nome": nome
        }
        
    elif op == "4":
        print("Fazendo uma locação...")
        print("Clientes disponíveis:")
        for codigo, nome in clientes.items():
            print(f"Código: {codigo}, Nome: {nome['nome']}")
        print("="*30)
        codigo_cliente = input("Digite o código do cliente: ")
        if codigo_cliente not in clientes:
            print("Cliente não cadastrado!")
            continue
        print("Colaboradores disponíveis:")
        for codigo, nome in colaboradores.items():
            print(f"Código: {codigo}, Nome: {nome['nome']}")
        print("="*30)
        codigo_colaborador = input("Digite o código do colaborador: ")
        if codigo_colaborador not in colaboradores:
            print("Colaborador não cadastrado!")
            continue
        print("Veículos disponíveis:")
        for codigo, veiculo in veiculos.items():
            if veiculo["quantidade"] > 0:
                print(f"Código: {codigo}, Marca: {veiculo['marca']}, Modelo: {veiculo['modelo']}, Valor aluguel por dia: {veiculo['valor_aluguel']}")
        print("="*30)
        codigo_veiculo = input("Digite o código do veículo que deseja alugar: ")
        if codigo_veiculo not in veiculos or veiculos[codigo_veiculo]["quantidade"] <= 0:
            print("Veículo não disponível!")
            continue
        dias_locacao = int(input("Digite um número de dias para locação: "))
        valor_unitario = veiculos[codigo_veiculo]["valor_aluguel"]
        valor_total_aluguel = valor_unitario * dias_locacao
        valor_seguro = valor_total_aluguel * 0.25
        desconto = 0
        if dias_locacao > 30:
            desconto = 0.20
        elif dias_locacao > 15:
            desconto = 0.10
        elif dias_locacao > 5:
            desconto = 0.05
        valor_total_locacao = valor_total_aluguel + valor_seguro
        valor_total_com_desconto = valor_total_locacao * (1 - desconto)
        veiculos[codigo_veiculo]["quantidade"] -= 1
        print("Locação concluída! Comprovante:")
        print(f"Cliente: {clientes[codigo_cliente]['nome']}")
        print(f"Colaborador: {colaboradores[codigo_colaborador]['nome']}")
        print(f"Veículo: {veiculos[codigo_veiculo]['marca']} {veiculos[codigo_veiculo]['modelo']}")
        print(f"Valor unitário do aluguel: R$ {valor_unitario:.2f}")
        print(f"Valor total do aluguel: R$ {valor_total_aluguel:.2f}")
        print(f"Valor do seguro: R$ {valor_seguro:.2f}")
        print(f"Valor total da locação: R$ {valor_total_locacao:.2f}")
        if desconto > 0:
            print(f"Valor total da locação com desconto: R$ {valor_total_com_desconto:.2f}")    
    else:
        print("Opção inválida!")
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != "s":
        break
    else:
        limpar_terminal()
        print("AÇÃO REALIZADA COM SUCESSO!")