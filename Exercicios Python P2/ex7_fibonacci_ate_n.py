"""Exercício 7: imprime a sequência de Fibonacci até um valor inserido pelo usuário.
Função `fibonacci_ate` retorna a lista de Fibonacci até incluir valores <= n.
"""

def fibonacci_ate(limite):
    if limite < 0:
        return []
    seq = [0, 1]
    if limite == 0:
        return [0]
    while True:
        novo = seq[-1] + seq[-2]
        if novo > limite:
            break
        seq.append(novo)
    return seq


def main():
    print("Exercício 7 - Fibonacci até N")
    n = int(input("Digite o valor máximo para a sequência de Fibonacci: "))
    seq = fibonacci_ate(n)
    print("Sequência de Fibonacci:", seq)


if __name__ == '__main__':
    main()
