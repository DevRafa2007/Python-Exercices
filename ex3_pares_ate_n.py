"""Exercício 3: solicita um número e imprime todos os números pares de 0 até esse número.
Função `pares_ate` retorna a lista de pares para ser testada.
"""

def pares_ate(n):
    if n < 0:
        return []
    return [i for i in range(0, n + 1) if i % 2 == 0]


def main():
    print("Exercício 3 - Pares de 0 até N")
    n = int(input("Digite um número inteiro não-negativo: "))
    resultado = pares_ate(n)
    print("Números pares:", resultado)


if __name__ == '__main__':
    main()
