import time
def ts(a):
    time.sleep(a)
while True:
    print("Menu \n Escolhas:\n Opção 1 - Continuar\n Opção 2 - Sair")
    op = input("Digite sua escolha(1 ou 2): ")

    try:
        intop = int(op)
    except ValueError:
        print("Digite um número por favor!!")
        ts(1)
        continue

    if intop == 1:
        print("Usuário escolheu continuar")
        print("...")
        ts(1.5)
        continue
    elif intop == 2:
        print("Usuário escolheu sair")
        print("...")
        ts(1)
        break
    else:
        ts(1.5)
        print("Digite um número valido entre as opções!")