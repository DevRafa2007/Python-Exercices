import funcoes

print("Bem-vindo à loja!")
print("Aqui estão os produtos disponíveis:")
print("1. Notebook - (US$ 750.00)")
print("2. Smartphone - (US$ 250.00)")
produto = int(input("Digite o numero do produto que deseja comprar: "))

if produto == 1:
    valor_produto = funcoes.conversor(750.00)
elif produto == 2:
    valor_produto = funcoes.conversor(250.00)

print(f"O valor do produto em reais é: R$ {valor_produto:.2f}")

print("Frete disponível:")
print("1.Brasil - US$52.00")
print("2.Argentina - US$ 75.00")

frete = int(input("Digite o numero do país para onde deseja enviar o produto: "))
if frete == 1:
    valor_frete = funcoes.conversor(52.00)
elif frete == 2:
    valor_frete = funcoes.conversor(75.00)
print(f"O valor do frete em reais é: R$ {valor_frete:.2f}")
valor_total = funcoes.soma(valor_produto, valor_frete)
print(f"O valor total da compra é: R$ {valor_total:.2f}")