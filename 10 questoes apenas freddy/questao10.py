# 10. Notas de 3 alunos em 4 bimestres

notas = []

for i in range(3):
    linha = []
    print(f"\nAlluno {i+1}")
    for j in range(4):
        nota = float(input(f"Nota do {j+1}° bimestre: "))
        linha.append(nota)
    notas.append(linha)

print("\nResultado:")
for i in range(3):
    media = sum(notas[i]) / 4

    if media >=7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print(f"Aluno {i+1}: Media = {media:2f}-{situacao}")