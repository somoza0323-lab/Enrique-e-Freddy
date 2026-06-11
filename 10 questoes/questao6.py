# 6. Exibir a diagonal pricipal de uma matriz 3x3.

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
print("Diagonal principal:")
for i in range(3):
    print(matriz[i][i])