numeros = ("um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    Entrada = int(input("Entre um numero de 1 a 20 para ver por extenso: "))
    if 0<=Entrada<=20:
        break
    
print(numeros[(Entrada - 1)])