import time
import random
n = random.randint(1, 20)
tentativas = 0
mensagem = "Um número esta sendo escolhido..."

for letra in mensagem:
    print(letra, end="", flush=True)
    time.sleep(0.05)

time.sleep(.5)
print("\nA maquina escolheu o número")
time.sleep(1)
while True:
    resposta = input("Digite o número que você acha que é entre 1 e 20: ").strip()
    tentativas+=1
    if not resposta:
        print("Digite um número antes de dar enter, animal")
        continue


    try:
        resposta_int = int(resposta)
    except ValueError:
        print("Essa porra nem é numero kct")
        continue

    if resposta_int > 20:
        print("É entre 1 e 20, você por acaso não sabe ler ??")

    if resposta_int == n:
        print("...")
        time.sleep(2)
        print("Você acertou!!!")
        if tentativas <= 1:
            print(f"Você levou {tentativas} chance para acertar")
        else:
            print(f"Você levou {tentativas} chances para acertar")
        break
    elif resposta_int < n:
        print("...")
        time.sleep(1)
        print("O número que procura é maior")
        
    else:
        print("...")
        time.sleep(1)
        print("O número que procura é menor")
        
