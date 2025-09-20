jovens = 0
medios = 0
veios = 0
print("Vamos separar idades por faixas etarias")
while True:
    idade = int(input("Digite uma das idades: "))

    if 0<= idade <=25:
        jovens+=1
    elif 26<= idade <=60:
        medios +=1
    elif idade > 60:
        veios +=1
    else:
        print("Idade ivalida!!")

    cont = input("Deseja continuar e digitar mais uma idade? (s/n): ")

    if cont == "s":
        continue
    else:
        break

print("\nQuantidade de pessoas por faixa etaria: ")
print(f"0 a 25 anos: {jovens}")
print(f"26 a 60 anos: {medios}")
print(f"Acima de 60 anos: {veios}")