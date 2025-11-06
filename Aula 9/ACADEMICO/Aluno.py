class Aluno:
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso
        self.notas = {}  # Dicionário para armazenar notas por disciplina
        self.disciplinas_cursadas = []