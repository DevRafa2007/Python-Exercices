import datetime 

def Nasc(idade):
    anoAtual = datetime.datetime.now().year
    anoNasc = anoAtual - idade
    return anoNasc

idade = int(input("Digite sua idade até o fim deste ano: "))
anoNasc = Nasc(idade)
print(f"Você nasceu em {anoNasc}.") 
