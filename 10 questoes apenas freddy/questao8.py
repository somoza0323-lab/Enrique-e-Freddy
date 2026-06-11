# 8. Contar numeros pares em uma matriz 4x4.

matriz = []
pares = 0

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para[{i}][{j}]: "))
        linha.append(valor)

        if valor % 2 == 0:
            pares += 1

    matriz.append(linha)

print("Quantidade de numeros pares =", pares)