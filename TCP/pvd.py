import os
def limpar_terminal():
    # Se for Windows, usa 'cls', senão usa 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')
produtos = {}
clientes = {}
vendedores = {}

while True:
    print("="*30)
    print("***PVD***")
    print("Bem Vindo ao Sistema!")
    print("="*30)
    print("O que gostaria de fazer?")
    print("***OPÇÕES***\n1 - Cadastrar um produto\n2 - Cadastrar um cliente\n3 - Cadastrar um vendedor\n4 - Fazer uma venda")
    op = input("Digite sua opção: ")
    print("="*30)
    if op == "1":
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        valor = float(input("Digite o valor do produto: "))
        estoque = int(input("Digite a quantidade em estoque: "))
        produtos[codigo] = {
            "nome": nome,
            "valor": valor,
            "estoque": estoque
        }
        
    elif op == "2":
        codigo = input("Digite o código do cliente: ")
        nome = input("Digite o nome do cliente: ")
        clientes[codigo] = {
            "nome": nome
        }
        
    elif op == "3":
        codigo = input("Digite o código do vendedor: ")
        nome = input("Digite o nome do vendedor: ")
        vendedores[codigo] = {
            "nome": nome
        }

    elif op == "4":
        print("Fazendo uma venda...")
        print("Clientes disponíveis:")
        for codigo, nome in clientes.items():
            print(f"Código: {codigo}, Nome: {nome['nome']}")
        print("="*30)
        codigo_cliente = input("Digite o código do cliente: ")
        if codigo_cliente not in clientes:
            print("Cliente não cadastrado!")
            continue
        print("Vendedores disponíveis:")
        for codigo, nome in vendedores.items():
            print(f"Código: {codigo}, Nome: {nome['nome']}")
        print("="*30)
        codigo_vendedor = input("Digite o código do vendedor: ")
        if codigo_vendedor not in vendedores:
            print("Vendedor não cadastrado!")
            continue
        venda_produtos = []
        while True:
            print("Produtos disponíveis:")
            for codigo, produto in produtos.items():
                if produto["estoque"] > 0:
                    print(f"Código: {codigo}, Nome: {produto['nome']}, Valor: {produto['valor']}, Estoque: {produto['estoque']}")
            print("="*30)
            codigo_produto = input("Digite o código do produto que deseja comprar (ou 'fim' para finalizar): ")
            if codigo_produto.lower() == 'fim':
                break
            if codigo_produto not in produtos or produtos[codigo_produto]["estoque"] <= 0:
                print("Produto não disponível!")
                continue
            quantidade = int(input("Digite a quantidade que deseja comprar: "))
            if quantidade > produtos[codigo_produto]["estoque"]:
                print("Quantidade indisponível em estoque!")
                continue
            venda_produtos.append((codigo_produto, quantidade))
            produtos[codigo_produto]["estoque"] -= quantidade
        if not venda_produtos:
            print("Nenhum produto foi comprado!")
            continue
        total_venda = sum(produtos[codigo]["valor"] * quantidade for codigo, quantidade in venda_produtos)
        imposto = total_venda * 0.25
        comissao = total_venda * 0.05
        print("Recibo da Venda:")
        print(f"Cliente: {clientes[codigo_cliente]['nome']}")
        print(f"Vendedor: {vendedores[codigo_vendedor]['nome']}")
        for codigo, quantidade in venda_produtos:
            produto = produtos[codigo]
            print(f"Produto: {produto['nome']}, Quantidade: {quantidade}, Valor Unitário: {produto['valor']}, Subtotal: {produto['valor'] * quantidade}")
        print(f"Total da Venda: {total_venda}")
        print(f"Imposto (25%): {imposto}")
        print(f"Comissão do Vendedor (5%): {comissao}")
    else:
        print("Opção inválida!")
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != "s":
        break
