matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"valor [{i}][{j}]: "))
        linha.append(valor)
        soma += valor
    matriz.append(linha)

print("\nMatriz:") 
for linha in matriz:
    print(linha)

print("soma dos elementos:", soma)

print("Diagonal principal:")
for i in range(3):
    print(matriz[i][i], end=" ")