# 7. Somar a diagonal principal.

matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

for i in range(3):
    soma += matriz[i][i]

print("Soma da diagonal principal =", soma)