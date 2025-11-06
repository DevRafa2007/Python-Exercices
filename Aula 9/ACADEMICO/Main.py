
from SistemaAcademico import SistemaAcademico


def main():
    sistema = SistemaAcademico()

    def menu():
        print("\n=== SISTEMA ACADÊMICO ===")
        print("1 - Cadastrar curso")
        print("2 - Cadastrar disciplina")
        print("3 - Cadastrar professor")
        print("4 - Cadastrar aluno")
        print("5 - Cadastrar nota")
        print("6 - Alterar nota")
        print("7 - Relatório geral")
        print("8 - Relatório por curso")
        print("9 - Relatório por disciplina")
        print("10 - Relatório do aluno")
        print("11 - Emitir certificado do aluno")
        print("0 - Sair")

    while True:
        menu()
        op = input("Escolha uma opção: ").strip()
        if op == "1":
            codigo = input("Código do curso: ").strip()
            nome = input("Nome do curso: ").strip()
            if sistema.buscar_curso_por_codigo(codigo):
                print("Curso já cadastrado com esse código.")
            else:
                sistema.cadastrar_curso(codigo, nome)
        elif op == "2":
            codigo = input("Código da disciplina: ").strip()
            nome = input("Nome da disciplina: ").strip()
            if sistema.buscar_disciplina_por_codigo(codigo):
                print("Disciplina já cadastrada com esse código.")
            else:
                sistema.cadastrar_disciplina(codigo, nome)
        elif op == "3":
            matricula = input("Matrícula do professor: ").strip()
            nome = input("Nome do professor: ").strip()
            cod_disc = input("Código da disciplina (vinculada): ").strip()
            cod_curso = input("Código do curso (vinculado): ").strip()
            disc = sistema.buscar_disciplina_por_codigo(cod_disc)
            curso = sistema.buscar_curso_por_codigo(cod_curso)
            if not disc:
                print("Disciplina não encontrada.")
            elif not curso:
                print("Curso não encontrado.")
            else:
                if sistema.buscar_professor_por_matricula(matricula):
                    print("Professor já cadastrado com essa matrícula.")
                else:
                    sistema.cadastrar_professor(matricula, nome, disc, curso)
        elif op == "4":
            matricula = input("Matrícula do aluno: ").strip()
            nome = input("Nome do aluno: ").strip()
            cod_curso = input("Código do curso: ").strip()
            curso = sistema.buscar_curso_por_codigo(cod_curso)
            if not curso:
                print("Curso não encontrado.")
            else:
                if sistema.buscar_aluno_por_matricula(matricula):
                    print("Aluno já cadastrado com essa matrícula.")
                else:
                    sistema.cadastrar_aluno(matricula, nome, curso)
        elif op == "5":
            mat = input("Matrícula do aluno: ").strip()
            cod_disc = input("Código da disciplina: ").strip()
            try:
                nota = float(input("Nota (0-10): ").strip())
            except ValueError:
                print("Nota inválida.")
                continue
            aluno = sistema.buscar_aluno_por_matricula(mat)
            disc = sistema.buscar_disciplina_por_codigo(cod_disc)
            if not aluno:
                print("Aluno não encontrado.")
            elif not disc:
                print("Disciplina não encontrada.")
            else:
                sistema.cadastrar_nota(aluno, disc, nota)
        elif op == "6":
            mat = input("Matrícula do aluno: ").strip()
            cod_disc = input("Código da disciplina: ").strip()
            try:
                nova_nota = float(input("Nova nota (0-10): ").strip())
            except ValueError:
                print("Nota inválida.")
                continue
            aluno = sistema.buscar_aluno_por_matricula(mat)
            disc = sistema.buscar_disciplina_por_codigo(cod_disc)
            if not aluno:
                print("Aluno não encontrado.")
            elif not disc:
                print("Disciplina não encontrada.")
            else:
                sistema.alterar_nota(aluno, disc, nova_nota)
        elif op == "7":
            sistema.gerar_relatorio_geral()
        elif op == "8":
            cod_curso = input("Código do curso: ").strip()
            curso = sistema.buscar_curso_por_codigo(cod_curso)
            if not curso:
                print("Curso não encontrado.")
            else:
                sistema.gerar_relatorio_curso(curso)
        elif op == "9":
            cod_disc = input("Código da disciplina: ").strip()
            disc = sistema.buscar_disciplina_por_codigo(cod_disc)
            if not disc:
                print("Disciplina não encontrada.")
            else:
                sistema.gerar_relatorio_disciplina(disc)
        elif op == "10":
            mat = input("Matrícula do aluno: ").strip()
            aluno = sistema.buscar_aluno_por_matricula(mat)
            if not aluno:
                print("Aluno não encontrado.")
            else:
                sistema.gerar_relatorio_aluno(aluno)
        elif op == "11":
            mat = input("Matrícula do aluno: ").strip()
            aluno = sistema.buscar_aluno_por_matricula(mat)
            if not aluno:
                print("Aluno não encontrado.")
            else:
                sistema.emitir_certificado(aluno)
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()