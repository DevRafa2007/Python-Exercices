def fibonacci(limite):
    if limite < 0:
        return []
    seq = [0, 1]
    if limite == 0:
        return [0]
    while True:
        novo = seq[-1] + seq[-2]
        if novo > limite:
            break
        seq.append(novo) #adiciona o novo na lista seq
    return seq
n = int(input("Digite o valor máximo para a sequência de Fibonacci: "))
seq = fibonacci(n)
print(f"Sequência de Fibonacci: {seq}")