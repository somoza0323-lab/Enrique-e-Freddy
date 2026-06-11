# 9. Calcular a media dos elementos de uma matriz 3x3.

matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"digite o valor [{i}][{j}]:"))
        linha.append(valor)
        soma += valor
    matriz.append(linha)

media =  soma / 9

print("Mediaa =", media)