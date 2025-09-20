"""Script simples para testar as funções principais dos exercícios.
Executa alguns casos de fumaça para validar o comportamento.
"""

import ex1_media_tres_numeros as ex1
import ex2_par_impar as ex2
import ex3_pares_ate_n as ex3
import ex4_maior_menor_lista as ex4
import ex5_media_numeros_pares as ex5
import ex6_fatorial as ex6
import ex7_fibonacci_ate_n as ex7
import ex8_eh_primo as ex8
import ex9_nomes_com_a as ex9


def run_tests():
    erros = []

    if abs(ex1.media_tres(1, 2, 3) - 2.0) > 1e-9:
        erros.append('ex1 falhou')
    if ex2.eh_par(4) is not True or ex2.eh_par(5) is not False:
        erros.append('ex2 falhou')
    if ex3.pares_ate(7) != [0, 2, 4, 6]:
        erros.append('ex3 falhou')
    if ex4.maior_e_menor([3, 1, 2]) != (3, 1):
        erros.append('ex4 falhou')
    if ex5.media_pares([1, 2, 3, 4]) != 3.0:
        erros.append('ex5 falhou')
    try:
        if ex6.fatorial(5) != 120:
            erros.append('ex6 falhou')
    except Exception:
        erros.append('ex6 falhou com exceção')
    if ex7.fibonacci_ate(10) != [0, 1, 1, 2, 3, 5, 8]:
        erros.append('ex7 falhou')
    if ex8.eh_primo(13) is not True or ex8.eh_primo(1) is not False:
        erros.append('ex8 falhou')
    if ex9.filtrar_com_a(['Ana', 'bruno', 'Alice', 'Carlos']) != ['Ana', 'Alice']:
        erros.append('ex9 falhou')

    if erros:
        print('Testes: FALHOU')
        for e in erros:
            print('-', e)
    else:
        print('Testes: PASSARAM TODOS')


if __name__ == '__main__':
    run_tests()
