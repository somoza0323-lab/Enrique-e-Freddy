# 4. Somar todos os elementos de uma matriz 3x3.

matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor para [{i}][{j}]: "))
        linha.append(linha)
        soma += valor 
    matriz.append(linha)
    
    print("Soma=",soma)