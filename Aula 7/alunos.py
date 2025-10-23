# alunos = {
#     "Aluno1": {"nota1": 7, "nota2":3},
#     "Aluno2": {"nota1": 10, "nota2":6},
#     "Aluno3": {"nota1": 8, "nota2":9}
# }

# for aluno in alunos.values():
#     media = (aluno["nota1"] + aluno["nota2"]) / 2
#     print(f"Média: {media}")

alunos = {
    "Aluno1": {8, 7},
    "Aluno2": {10, 6},
    "Aluno3": {9, 9}
}

for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{aluno} - Média: {media}")