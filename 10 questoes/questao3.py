# 3. Solicitar uma matriz 3x3 e exibila

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para[{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

    print("matriz:")
    for linha in matriz:
        print(linha)