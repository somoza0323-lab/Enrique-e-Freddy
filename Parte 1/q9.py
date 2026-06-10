nome = input("Dite o nome do aluno: ")

with open("c:/Users/vboxuser/alunos.txt", "a",encoding='utf-8') as arquivo:
    arquivo.write(nome + "\n")

print("Aluno salvo com sucesso!")