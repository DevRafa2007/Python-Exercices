"""Exercício 4: lê uma lista de números e exibe o maior e o menor valor da lista.
Função `maior_e_menor` retorna uma tupla (maior, menor).
"""

def maior_e_menor(lista):
    if not lista:
        raise ValueError("A lista não pode ser vazia")
    maior = max(lista)
    menor = min(lista)
    return maior, menor


def main():
    print("Exercício 4 - Maior e menor de uma lista")
    entrada = input("Digite números separados por espaço: ")
    lista = [float(x) for x in entrada.split()] if entrada.strip() else []
    if not lista:
        print("Lista vazia. Nada a mostrar.")
        return
    maior, menor = maior_e_menor(lista)
    print(f"Maior: {maior}, Menor: {menor}")


if __name__ == '__main__':
    main()
