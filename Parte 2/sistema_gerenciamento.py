alunos = []

def salvar_dados():
    try:
        arquivo = open("c:/Users/vboxuser/Documents/alunos.txt", "w", encoding="utf-8")

        for aluno in alunos:
            linha = (
                aluno["nome"] + ";" +
                str(aluno["idade"]) + ";" +
                aluno["turma"] + ";" +
                str(aluno["notas"][0]) + ";" +
                str(aluno["notas"][1]) + ";" +
                str(aluno["notas"][2]) + ";" +
                str(aluno["notas"][3]) + "\n"
            )
            arquivo.write(linha)

        arquivo.close()
        print("Dados salvos com sucesso!")

    except:
        print("Erro ao salvar arquivo.")


def carregar_dados():
    try:
        arquivo = open("c:/Users/vboxuser/Documents/alunos.txt", "r", encoding="utf-8")

        for linha in arquivo:
            dados = linha.strip().split(";")

            aluno = {
                "nome": dados[0],
                "idade": int(dados[1]),
                "turma": dados[2],
                "notas": [
                    float(dados[3]),
                    float(dados[4]),
                    float(dados[5]),
                    float(dados[6])
                ]
            }

            alunos.append(aluno)

        arquivo.close()

    except FileNotFoundError:
        print("Arquivo ainda não existe.")


def cadastrar_aluno():

    aluno = {}

    aluno["nome"] = input("Nome do aluno: ")
    aluno["idade"] = int(input("Idade: "))
    aluno["turma"] = input("Turma: ")

    aluno["notas"] = [0, 0, 0, 0]

    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")


def lancar_notas():

    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            notas = []

            for i in range(4):
                nota = float(input(f"Digite a nota {i+1}: "))
                notas.append(nota)

            aluno["notas"] = notas

            print("Notas lançadas com sucesso!")
            return

    print("Aluno não encontrado.")


def consultar_aluno():

    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            media = sum(aluno["notas"]) / 4

            if media >= 7:
                situacao = "Aprovado"
            elif media >= 5:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"

            print("\n===== CONSULTA =====")
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Turma:", aluno["turma"])
            print("Notas:", aluno["notas"])
            print("Média:", round(media, 2))
            print("Situação:", situacao)

            return

    print("Aluno não encontrado.")


def relatorio_geral():

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    soma_medias = 0

    melhor_aluno = None
    pior_aluno = None

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    maior_media = -1
    menor_media = 11

    for aluno in alunos:

        media = sum(aluno["notas"]) / 4

        soma_medias += media

        if media > maior_media:
            maior_media = media
            melhor_aluno = aluno["nome"]

        if media < menor_media:
            menor_media = media
            pior_aluno = aluno["nome"]

        if media >= 7:
            aprovados += 1
        elif media >= 5:
            recuperacao += 1
        else:
            reprovados += 1

    media_turma = soma_medias / len(alunos)

    print("\n===== RELATÓRIO GERAL =====")
    print("Quantidade de alunos:", len(alunos))
    print("Média da turma:", media_turma)
    print("Melhor aluno:", melhor_aluno, "-",maior_media, 2)
    print("Pior aluno:", pior_aluno, "-", menor_media, 2)
    print("Aprovados:", aprovados)
    print("Recuperação:", recuperacao)
    print("Reprovados:", reprovados)

def menu():

    while True:

        print("\n===== SISTEMA DE GERENCIAMENTO ESCOLAR =====")
        print("1 - Cadastrar Aluno")
        print("2 - Lançar Notas")
        print("3 - Consultar Aluno")
        print("4 - Relatório Geral")
        print("5 - Salvar Dados")
        print("6 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                cadastrar_aluno()

            elif opcao == 2:
                lancar_notas()

            elif opcao == 3:
                consultar_aluno()

            elif opcao == 4:
                relatorio_geral()

            elif opcao == 5:
                salvar_dados()

            elif opcao == 6:
                salvar_dados()
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida!")

        except ValueError:
            print("Digite apenas números.")


carregar_dados()
menu()