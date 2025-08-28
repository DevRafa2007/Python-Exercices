"""Exercício 8: determina se um número é primo ou não.
Função `eh_primo` faz checagem eficiente até sqrt(n).
"""

import math


def eh_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    raiz = int(math.sqrt(n))
    i = 3
    while i <= raiz:
        if n % i == 0:
            return False
        i += 2
    return True


def main():
    print("Exercício 8 - Número primo")
    n = int(input("Digite um número inteiro: "))
    if eh_primo(n):
        print(f"{n} é primo.")
    else:
        print(f"{n} não é primo.")


if __name__ == '__main__':
    main()
