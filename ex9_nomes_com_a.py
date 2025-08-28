"""Exercício 9: lê uma lista de nomes e retorna apenas os que começam com 'A'.
Função `filtrar_com_a` preserva capitalização e espaços externos são removidos.
"""

def filtrar_com_a(nomes):
    resultado = [nome for nome in nomes if nome.strip() and nome.strip()[0].upper() == 'A']
    return resultado


def main():
    print("Exercício 9 - Nomes que começam com 'A'")
    entrada = input("Digite nomes separados por vírgula: ")
    nomes = [x.strip() for x in entrada.split(',')] if entrada.strip() else []
    filtrados = filtrar_com_a(nomes)
    print("Nomes que começam com 'A':", filtrados)


if __name__ == '__main__':
    main()
