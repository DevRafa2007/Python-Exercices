# Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre:                                                                                                                                                
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.                                                                                          
# C) Se o valor 5 foi digitado e está ou não na lista.
lista= []
while True:
    c = int(input("Digite quantos numeros quiser(para sair digite 0 ou um negativo): "))
    if c <= 0:
        break
    else:
        lista.append(c)

lista.sort(reverse=True)

print("-=" * 30)
print(f"A sua lista tem {len(lista)} números")
print(f"A lista em ordem decrescente é: {lista}")
if 5 in lista:
    print("O 5 esta entre os valores da sua lista")