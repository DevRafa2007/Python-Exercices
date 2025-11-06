class SistemaAcademico:
    def __init__(self):
        self.cursos = []
        self.disciplinas = []
        self.professores = []
        self.alunos = []

    def cadastrar_curso(self, codigo, nome):
        curso = Curso(codigo, nome)
        self.cursos.append(curso)
        print(f"Curso {nome} cadastrado com sucesso!")

    def cadastrar_disciplina(self, codigo, nome):
        disciplina = Disciplina(codigo, nome)
        self.disciplinas.append(disciplina)
        print(f"Disciplina {nome} cadastrada com sucesso!")

    def cadastrar_professor(self, matricula, nome, disciplina, curso):
        professor = Professor(matricula, nome, disciplina, curso)
        self.professores.append(professor)
        print(f"Professor {nome} cadastrado com sucesso!")

    def cadastrar_aluno(self, matricula, nome, curso):
        aluno = Aluno(matricula, nome, curso)
        self.alunos.append(aluno)
        print(f"Aluno {nome} cadastrado com sucesso!")

    def cadastrar_nota(self, aluno, disciplina, nota):
        for a in self.alunos:
            if a.matricula == aluno.matricula:
                a.notas[disciplina.codigo] = nota
                if disciplina not in a.disciplinas_cursadas:
                    a.disciplinas_cursadas.append(disciplina)
                print(f"Nota {nota} cadastrada para o aluno {a.nome} na disciplina {disciplina.nome}")
                return
        print("Aluno não encontrado!")

    def calcular_media_aluno(self, aluno):
        if not aluno.notas:
            return 0
        return sum(aluno.notas.values()) / len(aluno.notas)

    def verificar_aprovacao(self, aluno):
        media = self.calcular_media_aluno(aluno)
        if media >= 7:
            return "Aprovado"
        elif 4 <= media < 7:
            disciplinas_recuperacao = []
            for disciplina in aluno.disciplinas_cursadas:
                if aluno.notas[disciplina.codigo] < 7:
                    disciplinas_recuperacao.append(disciplina)
            return ("Recuperação", disciplinas_recuperacao)
        else:
            return "Reprovado"

    def alterar_nota(self, aluno, disciplina, nova_nota):
        if disciplina.codigo in aluno.notas:
            aluno.notas[disciplina.codigo] = nova_nota
            print(f"Nota alterada com sucesso para {nova_nota}")
        else:
            print("Disciplina não encontrada para este aluno!")

    def gerar_relatorio_geral(self):
        print("\n=== RELATÓRIO GERAL ===")
        print("\nAlunos Matriculados:")
        for aluno in self.alunos:
            print(f"- {aluno.nome} (Matrícula: {aluno.matricula})")
        
        print("\nProfessores:")
        for professor in self.professores:
            print(f"- {professor.nome} (Matrícula: {professor.matricula})")
        
        print("\nCursos:")
        for curso in self.cursos:
            print(f"- {curso.nome} (Código: {curso.codigo})")
        
        print("\nDisciplinas:")
        for disciplina in self.disciplinas:
            print(f"- {disciplina.nome} (Código: {disciplina.codigo})")

    def gerar_relatorio_curso(self, curso):
        print(f"\n=== ALUNOS MATRICULADOS NO CURSO {curso.nome} ===")
        for aluno in self.alunos:
            if aluno.curso.codigo == curso.codigo:
                print(f"- {aluno.nome} (Matrícula: {aluno.matricula})")

    def gerar_relatorio_disciplina(self, disciplina):
        print(f"\n=== ALUNOS MATRICULADOS NA DISCIPLINA {disciplina.nome} ===")
        for aluno in self.alunos:
            if disciplina in aluno.disciplinas_cursadas:
                print(f"- {aluno.nome} (Matrícula: {aluno.matricula})")

    def gerar_relatorio_aluno(self, aluno):
        print(f"\n=== RELATÓRIO DO ALUNO {aluno.nome} ===")
        print(f"Curso: {aluno.curso.nome}")
        print("\nNotas por Disciplina:")
        for disciplina in aluno.disciplinas_cursadas:
            nota = aluno.notas.get(disciplina.codigo, 'Não avaliado')
            print(f"- {disciplina.nome}: {nota}")
        print(f"\nMédia Geral: {self.calcular_media_aluno(aluno):.2f}")

    def verificar_conclusao_curso(self, aluno):
        disciplinas_aprovadas = sum(1 for nota in aluno.notas.values() if nota >= 7)
        return disciplinas_aprovadas >= 10

    def emitir_certificado(self, aluno):
        if self.verificar_conclusao_curso(aluno):
            data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
            print("\n" + "="*50)
            print("CERTIFICADO DE CONCLUSÃO DE CURSO")
            print("="*50)
            print(f"\nCertificamos que {aluno.nome}")
            print(f"concluiu com êxito o curso de {aluno.curso.nome}")
            print(f"\nData de Emissão: {data_atual}")
            print("\n" + "="*50)
        else:
            print("O aluno ainda não cumpriu os requisitos para conclusão do curso!")

    # Novos métodos utilitários de busca
    def buscar_curso_por_codigo(self, codigo):
        return next((c for c in self.cursos if c.codigo == codigo), None)

    def buscar_disciplina_por_codigo(self, codigo):
        return next((d for d in self.disciplinas if d.codigo == codigo), None)

    def buscar_aluno_por_matricula(self, matricula):
        return next((a for a in self.alunos if a.matricula == matricula), None)

    def buscar_professor_por_matricula(self, matricula):
        return next((p for p in self.professores if p.matricula == matricula), None)