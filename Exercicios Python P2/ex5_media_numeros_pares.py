"""Exercício 5: lê uma lista de números e retorna a média dos números pares.
Função `media_pares` retorna None se não houver pares.
"""

def media_pares(lista):
    pares = [x for x in lista if x % 2 == 0]
    if not pares:
        return None
    return sum(pares) / len(pares)


def main():
    print("Exercício 5 - Média dos números pares de uma lista")
    entrada = input("Digite números inteiros separados por espaço: ")
    lista = [int(x) for x in entrada.split()] if entrada.strip() else []
    resultado = media_pares(lista)
    if resultado is None:
        print("Não há números pares na lista.")
    else:
        print(f"A média dos números pares é: {resultado}")


if __name__ == '__main__':
    main()
