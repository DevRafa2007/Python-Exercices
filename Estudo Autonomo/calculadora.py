def calculadora(op):
    if op == "soma":
        def soma(a, b):
            resultado = a+b
            return resultado
        return soma
    elif op == "subitracao" or op == "subtração":
        def sub(a,b):
            resultado = a - b
            return resultado
        return sub
    elif op == "divisao" or op == "divisão":
        def div(a, b):
            resultado = a/b
            return resultado
        return div
    elif op == "multiplicacao"  or op == "multiplicação":
        def mul(a, b):
            resultado = a*b
            return resultado
        return mul
    else:
        return None
    
op = input("Digite a operação que deseja fazer (soma, subtração, divisão ou multiplicação): ").strip().lower()
a = int(input("Digite o primeiro numero que fara parte da operação: "))
b = int(input("Digite o segundo numero que fara parte da operação: "))
resultado = calculadora(op)
if resultado:
    print(f"O resultado da {op} entre {a} e {b} é: {resultado(a,b)}")