def n_ate(n):
    if n < 0:
        return "Tente novamente com um número positivo"
    if not n % 2 == 0:
        x = [i for i in range(1, n + 1, 2)]
        return f"Os antecessores impares de {n} são {x}" 
    y = [i for i in range(0, n + 1, 2)]
    return f"Os antecessores pares de {n} são {y}" 

n = int(input("Digite um número inteiro não negativo: "))
print(n_ate(n))