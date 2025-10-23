from datetime import date

def soma(valor1, valor2):
    return valor1 + valor2

def subtrai(valor1, valor2):
    return valor1 - valor2

def caracteres(nome):
    return len(nome)

def idade(ano_nasc):
    ano_atual = date.today().year
    return ano_atual - ano_nasc


def conversor(valor):
    valor_convertido = valor * 5.09
    return valor_convertido